# Cvičení: Regulární výrazy

Řešeno na <https://regex101.com/>

## Předčíslí

```txt
\d{0,6}-?\d{6,10}/\d{4}
```
https://regex101.com/r/n7x9Wg/1

Není to dokonalé, ale jako řešení stačí

## Číslo účtu podruhé

```txt
[12][1-3]\d{6,8}/2100
```
https://regex101.com/r/VoUKri/1


## Registrační značka

```txt
\d[A-Z]\w \d{4}
\d(A|B|C|E|H|J|K|L|M|P|S|T|U|Z)\w \d{4}
```

https://regex101.com/r/wXlJDo/1
https://regex101.com/r/ZrPyTs/1

## Telefonní číslo

```txt
(\+420)? ?\d{3} ?\d{3} ?\d{3}
```
https://regex101.com/r/O50NSs/1


## Ministerstva

```txt
Ministerstvo[\w ]*
```
https://regex101.com/r/wrXVhD/1

## Nápravy

```txt
\w{1}\,\w{1} m
\w{2}\,\w{2} t
```
https://regex101.com/r/RydgSW/1
https://regex101.com/r/hbwv8Z/1

## Slavný soude

```txt
\d{2} [A-Z] \d{1,4}/\d{4}
```

https://regex101.com/r/zy8n4X/1

## Ave, Caesar

```txt
I?(V|X)?I{0,3}
```
https://regex101.com/r/D31W3G/2

Není to dokonalé, ale jako řešení stačí
