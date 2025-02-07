install:
	pip install -r requirements.txt

build:
	cargo build --release
	cp target/release/libboost.so .

clean:
	# Remove the build .so file
	rm -f libboost.so