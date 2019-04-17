import sx127x
import config_lora

import LoRaSender

def main():

    '''
    pin_id_led = ON_BOARD_LED_PIN_NO
    on_board_led_high_is_on = ON_BOARD_LED_HIGH_IS_ON
    pin_id_reset = PIN_ID_FOR_LORA_RESET
    blink_on_start = (2, 0.5, 0.5)
    '''
    controller = config_lora.Controller()

    '''
    name = 'SX127x'
    parameters = {'frequency': 433E6, 'tx_power_level': 2, 'signal_bandwidth': 125E3,
                  'spreading_factor': 8, 'coding_rate': 5, 'preamble_length': 8,
                  'implicitHeader': False, 'sync_word': 0x12, 'enable_CRC': False}
    onReceive = None
    '''
    SX127x_Ins = sx127x.SX127x(name='LoRa')

    '''
    transceiver: SX127x
    pin_id_ss = PIN_ID_FOR_LORA_SS
    pin_id_RxDone = PIN_ID_FOR_LORA_DIO0
    pin_id_RxTimeout = PIN_ID_FOR_LORA_DIO1
    pin_id_ValidHeader = PIN_ID_FOR_LORA_DIO2
    pin_id_CadDone = PIN_ID_FOR_LORA_DIO3
    pin_id_CadDetected = PIN_ID_FOR_LORA_DIO4
    pin_id_PayloadCrcError = PIN_ID_FOR_LORA_DIO5
    '''
    lora = controller.add_transceiver(SX127x_Ins,
                                      pin_id_ss=config_lora.Controller.PIN_ID_FOR_LORA_SS,
                                      pin_id_RxDone=config_lora.Controller.PIN_ID_FOR_LORA_DIO0)
    print('lora', lora)
       
    LoRaSender.send(lora)
  
if __name__ == '__main__':
    main()