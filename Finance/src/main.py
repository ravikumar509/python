from tracker.Tracker import Tracker
def main():
    print("***************************")
    print("Welcome to Expenses Tracker")
    print("***************************")
    tracker = Tracker()
    tracker.get_balance()
    tracker.menu()
    

if __name__ == "__main__":
    main()