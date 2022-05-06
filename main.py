from config.entry import Configuration
from runner import run

def main():
    config = Configuration()
    config.run__config()
    run()
    
if __name__ == "__main__":
    main()