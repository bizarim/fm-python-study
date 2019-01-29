import Libs.common.packet
import Libs.database.query

def run_test():
    Libs.common.packet.send()
    Libs.database.query.excute()
    Libs.common.packet.recv()
    

run_test()