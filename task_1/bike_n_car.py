class bike:
    def __init__(f,acceleration):
        f.current_speed=0
        f.acceleration=acceleration
        f.brand='Harley Davidson'
        f.color='white'
        f.mileage=50
        f.no_of_gears=4
        f.no_of_seats=2
        f.max_speed=100
        f.engine_status=0
        f.cost=70000
    def increase_speed(f):
        if f.engine_status==1:
            f.current_speed+=f.acceleration
        else:
            f.current_speed=0     
    def decrease_speed(f):
        if f.engine_status==1:
            f.current_speed-=f.acceleration
        else:
            f.current_speed=0
    def start_engine(f):
        f.engine_status=1
    def stop_engine(f):
        f.engine_status=0
    def apply_brakes(f):
        f.current_speed=0

class car:
    def __init__(f,acceleration):
        f.current_speed=0
        f.acceleration=acceleration
        f.brand='Tesla'
        f.color='Grey'
        f.mileage=30
        f.no_of_gears=6
        f.no_of_seats=4
        f.max_speed=120
        f.engine_status=0
        f.cost=200000
    def increase_speed(f):
        if f.engine_status==1:
            f.current_speed+=f.acceleration
        else:
            f.current_speed=0     
    def decrease_speed(f):
        if f.engine_status==1:
            f.current_speed-=f.acceleration
        else:
            f.current_speed=0
    def start_engine(f):
        f.engine_status=1
    def stop_engine(f):
        f.engine_status=0
    def apply_brakes(f):
        f.current_speed=0

        
