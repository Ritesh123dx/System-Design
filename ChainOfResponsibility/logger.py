from abc import ABC

class LogProcessor(ABC):

    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, log_processor : 'LogProcessor'):
        self.next_log_processor = log_processor
    
    def log(self, log_level, msg):
        
        if self.next_log_processor != None:
            self.next_log_processor.log(log_level, msg)
        else:
            print("Invalid log level provided")


class InfoLogProcessor(LogProcessor):
    def __init__(self, log_processor : LogProcessor):
        super().__init__(log_processor)
    
    def log(self, log_level, msg):
        if log_level == LogProcessor.INFO:
            print(f"INFO: {msg}")
        else:
            super().log(log_level, msg)


class DebugLogProcessor(LogProcessor):
    def __init__(self, log_processor : LogProcessor):
        super().__init__(log_processor)
    
    def log(self, log_level, msg):
        if log_level == LogProcessor.DEBUG:
            print(f"DEBUG: {msg}")
        else:
            super().log(log_level, msg)


log_processor = InfoLogProcessor(DebugLogProcessor(None))
log_processor.log(LogProcessor.INFO, "This is an information message")
log_processor.log(LogProcessor.DEBUG, "This is a debug message")
log_processor.log(LogProcessor.ERROR, "This is an error message")
