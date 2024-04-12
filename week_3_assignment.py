# Copyright 2024 Steve Nginyo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def calculate_discount(price, discount_percent):
    if(discount_percent<20):
        return price
    else:
        return (1-(discount_percent/100))*price
    
def askPrice():
    return input('Enter price \n')

def askDiscount():
    return input('Enter discount \n')

price = int(askPrice())
discount = int(askDiscount())

if(discount>100):
    raise Exception("Sorry, invalid discount")

print("Here is the final price",calculate_discount(price, discount))