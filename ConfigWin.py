from gi.repository import Gtk, GLib
import ConfigParser


class ConfigWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Proxy Configuration")

        # Set window properties
        self.set_icon_from_file('proxy_on.png')
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(400, 100)

        # Load proxy configuration
        self.config = ConfigParser.RawConfigParser()
        self.config.read('config.ini')

        # Components
        label_host = Gtk.Label()
        label_host.set_text("Host:")
        self.host_entry = Gtk.Entry()
        self.host_entry.set_text(self.config.get('ProxyConfig', 'proxy.host'))

        label_port = Gtk.Label()
        label_port.set_text("Port:")
        self.port_entry = Gtk.Entry()
        self.port_entry.set_text(self.config.get('ProxyConfig', 'proxy.port'))

        self.check_auth = Gtk.CheckButton("Authentication")
        self.check_auth.connect("toggled", self.on_auth_selected)

        label_user = Gtk.Label()
        label_user.set_text("User:")
        self.user_entry = Gtk.Entry()
        self.user_entry.set_text(self.config.get('ProxyConfig', 'proxy.user'))

        label_pwd = Gtk.Label()
        label_pwd.set_text("Port:")
        self.pwd_entry = Gtk.Entry()
        self.pwd_entry.set_visibility(False)
        self.pwd_entry.set_text(self.config.get('ProxyConfig', 'proxy.password'))

        self.accept = Gtk.Button(label="Accept")
        self.accept.connect("clicked", self.on_bt_accept)
        self.cancel = Gtk.Button(label="Cancel")
        self.cancel.connect("clicked", self.on_bt_cancel)

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, border_width=10)
        self.add(vbox)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        hbox.pack_start(label_host, False, False, 0)
        hbox.pack_start(self.host_entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        hbox.pack_start(label_port, False, False, 0)
        hbox.pack_start(self.port_entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        hbox.pack_start(self.check_auth, False, False, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        hbox.pack_start(label_user, False, False, 0)
        hbox.pack_start(self.user_entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        hbox.pack_start(label_pwd, False, False, 0)
        hbox.pack_start(self.pwd_entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        hbox.pack_start(self.accept, True, True, 0)
        hbox.pack_start(self.cancel, True, True, 0)

        if self.config.get('ProxyConfig', 'proxy.auth') == 'True':
            self.check_auth.set_active(True)
        else:
            self.check_auth.set_active(False)
        self.on_auth_selected(self.check_auth)

    def on_bt_accept(self, widget):
        self.save_config_file()
        self.destroy()

    def on_bt_cancel(self, widget):
        self.destroy()

    def on_auth_selected(self, button):
        value = button.get_active()
        # disable user/pwd fields
        self.user_entry.set_sensitive(value)
        self.pwd_entry.set_sensitive(value)

    def save_config_file(self):
        # Set Config values
        self.config.set('ProxyConfig', 'proxy.host', self.host_entry.get_text().strip())
        self.config.set('ProxyConfig', 'proxy.port', self.port_entry.get_text().strip())
        self.config.set('ProxyConfig', 'proxy.auth', self.check_auth.get_active())
        self.config.set('ProxyConfig', 'proxy.user', self.user_entry.get_text().strip())
        self.config.set('ProxyConfig', 'proxy.password', self.pwd_entry.get_text().strip())

        # Write configuration to file
        with open('config.ini', 'wb') as configfile:
            self.config.write(configfile)
