# Proxy Indicator  

Proxy Indicator is a tool utility so set/unset proxy settings in ubuntu 
in corporative networks where user and password are needed. 
 
You can set/unset proxy settings in a click  

Use your default proxy configuration to set proxy

### dependencies 
* python-gtk3
* gir1.2-appindicator-0.1
* gir1.2-appindicator3-0.1


### *gnome 3 extension* 

[appindicator-support](https://extensions.gnome.org/extension/615/appindicator-support/).


### Tested in 
* Ubuntu 14.04
* Xubuntu 14.04
* Lubuntu 14.04
* Ubuntu Gnome 14.04
* Ubuntu Mate 15.10


This project is roughly inspired in 
[uproxy](https://code.google.com/p/ubproxy/).  

## Version  
* V 0.3.1 [2015/11/14]

##Changelog
* V 0.3 [2015/10/28]
* V 0.2 [2015/10/27]
* V 0.1 [2015/10/26]

## Install  
[TODO]  
extract file and move `proxy-indicator` directory to `/opt/extras.ubuntu.com/`

```sh
sudo mkdir -p  /usr/local/bin/proxy-indicator/
tar xvf proxy-indicator.tar.gz
chmod +x proxy-indicator/run
sudo mv proxy-indicator /usr/local/bin/proxy-indicator/
```

Add `/usr/local/bin/proxy-indicator/run` to inital programs on your desktop

## Configure    
[TODO]

## Extra Info  
[TODO]
