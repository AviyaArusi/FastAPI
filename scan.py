from modelScanner import H5CDR


def scanner(file_path: str):
    scanner = H5CDR(file_path)
    scan_results = scanner.scan()
    if scan_results:
        findings = scanner.analyze()
        return findings
    return scanner

def disarm(file_path: str):
    scanner = H5CDR(file_path)
    disarm_results = scanner.disarm()
    scanner.save_as_new_file("safe_model.h5")
    return disarm_results





