if (Test-Path .venv){
    Remove-Item -r .venv
}
python -m venv .venv
.venv\Scripts\python.exe -m pip install tabulate
.venv\Scripts\python.exe -m pip install pandas
.venv\Scripts\python.exe -m pip install openpyxl
.venv\Scripts\python.exe -m pip install pathlib
activate .venv
