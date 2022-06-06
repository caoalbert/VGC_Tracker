# VGC_Tracker

VGC Tracker is a python script that helps track giftcard balances. 

To initialize:
```
python3 vgc.py initialize
```
To add a new giftcard/deduct balance on an exisiting giftcard:
```
python3 vgc.py name-of-gift-card amount/intial-balance
```
To lookup balance on an existing giftcard:
```
python3 vgc.py name-of-gift-card
```
To return all giftcards with balance:
```
python3 vgc.py list
```
To remove all existing giftcard:
```
python3 vgc.py reset
```

The tracker automatically removes giftcards that have 0 dollar balance after the last deduction. 