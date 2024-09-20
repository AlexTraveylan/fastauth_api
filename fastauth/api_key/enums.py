from enum import Enum


class PlanEnum(Enum, str):
    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"
