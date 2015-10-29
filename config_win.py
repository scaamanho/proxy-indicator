from gi.repository import Gtk as gtk, GLib
import ConfigParser
import os


class ConfigWin():
    def __init__(self):
        #Init Glade Builder
        builder = gtk.Builder()
        builder.add_from_file('proxy_config.glade')

        #Connect signals to builder
        self.window = builder.get_object('window')
        builder.connect_signals(self)

        # Get components from builder
        self.tf_host = builder.get_object('tf_host')
        self.tf_port = builder.get_object('tf_port')
        self.cb_auth = builder.get_object('cb_auth')
        self.tf_user = builder.get_object('tf_user')
        self.tf_pass = builder.get_object('tf_pass')

        #Read configuration
        self.config_file = os.getenv("HOME")+'/.config/proxy-indicator/config.ini'
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.config_file)

        #Set values from configuration
        self.tf_host.set_text(self.config.get('ProxyConfig', 'proxy.host'))
        self.tf_port.set_text(self.config.get('ProxyConfig', 'proxy.port'))
        self.tf_user.set_text(self.config.get('ProxyConfig', 'proxy.user'))
        self.tf_pass.set_text(self.config.get('ProxyConfig', 'proxy.password'))
        self.cb_auth.set_active(False)
        if self.config.get('ProxyConfig', 'proxy.auth') == 'True':
            self.cb_auth.set_active(True)

        #Enable/Disable user/pwd fields
        self.cb_auth_toggled(self.cb_auth)

    def show(self):
        self.window.show()

    def bt_accept_clicked(self, button):
        self.save_config_file()
        self.window.destroy()

    def bt_cancel_clicked(self, button):
        self.window.destroy()

    def cb_auth_toggled(self, button):
        value = button.get_active()
        # disable user/pwd fields
        self.tf_user.set_sensitive(value)
        self.tf_pass.set_sensitive(value)

    def on_bt_accept(self, widget):
        self.save_config_file()
        self.window.destroy()

    def on_bt_cancel(self, widget):
        self.window.destroy()

    def on_auth_selected(self, button):
        value = button.get_active()
        # disable user/pwd fields
        self.user_entry.set_sensitive(value)
        self.pwd_entry.set_sensitive(value)

    def save_config_file(self):
        # Set Config values
        self.config.set('ProxyConfig', 'proxy.host', self.tf_host.get_text().strip())
        self.config.set('ProxyConfig', 'proxy.port', self.tf_port.get_text().strip())
        self.config.set('ProxyConfig', 'proxy.auth', self.cb_auth.get_active())
        self.config.set('ProxyConfig', 'proxy.user', self.tf_user.get_text().strip())
        self.config.set('ProxyConfig', 'proxy.password', self.tf_pass.get_text().strip())

        # Write configuration to file
        with open(self.config_file, 'wb') as configfile:
            self.config.write(configfile)
