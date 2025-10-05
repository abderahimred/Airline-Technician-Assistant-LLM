from src.inference import predict_action

problem = "Engine vibration at takeoff"
action = predict_action(problem)
print(action)
