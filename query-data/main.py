import asyncio

from pysungrow import identify, SungrowClient
from pymodbus.client import AsyncModbusTcpClient


async def get_data():
    modbus_client = AsyncModbusTcpClient("192.168.178.128")

    # first we need to identify the model of inverter...
    serial_number, device, output_type = await identify(modbus_client)

    # ...then we can create a client...
    client = SungrowClient(modbus_client, device, output_type)

    # ...using which we can get data
    return await client.get("total_dc_power")


if __name__ == '__main__':
    asyncio.run(get_data())
