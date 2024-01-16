import abc
import enum
from typing import List


class CaseStatus(enum.Enum):
    PASS = 0
    FAIL = 1
    BLOCK = 2
    UNKNOWN = 3


class DeviceObject:
    def __init__(self, rta_host, rta_port, rta_user, rta_pwd, slot_extent=1):
        pass
        # self.rta = rta
        # self.rtb = rtb
        self.slot_extent = slot_extent


class BaseCase(abc.ABC):
    def __init__(self, dev_list: List[DeviceObject, None], log_obj=None):
        self.dev_list = dev_list
        self.log_obj = log_obj
        self.__count = 0
        self.status = CaseStatus.PASS

    def exec_case(self):
        try:
            self.__count += 1
            self.case_start()
            self.method()
            self.case_end()

            self.status = CaseStatus.PASS
        except Exception as e:
            self.log_obj.log_error(e)
            self.status = CaseStatus.FAIL

    @property
    def get_count(self):
        return self.__count

    def method(self):
        pass

    def case_start(self):
        # TODO 登录设备

        # TODO 执行测试套

        # TODO 设备检查

        # TODO 退出设备
        pass

    def case_end(self):
        pass
