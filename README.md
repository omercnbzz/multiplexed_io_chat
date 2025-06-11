#  I/O Multiplexing 

Bu proje, Python'da aynı anda hem terminal girdisini (stdin) hem de soket bağlantısını dinleyerek nasıl mesajlaşma yapılabileceğini gösteren bir örnektir. `select` modülü kullanılarak I/O multiplexing gerçekleştirilmiştir.

## Amaç

Python'da terminal üzerinden kullanıcıdan giriş alırken, aynı zamanda ağdan (socket) gelen verileri dinlemenin yolunu göstermek.

## Dosyalar

- `iomulti.py`: Ana dosya. Sunucuya bağlanır ve hem terminalden hem de sunucudan gelen mesajları okur.

## Gereksinimler

- Python 3.x

## Kullanım

1. Bir TCP sunucu başlatın (örneğin başka bir terminalde `chat_server.py` gibi bir şey).
2. İstemciyi başlatın:

```bash
python iomulti.py
