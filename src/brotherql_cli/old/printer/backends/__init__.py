# from brotherql_cli.printer.backends.generic import BrotherQLBackendGeneric

def backend_factory():
    from brotherql_cli.printer.backends.network import BrotherQLBackendNetwork
    return BrotherQLBackendNetwork
