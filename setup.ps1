if (Test-Path .venv){
    Remove-Item -r .venv
}
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
activate .venv
