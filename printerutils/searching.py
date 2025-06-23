import subprocess

def ping_network(base_ip='192.168.1.', start=1, end=254):
    live = []
    for i in range(start, end+1):
        ip = f"{base_ip}{i}"
        res = subprocess.run(['ping','-c','1','-W','1',ip],
                             stdout=subprocess.DEVNULL)
        if res.returncode == 0:
            live.append(ip)
    return live

from easysnmp import Session, EasySNMPTimeoutError, EasySNMPError

def query_printer(ip, community='public', version=2):
    sess = Session(hostname=ip, community=community, version=version)
    try:
        sys_descr = sess.get('sysDescr.0').value
        sys_object = sess.get('sysObjectID.0').value
        sys_location = sess.get('sysLocation.0').value
    except EasySNMPTimeoutError:
        return None
    except EasySNMPError:
        return None

    # Optional: use printer-specific Object IDs
    toner_level = None
    try:
        oid = '1.3.6.1.2.1.43.11.1.1.9.1'  # prtMarkerSuppliesLevel.1
        toner_level = sess.get(oid).value
    except EasySNMPError:
        pass

    return dict(ip=ip, sys_descr=sys_descr, sys_object=sys_object,
                sys_location=sys_location, toner_level=toner_level)

def scan_lan_for_printers(base_ip='192.168.1.', community='public'):
    hosts = ping_network(base_ip)
    printers = []
    for ip in hosts:
        info = query_printer(ip, community)
        if info:
            printers.append(info)
    return printers

if __name__ == '__main__':
    found = scan_lan_for_printers('192.168.1.', 'public')
    for p in found:
        print(f"{p['ip']}: {p['sys_descr']} @ {p['sys_location']};")
