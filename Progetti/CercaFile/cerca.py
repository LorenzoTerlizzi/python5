import os
import mmap
import shutil
import datetime
import PyPDF2
import textract

# Funzione principale
def main():
    sRoot = input("Inserisci la root directory: ")
    sStringaDaCercare = input("Inserisci la stringa da cercare: ")
    sOutDir = input("Inserisci la dir di output: ")

    if not os.path.isdir(sRoot):
        print("La directory specificata non esiste.")
        return

    now = datetime.datetime.now()
    dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
    sOutSubDir = os.path.join(sOutDir, dt_string)
    os.makedirs(sOutSubDir, exist_ok=True)

    iNumFileTrovati = 0
    iNumFileCercati = 0

    for root, dirs, files in os.walk(sRoot):
        # Evita la directory di output
        if in_directory(root, sOutSubDir):
            continue

        for filename in files:
            iNumFileCercati += 1
            pathCompleto = os.path.join(root, filename)

            if CercaStringaInFilename(filename, sStringaDaCercare):
                print("Trovato file:", filename)
                iNumFileTrovati += 1
                SalvaFile(pathCompleto, filename, sOutSubDir)
            elif CercaStringaInFileContent(pathCompleto, sStringaDaCercare):
                print("Trovato file nel contenuto:", filename)
                iNumFileTrovati += 1
                SalvaFile(pathCompleto, filename, sOutSubDir)

    print(f"Trovati {iNumFileTrovati} file su {iNumFileCercati} file presenti.")


def CercaStringaInFilename(sFilename, sStringToSearch):
    sFilename1 = sFilename.lower()
    sStringToSearch1 = sStringToSearch.lower()
    return sFilename1.find(sStringToSearch1) > -1


def CercaStringaInFileContent(sFile, sString):
    sString = sString.lower()
    iLen = len(sString)
    try:
        with open(sFile, "rb") as f:
            if sFile.lower().endswith(".pdf"):
                return CercaInFilePdf(sFile, sString)
            elif sFile.lower().endswith((".doc", ".docx")):
                return CercaInFileDoc(sFile, sString)
            else:
                s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                sAppo = s.readline()
                while len(sAppo) > 0:
                    if sString.encode() in sAppo.lower():
                        return True
                    sAppo = s.readline()
    except Exception as e:
        print(f"Errore nella lettura di {sFile}: {e}")
    return False


def CercaInFilePdf(sFile, sString):
    try:
        pdfReader = PyPDF2.PdfFileReader(sFile)
        for page_num in range(pdfReader.numPages):
            text = pdfReader.getPage(page_num).extractText().lower()
            if sString in text:
                return True
    except Exception as e:
        print(f"Errore nella lettura del PDF {sFile}: {e}")
    return False


def CercaInFileDoc(sFile, sString):
    try:
        text = textract.process(sFile).decode('utf-8').lower()
        return sString in text
    except Exception as e:
        print(f"Errore nella lettura del DOC {sFile}: {e}")
    return False


def SalvaFile(sFilePath, sFileName, sOutDir):
    sFilePathNew = os.path.abspath(sFilePath).replace("_", "__").replace("\\", "_").replace("/", "_")
    sOutFile = os.path.join(sOutDir, sFilePathNew)
    os.makedirs(os.path.dirname(sOutFile), exist_ok=True)
    shutil.copyfile(sFilePath, sOutFile)
    print(f"File copiato in: {sOutFile}")


def in_directory(dir1, dir2):
    directory1 = os.path.abspath(dir1).lower()
    directory2 = os.path.abspath(dir2).lower()
    return directory1.startswith(directory2)


if __name__ == "__main__":
    main()
