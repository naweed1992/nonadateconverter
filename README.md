# nona date converter

## Name
Nona Date Converter

## Description
A library to convert gregorian, hijri and jalali calenders to each other.

## Installation
pip3 install nonadateconverter pip3 install git+https://github.com/naweed1992/nonadateconverter.git

## Usage
Methods and Functions:
1. nonadateconverter.hijri(Year, Month, day).hijri_to_gregorian()
Description: This function converts Hijri date to Gregorian date !
Example:
nonadateconverter.hijri(1444, 08, 07).hijri_to_gregorian()
out: (2023,02 ,28 ) #Gregorian,output type: tuple!
####
2. nonadateconverter.gregorian(Year, Month, day).gregorian_to_hijri()
Description: This function converts Gregorian date to Hijri date !
Example:
nonadateconverter.gregorian(2023,02 ,28 ).gregorian_to_hijri()
out: (1444, 08 , 07 ) #Hijri,output type: tuple!
####
3. nonadateconverter.jalali(Year, Month, day).jalali_to_hijri()
Description: This function converts Jalali date to Hijri date !
Example:
nonadateconverter.jalali(1401, 12, 09).jalali_to_hijri()
out: (1444, 08, 07) #Hijri,output type: tuple!
####
4. nonadateconverter.hijri(Year, Month, day).hijri_to_jalali()
Description: This function converts Hijri date to Jalali date !
Example:
nonadateconverter.hijri(1444, 08, 07).hijri_to_jalali()
out: (1401, 12, 09 ) #Jalali,output type: tuple!
####
5. nonadateconverter.gregorian(Year, Month, day).gregorian_to_jalali()
Description: This function converts Gregorian date to Jalali date !
Example:
nonadateconverter.gregorian(2023-02-28).gregorian_to_jalali()
out: (1401,12,09) #Jalali,output type: tuple!
####
6. nonadateconverter.jalali(Year, Month, day).jalali_to_gregorian()
Description: This function converts Jalali date to Gregorian date !
Example:
nonadateconverter.jalali(1401,12,09).jalali_to_gregorian()
out: (2023-02-28) #Gregorian,output type: tuple!
####
7. nonadateconverter.gregorian.now()
Description: This function shows current time in gregorian!
Example:
nonadateconverter.gregorian.now()
out: (2023,02 ,28 ) #Gregorian,output type: tuple!
####
8. nonadateconverter.jalali.now()
Description: This function shows current time in jalali!
Example:
nonadateconverter.jalali.now()
out: (1401,12 ,12 ) #Jalali,output type: tuple!
####
9. nonadateconverter.hijri.now()
Description: This function shows current time in hijri!
Example:
nonadateconverter.hijri.now()
out: (1444,08 ,10 ) #hijri,output type: tuple!
####
10. nonadateconverter.gregorian(year, month, day).weekday()
Description: This function shows the week day
Example:
nonadateconverter.gregorian(2023, 02 , 28).weekday()
out: Tuesday #output type: String
####
11. nonadateconverter.jalali(year, month, day).weekday()
Description: This function shows the week day
Example:
nonadateconverter.jalali(1401, 12 , 09).weekday()
out: Tuesday #output type: String
####
12. nonadateconverter.hijri(year, month, day).weekday()
Description: This function shows the week day
Example:
nonadateconverter.hijri(1444, 12 , 09).weekday()
out: Tuesday #output type: String
####
13. nonadateconverter.gregorian(year, month, day).elapsedtime()
Description: This function shows elapsed time from input date until now!
Example:
nonadateconverter.gregorian(2022, 02, 05).elapsedtime()
out: (1, 7, 7) #(year, month, day) ,output type: tuple!
####
14. nonadateconverter.jalali(year, month, day).elapsedtime()
Description: This function shows elapsed time from input date until now
Example:
nonadateconverter.jalali(1400, 02, 05).elapsedtime()
out: (1, 7, 7) #(year, month, day) ,output type: tuple!
####
15. nonadateconverter.hijri(year, month, day).elapsedtime()
Description: This function shows elapsed time from input date until now
Example:
nonadateconverter.hijri(1444, 02, 05).elapsedtime()
out: (1, 7, 7) #(year, month, day) ,output type: tuple!
## Support
email me on navid.nourazar@gmail.com

## Authors and acknowledgment
Thanks to Filoger which had impact on developing the project.

## License
open source

## Project status
Done
