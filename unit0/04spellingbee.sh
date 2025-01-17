gunzip -c dictionary.gz | grep -E "^[zoniacr]*r[zoniacr]*$"| grep -E ".{4,}"| wc
