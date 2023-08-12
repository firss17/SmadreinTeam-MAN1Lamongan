import time
import json
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

if __name__ == "__main__":
    try:
        # Connect to the slave
        serial1 = serial.Serial(
                               port='/dev/ttyS0',
                               baudrate=9600,
                               bytesize=8,
                               parity='N',
                               stopbits=1,
                               xonxoff=0
                              )

        serial2 = serial.Serial(
                               port='/dev/ttyS0',
                               baudrate=9600,
                               bytesize=8,
                               parity='N',
                               stopbits=1,
                               xonxoff=0
                              )

        master1 = modbus_rtu.RtuMaster(serial1)

        master2 = modbus_rtu.RtuMaster(serial2)
        master1.set_timeout(2.0)
        master1.set_verbose(True)
        master2.set_timeout(2.0)
        master2.set_verbose(True)
        # Changing power alarm value to 100 W
        # master.execute(1, cst.WRITE_SINGLE_REGISTER, 1, output_value=100)
        dict_payload = dict()

        while True:
            data1 = master1.execute(1, cst.READ_INPUT_REGISTERS, 0, 10)
            data2 = master2.execute(1, cst.READ_INPUT_REGISTERS, 0, 10)

            dict_payload["voltage 1"]= data1[0] / 10.0
            dict_payload["current1_A"] = (data1[1] + (data1[2] << 16)) / 1000.0 # [A]
            dict_payload["power1_W"] = (data1[3] + (data1[4] << 16)) / 10.0 # [W]
            dict_payload["energy1_Wh"] = data1[5] + (data1[6] << 16) # [Wh]
            dict_payload["frequency1_Hz"] = data1[7] / 10.0 # [Hz]
            dict_payload["power_factor1"] = data1[8] / 100.0
            dict_payload["alarm1"] = data1[9] # 0 = no alarm
            str_payload = json.dumps(dict_payload, indent=2)

            dict_payload["voltage2"]= data2[0] / 10.0
            dict_payload["current2_A"] = (data2[1] + (data2[2] << 16)) / 1000.0 # [A]
            dict_payload["power2_W"] = (data2[3] + (data2[4] << 16)) / 10.0 # [W]
            dict_payload["energy2_Wh"] = data2[5] + (data2[6] << 16) # [Wh]
            dict_payload["frequency2_Hz"] = data2[7] / 10.0 # [Hz]
            dict_payload["power2_factor"] = data2[8] / 100.0
            dict_payload["alarm2"] = data2[9] # 0 = no alarm
            str_payload = json.dumps(dict_payload, indent=2)
            print(str_payload)
            time.sleep(2)


    except KeyboardInterrupt:
        print('exiting pzem script')
    except Exception as e:
        print(e)
    finally:
        master1.close()
        master2.close() 

