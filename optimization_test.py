import requests

url = "http://127.0.0.1:5000/optimize"

# Define different test cases with various targets and constraints
test_cases = [
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "time(sec)", "type": "leq", "value": 42}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "time(sec)", "type": "leq", "value": 83}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "time(sec)", "type": "leq", "value": 143}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "memPeak(MB)", "type": "leq", "value": 145.09}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "memPeak(MB)", "type": "leq", "value": 161.78}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "memPeak(MB)", "type": "leq", "value": 201.64}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "sol(keuro)", "type": "leq", "value": 309.87}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "sol(keuro)", "type": "leq", "value": 341.34}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "sol(keuro)", "type": "leq", "value": 367.09}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "memAvg(MB)", "type": "leq", "value": 130.50}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "memAvg(MB)", "type": "leq", "value": 143.02}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "memAvg(MB)", "type": "leq", "value": 152.51}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "memAvg(MB)", "type": "leq", "value": 130.50}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "totEnergy(kW)", "type": "leq", "value": 0.000040}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "totEnergy(kW)", "type": "leq", "value": 0.000612}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    },
    {
        "algorithm": "anticipate",
        "objective": {"target": "CO2e(kg)", "type": "min"},
        "robustness_fact": None,
        "constraints": [{"target": "totEnergy(kW)", "type": "leq", "value": 0.001570}],
        "inputs": [
            {"name": "load_std", "value": 269.26},
            {"name": "load_mean", "value": 277.45},
            {"name": "pv_std", "value": 317.21},
            {"name": "pv_mean", "value": 166.42}
        ],
        "country": "Italy"
    }
    # Add additional test cases as needed...
]

if __name__ == "__main__":

    for idx, payload in enumerate(test_cases, start=1):
        response = requests.post(url, json=payload)
        try:
            data = response.json()
        except Exception as e:
            data = f"Failed to parse JSON: {e}"
        print(f"Test case {idx}: {data}")
