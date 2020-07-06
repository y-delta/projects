import requests
import sys

def fetch_data():
    url = "https://api.covid19india.org/data.json"
    data = requests.get(url)
    data = data.json()
    data = data["statewise"][0]
    
    total_cases = data["confirmed"]
    active_cases = int(data["active"])
    new_active = int(data["deltaconfirmed"])
    deaths = data["deaths"]
    new_deaths = int(data["deltadeaths"])
    recovered = data["recovered"]
    new_recovery = int(data["deltarecovered"])
    print('India\nTotal cases : {0}\nActive Cases: {1} {2:+}\nDeaths : {3} {4:+}\nRecovered : {5} {6:+}'.format(total_cases,active_cases,new_active,deaths,new_deaths,recovered,new_recovery))


def fetch_data_by_state(state):
    url = "https://api.covid19india.org/v3/data.json"
    data = requests.get(url)
    data = data.json()
    new_cases = data[state.upper()]["delta"]
    data = data[state.upper()]["total"]

    total_cases = data["confirmed"]
    new_cases = new_cases["confirmed"]
    deaths = data["deceased"]
    recovered = data["recovered"]
    print('{0}\nTotal cases : {1} {2:+}\nDeaths : {3}\nRecovered : {4}'.format(state.upper(),total_cases,new_cases,deaths,recovered))

def fetch_district_data(state, district):
    url = "https://api.covid19india.org/state_district_wise.json" 
    data = requests.get(url)
    data = data.json()
    data = data[state]
    data = data["districtData"][district]

    total_cases = data["confirmed"]
    active_cases = int(data["active"])
    deaths = data["deceased"]
    recovered = data["recovered"]

    print('{0}\nTotal cases : {1}\nActive Cases: {2}\nDeaths : {3}\nRecovered : {4}'.format(district, total_cases,active_cases,deaths,recovered))


def world_data():
    url = ""
    #Not Implemented Yet

def main():
    if len(sys.argv)==3:
        fetch_district_data(sys.argv[1],sys.argv[2])
    elif len(sys.argv)==2:
        if sys.argv[1]=="world":
            world_data()
        else:
            fetch_data_by_state(sys.argv[1])
    else:
        fetch_data()

if __name__=="__main__":
    main()

