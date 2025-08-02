select round(avg(DAILY_FEE),0) as AVERGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = "SUV"
