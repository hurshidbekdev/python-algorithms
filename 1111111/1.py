car0={
    'model':'gentra',
    'rang':'qizil',
    'yil':2000,
    'narh':2000
}
car1={
    'model':'lacetti',
    'rang':'kok',
    'yil':2010,
    'narh':1200
}
car2={
    'model':'mers',
    'rang':'oq',
    'yil':2019,
    'narh':1500
}
cars=[car0,car1,car2]
for car in cars:
  print(f'{car["model"].title()},'
        f'{car["rang"].title()},'
        f'{car["yil"]}-yil,{car["narh"]}$'
      )

















