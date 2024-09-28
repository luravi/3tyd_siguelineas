derecha = Math.random_boolean()

def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 20 and maqueen.ultrasonic(PingUnit.CENTIMETERS) > 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 200)
    
    elif derecha == True:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 200)

basic.forever(on_forever)
