WIN = windows
LIN = linux
SCRIPT = two_to_ten.py
WIN_EXE = --onefile $(SCRIPT) --distpath $(WIN) --workpath $(WIN) --specpath $(WIN) --clean
LIN_EXE = --onefile $(SCRIPT) --distpath $(LIN) --workpath $(LIN) --specpath $(LIN) --clean


windows:
	mkdir $(WIN)
	pip install pyinstaller
	pyinstaller $(WIN_EXE)
	./$(WIN)/two_to_ten.exe

linux:
	mkdir $(LIN)
	pip install pyinstaller
	pyinstaller $(LIN_EXE)
	./$(LIN)/two_to_ten.exe

web:
	cmd /c start http://localhost:8000/two_to_ten.html
	python -m http.server 8000

clean:
	rm -rf $(WIN)
	rm -rf $(LIN)