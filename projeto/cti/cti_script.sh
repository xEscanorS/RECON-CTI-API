#!/bin/bash

echo "Coloque sua plataforma:";
read plataforma;

echo "Coloque sua api_key:";
read api_key;

if [[ "$plataforma" == "VT" ]]; then
  echo "Coloque sua hash:";
  read hash;
  python ./projeto/cti/reconCTI.py -t "$plataforma" -a "$api_key" -hs "$hash";
  mkdir -p /saida
  mv VT-CTI.csv /saida/
else 
  echo "Coloque seu ip:";
  read ip;
  python ./projeto/cti/reconCTI.py -t "$plataforma" -a "$api_key" -i "$ip";
  mkdir -p /saida
  mv CENSYS-CTI.csv /saida/
fi
