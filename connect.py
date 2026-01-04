import re
from wifi import Cell, Scheme
import wifi.subprocess_compat as subprocess
from wifi.utils import ensure_file_exists

class SchemeWPA(Scheme):
    def __init__(self, interface, name, options=None):
        self.interface = interface
        self.interfaces = "/etc/wpa_supplicant/wpa_supplicant-" + interface + ".conf"
        self.name = name
        self.options = options or {}

    def __str__(self):
        options = ''.join("\n    {k}=\"{v}\"".format(k=k, v=v) for k, v in self.options.items())
        return "country=EC" + "\n" + "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev" + "\n" + "update_config=1" + "\n" + "network={" + options + "\n    mode=0" + "\n}\n"

    def __repr__(self):
            return 'Scheme(interface={interface!r}, name={name!r}, options={options!r}'.format(**vars(self))
            
    def save(self):
        """
        Writes the configuration to the :attr:`interfaces` file.
        """
        if not self.find(self.interface, self.name):
            with open(self.interfaces, 'w') as f:
                f.write('\n')
                f.write(str(self))        
