---
id: 2399
title: "נוסחת טאפר - הנוסחה שמציירת את עצמה"
date: 2013-03-28 01:14:08
layout: post
categories: 
  - משחקים וחידות מתמטיות
  - תכנות
tags: 
  - הפניה עצמית
social_media_share: true
---
בואו ניגש ללב העניין. התבוננו בנוסחה הבאה:

{% equation %}\frac{1}{2}&lt;\left\lfloor \mbox{mod}\left(\left\lfloor \frac{y}{17}\right\rfloor 2^{-17\left\lfloor x\right\rfloor -\mbox{mod}\left(\left\lfloor y\right\rfloor ,17\right)},2\right)\right\rfloor {% endequation %}

בלי פאניקה! הכל יוסבר.

ראשית, סימנים: {% equation %}\left\lfloor a\right\rfloor {% endequation %} מסמל את <strong>הערך השלם התחתון </strong>של המספר {% equation %}a{% endequation %}, שמוגדר להיות המספר השלם הגדול ביותר שקטן או שווה ל-{% equation %}a{% endequation %}. למשל, {% equation %}\left\lfloor \frac{5}{3}\right\rfloor =1{% endequation %} ואילו {% equation %}\left\lfloor 2\right\rfloor =2{% endequation %}. בנוסף, {% equation %}\mbox{mod}\left(a,n\right){% endequation %} מסמל את הערך שמתקבל כאשר לוקחים את המספר {% equation %}a{% endequation %}, מחלקים אותו ב-{% equation %}n{% endequation %} ולוקחים את השארית. למשל, {% equation %}\mbox{mod}\left(3.3,2\right)=1.3{% endequation %}. זה הכל.

המשוואה הזו מכילה שני משתנים - {% equation %}x,y{% endequation %}. שניהם יכולים לקבל כל ערך שהוא מספר ממשי. עכשיו משחקים את המשחק הבא: מסתכלים על המישור {% equation %}\mathbb{R}^{2}{% endequation %} שהוא אוסף כל הנקודות {% equation %}\left(x,y\right){% endequation %} שהן מספרים ממשיים. לכל נקודה {% equation %}\left(x,y\right){% endequation %} כזו, אם כאשר מציבים את {% equation %}x,y{% endequation %} בנוסחה אי השוויון שבה אכן מתקיים, צובעים את הנקודה {% equation %}\left(x,y\right){% endequation %} בצבע שחור; אם השוויון לא מתקיים, מותירים את הנקודה לבנה. כעת, אם נסתכל על התמונה שנקבל נראה שקיבלנו תמונה אינסופית שבה המוני נקודות פזורות פה ושם וקשה להבין מה קורה, אבל אם נצטמצם לריבוע קטן יחסית - באורך 17 וברוחב 105 - ונלך למקום המתאים, נראה את התמונה הבאה:

<strong><a href="{{site.baseurl}}{{site.post_images}}/2013/03/tupper.png"><img class="alignnone size-medium wp-image-2401" alt="tupper" src="{{site.baseurl}}{{site.post_images}}/2013/03/tupper.png" width="300" height="48" /></a></strong>

רגע, מה? זו תמונה של המשוואה שבעזרתה יצרנו את התמונה מלכתחילה! יש לנו כאן סוג של הפניה עצמית - משוואה שיודעת <strong>לצייר</strong> את עצמה. הזוי לחלוטין, ומתעלה אפילו על <a href="http://www.gadial.net/2009/05/10/godel_incompleteness_proof_sketch/">משפטי אי השלמות של גדל</a> ותוכניות המחשב <a href="http://www.gadial.net/2009/11/27/quine_and_recursion_theorem/">שיודעות להדפיס את הקוד של עצמן</a>!

טוב, לא בדיוק.

הנוסחה הזו, שתוארה לראשונה על ידי ג'ף טאפר ב<a href="http://www.dgp.toronto.edu/people/mooncake/papers/SIGGRAPH2001_Tupper.pdf">מאמר</a> מ-2001, היא קסם במלוא מובן המילה. בהתחלה היא יוצרת רושם מדהים לחלוטין, של משהו בלתי אפשרי לגמרי שהגיע משום מקום, וזו תחושה נפלאה; אחר כך, כשמתחילים לחשוב על זה, מתברר מהר מאוד שהנוסחה משיגה את האפקט הזה על ידי תעלול לא מסובך במיוחד. זה מקלקל למדי את תחושת הפלא הראשונית, אבל מצד שני ההבנה של האופן שבו הקסם מתבצע היא תענוג בפני עצמו. כמובן שאני ממליץ לכולכם לחשוב על העניין בעצמכם; לא צריך הרבה יותר מאשר את הנוסחה שלעיל. יש רק פריט מידע אחד שטרם נתתי לכם - <strong>היכן</strong> בעצם מתחילה אותה תמונה מופלאה בתוך המישור?

ובכן, התמונה מתרחשת בנקודות עם קואורדינטת {% equation %}x{% endequation %} בין 0 ל-105, דהיינו {% equation %}0\le x\le105{% endequation %}, וקואורדינטת {% equation %}y{% endequation %} בין {% equation %}k{% endequation %} ל-{% equation %}k+16{% endequation %}, כלומר {% equation %}k\le y\le k+16{% endequation %}. מיהו {% equation %}k{% endequation %}? ובכן, מספר גדול לאין שיעור, שמתואר כאן עם רווחים כדי שיהיה קריא ולא יחרוג מגבולות השורה:
<p dir="ltr"><strong>960 939 379 918 958 884 971 672 962 127 852 754 715 004 339 660 129 306 651 505 519 271 702 802 395 266 424 689 642 842 174 350 718 121 267 153 782 770 623 355 993 237 280 874 144 307 891 325 963 941 337 723 487 857 735 749 823 926 629 715 517 173 716 995 165 232 890 538 221 612 403 238 855 866 184 013 235 585 136 048 828 693 337 902 491 454 229 288 667 081 096 184 496 091 705 183 454 067 827 731 551 705 405 381 627 380 967 602 565 625 016 981 482 083 418 783 163 849 115 590 225 610 003 652 351 370 343 874 461 848 378 737 238 198 224 849 863 465 033 159 410 054 974 700 593 138 339 226 497 249 461 751 545 728 366 702 369 745 461 014 655 997 933 798 537 483 143 786 841 806 593 422 227 898 388 722 980 000 748 404 719</strong></p>
חלקכם כבר מנחשים, למראה המספר, שכאן בעצם מסתתרת החוכמה האמיתית - איכשהו הציור "מתחבא" בתוך המספר הזה. אבל איך?

לפני התשובה, הנה לכם משחק אינטראקטיבי - הזינו פנימה ערך של {% equation %}k{% endequation %} (אפשר עם רווחים) וקבלו את התמונה עבור {% equation %}0\le x\le105{% endequation %} ו-{% equation %}k\le y\le k+16{% endequation %}:

<script src="{{site.baseurl}}/assets/js/bigint.js" type="text/javascript"></script>
<script type="text/javascript">
var square_size = 4;
var get_and_draw = function(){
var t=document.getElementById('number');

var empty = new String;
k_string = t.value.replace(/\s/g, empty);
draw_from_k(str2bigInt(k_string,10,1,1));
}
var draw_from_k = function(k){
var c=document.getElementById('formula');
var ctx=c.getContext('2d');
ctx.clearRect ( 0 , 0 , c.width , c.height );
divInt_(k,17);
for (x=105; x>=0; x=x-1){
for (y=0; y<17; y++){
var bit = modInt(k,2);
if (bit == 1){
draw_pixel(x,y,ctx);
}
divInt_(k,2);
}
}
}

var draw_pixel = function(x,y, ctx){
ctx.fillRect(x*square_size, y*square_size, square_size, square_size);
}

var init = function() {
draw_from_k(ctx,k);
}
</script>

<canvas id="formula" style="border: 1px solid #000000;" width="424" height="68"></canvas>
<input id="number" type="text" /> <input onclick="get_and_draw()" type="button" value="ציירו!" />

כעת, הבה ונעבור להסבר של מה שקורה כאן. התעלול הוא פשוט מאוד - הנוסחה של טאפר היא נוסחה שמטרתה לפענח קידודים של תמונות מונוכרומטיות (בשחור-לבן). המספר {% equation %}k{% endequation %} מחזיק בתוכו את הקידוד של התמונה, והנוסחה מפענחת את הקידוד הזה ואומרת איפה לשים שחור ואיפה לשים לבן. בשל כך, הנוסחה מסוגלת להחזיר <strong>כל</strong> תמונה שרק נרצה, כל עוד נזין לה את המספר המתאים. לא מאמינים? נסו למשל את זה:
<p dir="ltr"><strong>485 848 307 199 443 192 292 484 775 523 195 446 750 165 771 267 770 474 169 193 207 700 51 005 067 907 907 541 020 178 059 194 196 266 956 625 065 918 178 608 930 545 615 357 634 623 847 182 313 037 176 237 950 246 743 833 022 219 851 353 244 464 297 196 422 052 599 618 366 926 759 595 937 669 170 337 031 986 392 318 882 323 798 450 346 890 393 645 210 909 095 498 636 458 859 695 483 157 512 356 430 020 530 323 399 745 167 547 408 250 078 493 473 637 808 923 733 333 196 160 087 525 223 963 972 079 179 702 470 428 441 062 803 798 996 831 022 016 431 226 755 561 007 151 709 067 404 979 608 249 899 531 206 486 163 294 240 248 539 016 274 762 746 088 450 590 994 298 169 153 574 985 192 777 454 048 087 559 586 719 989 59</strong></p>
ובכן, מה שטאפר עשה (בתור משהו שהוא בסך הכל קוריוז קצרצר בתוך מאמר רציני) היה לצייר את הנוסחה הזו, לחשב את הקידוד שמתאים לציור ולקבל את {% equation %}k{% endequation %} שלנו. לכן קשה לומר שהנוסחה "מציירת את עצמה" - נכון לומר שהיא מציירת <strong>הכל</strong>, ולכן בפרט גם את עצמה, אבל זה פחות מעניין מתוכניות שמדפיסות <strong>רק</strong> את הקוד של עצמן או ממשפטי אי השלמות של גדל. כמובן, זה פותח פתח לאתגר חדש - לכתוב נוסחה שתכיל את {% equation %}k{% endequation %} בצורה מפורשת וגם תצייר את עצמה, אבל זה יישאר כאתגר לקוראים בבית.

עדיין, איך הנוסחה מסוגלת לקחת מספר {% equation %}k{% endequation %}, שבכלל לא מופיע בתוכה באופן מפורש, לפענח אותו ולצייר תמונה? לשם כך צריך להבין מה בעצם הנוסחה עושה. בואו נסתכל שוב על החלק המרכזי בה:

{% equation %}\left\lfloor \mbox{mod}\left(\left\lfloor \frac{y}{17}\right\rfloor 2^{-17\left\lfloor x\right\rfloor -\mbox{mod}\left(\left\lfloor y\right\rfloor ,17\right)},2\right)\right\rfloor {% endequation %}

נתחיל עם {% equation %}\left\lfloor \frac{y}{17}\right\rfloor {% endequation %}. בהנחה ש-{% equation %}k{% endequation %} מתחלק ב-17 (והוא מתחלק - בדקו זאת!) הרי שלכל ערך {% equation %}k\le y\le k+16{% endequation %} נקבל ש-{% equation %}\left\lfloor \frac{y}{17}\right\rfloor =\frac{k}{17}{% endequation %} (הסבירו לעצמכם למה). כלומר, ה-{% equation %}\left\lfloor \frac{y}{17}\right\rfloor {% endequation %} הוא פשוט דרך מחוכמת להכניס את {% equation %}k{% endequation %} לנוסחה בלי לכתוב אותו במפורש; ולמעשה, לא {% equation %}k{% endequation %} הוא מה שמקודד את התמונה אלא {% equation %}\frac{k}{17}{% endequation %} (מבחינה פילוסופית אפשר לטעון ששני המספרים הללו מקודדים את התמונה, אבל תכף נראה שיותר נכון לומר זאת על {% equation %}\frac{k}{17}{% endequation %}). כדי לפשט לעצמי את החיים אסמן מעתה {% equation %}a=\frac{k}{17}{% endequation %}.

עכשיו אנחנו כופלים את {% equation %}a{% endequation %} ב-2 בחזקת מינוס משהו מפלצתי. עזבו לבינתיים את המשהו המפלצתי - נסמן אותו ב-{% equation %}t{% endequation %}. מהו {% equation %}a2^{-t}{% endequation %}? זה סימון אחר ל-{% equation %}\frac{a}{2^{t}}{% endequation %}, כלומר אנחנו מחלקים את {% equation %}a{% endequation %} בחזקה גדולה של 2. הדבר הזה שקול ל<strong>הזזה של הספרות</strong> של {% equation %}a{% endequation %} בייצוג בינארי, או בנקודת מבט אחרת - הזזה של <strong>מיקום הנקודה העשרונית</strong> בייצוג בינארי של {% equation %}a{% endequation %}.

הרבה יותר קל להבין את זה אם חושבים על מספרים בבסיס 10 כפי שאנחנו רגילים. הביטו לרגע במספר {% equation %}a=531{% endequation %}. מספר חביב וטוב לב ואהוב על הבריות. כעת נתעלל בו ונחלק אותו ב-10, וזה כואב, כי הוא לא מתחלק ב-10. מה שנקבל הוא את המספר {% equation %}53.1{% endequation %}, שזה כמו {% equation %}513.{% endequation %}, רק אחרי שהנקודה זזה צעד אחד שמאלה. ואם נחלק ב-{% equation %}10^{2}{% endequation %} כלומר ב-100 נקבל {% equation %}5.31{% endequation %}, כלומר הנקודה זזה שני צעדים שמאלה. באופן כללי אם מחלקים מספר ב-{% equation %}10^{t}{% endequation %} , מה שיקרה הוא שהנקודה בייצוג העשרוני שלו תזוז {% equation %}t{% endequation %} צעדים שמאלה. כעת, אם נחלק מספר ב-{% equation %}2^{t}{% endequation %}, הנקודה תזוז {% equation %}t{% endequation %} צעדים שמאלה בייצוג של המספר בבסיס 2. כך למשל המספר 13 מיוצג בבסיס 2 בתור {% equation %}1101{% endequation %} (כי {% equation %}13=1\cdot2^{0}+0\cdot2^{1}+1\cdot2^{2}+1\cdot2^{3}{% endequation %}). אם נחלק אותו ב-{% equation %}4=2^{2}{% endequation %} נקבל את המספר "שלוש ורבע", שבבסיס בינארי הוא {% equation %}11.01{% endequation %} (כי {% equation %}11{% endequation %} בבינארי זה 3 ו-{% equation %}.01=0\cdot\frac{1}{2}+1\cdot\frac{1}{4}{% endequation %}).

יפה, אם כן, הנוסחה מבצעת חישוב שאסמן את התוצאה שלו בתור {% equation %}b=a2^{-t}{% endequation %}, שבסך הכל לוקחת את {% equation %}a{% endequation %} ומזיזה את הנקודה בייצוג הבינארי שלו {% equation %}t{% endequation %} צעדים שמאלה. אז מבצעים את החישוב הבא: {% equation %}\left\lfloor \mbox{mod}\left(b,2\right)\right\rfloor {% endequation %}. כלומר, גם לוקחים את {% equation %}b{% endequation %} מודולו 2, וגם לוקחים ערך שלם תחתון. גם על שתי הפעולות הללו כדאי לחשוב במונחים של הייצוג הבינארי של המספר. ביצוע הפעולה {% equation %}\mbox{mod}\left(b,2\right){% endequation %} לוקח את {% equation %}b{% endequation %} ופשוט זורק לזבל את כל הספרות ש<strong>משמאל </strong>לנקודה העשרונית, <strong>חוץ מאשר </strong>את הספרה הראשונה שמשמאל לה. כלומר, {% equation %}\mbox{mod}\left(101101.1101,2\right)=1.1101{% endequation %}. למה זה נכון? ובכן, את {% equation %}101101.1101{% endequation %} אפשר לכתוב גם כסכום שני מספרים: {% equation %}101101.1101=101100+1.1101{% endequation %}. המספר השמאלי מתחלק ב-2 והמספר הימני קטן מ-2. זה מספיק כדי לראות את נכונות הטענה גם באופן כללי, אבל אשאיר לכם להשלים את הפרטים.

כעת, מה עושה הערך השלם התחתון למספר? פשוט מאוד - מחסל את כל הספרות ש<strong>מימין</strong> לנקודה העשרונית. למה? כי זה החלק השברי של המספר, וזה בדיוק מה שנפטרים ממנו כשלוקחים ערך שלם תחתון.

במילים אחרות, {% equation %}\left\lfloor \mbox{mod}\left(b,2\right)\right\rfloor {% endequation %} לוקחת את המספר {% equation %}b{% endequation %} ומחזירה ספרה בודדת מתוך {% equation %}b{% endequation %} - בדיוק את זו שנמצאת מייד משמאל לנקודה העשרונית בייצוג של {% equation %}b{% endequation %} בבסיס בינארי. מסקנה: {% equation %}\left\lfloor \mbox{mod}\left(a2^{-t},2\right)\right\rfloor {% endequation %} היא פונקציה שלוקחת את {% equation %}a{% endequation %} ומחזירה בדיוק את הספרה במקום ה-{% equation %}t{% endequation %}-י בייצוג הבינארי של {% equation %}a{% endequation %} (כשמתחילים את הספירה של המקומות מ-0). עד כדי כך פשוט.

כעת נותר רק להבין מהו {% equation %}t{% endequation %}. ובכן, {% equation %}t=17\left\lfloor x\right\rfloor +\mbox{mod}\left(\left\lfloor y\right\rfloor ,17\right){% endequation %}. בואו ננסה להבין את זה.

ראשית {% equation %}\left\lfloor x\right\rfloor {% endequation %} ו-{% equation %}\left\lfloor y\right\rfloor {% endequation %} פירושם שלמרות שהנוסחה יכולה לקבל ערכים ממשיים כלשהם של {% equation %}x,y{% endequation %}, היא מתעניינת רק בערכים השלמים שלהם; הנקודות {% equation %}\left(3.5,2.7\right){% endequation %} ו-{% equation %}\left(3,2\right){% endequation %} יהיו צבועות באותו הצבע, ולמעשה אם {% equation %}\left(3,2\right){% endequation %} צבועה בשחור, כך גם כל נקודה אחרת מהצורה {% equation %}\left(3.a,2.b\right){% endequation %} עבור מספרים כלשהם {% equation %}a,b{% endequation %}. נשאר רק להבין את {% equation %}17\left\lfloor x\right\rfloor +\mbox{mod}\left(\left\lfloor y\right\rfloor ,17\right){% endequation %}.

הנוסחה הזו בוודאי מוכרת לכל מי שקצת תכנת בחייו והתעסק עם מערכים דו ממדיים. בקצרה, <strong>מערך</strong> הוא אוסף תאי זכרון רצופים במחשב, שלכל אחד יש אינדקס (שמתחיל במקרה שלנו מ-0). אם {% equation %}A{% endequation %} הוא מערך, אז {% equation %}A\left[4\right]{% endequation %} מסמן את התא החמישי במערך (מתחילים מאפס!) וכן הלאה. כעת, מערך דו ממדי הוא מערך שבו לכל תא יש שתי קואורדינטות, למשל {% equation %}A\left[3\right]\left[5\right]{% endequation %} מסמן את התא בעמודה מס' 3 ושורה מס' 5 (למתמטיקאים שביניכם, זו פשוט מטריצה בעוד שמערך הוא וקטור, אם כי במטריצות נהוג לתת את אינדקס השורה קודם וכאן עשיתי ההפך כדי להתאים לנוסחה של טאפר).

כעת, מערכים דו ממדיים מאוחסנים בזכרון של המחשב בתור מערכים רגילים, חד ממדיים; כאשר התוכנית נתקלת בגישה למערך מהצורה {% equation %}A\left[3\right]\left[4\right]{% endequation %} היא מתרגמת את הפניה הזו לכתובת במערך החד ממדי המקורי. איך עושים את זה? ובכן, הרעיון הוא לאחסן את המערך הדו-ממדי "עמודה עמודה". נניח שאורך כל עמודה במערך הדו-ממדי היא {% equation %}6{% endequation %}, אז עמודה מס' 0 אוחסנה בתאי הזכרון 0-5; עמודה מס' 1 בתאי הזכרון 6-11; עמודה 2 ב-12-17, ועמודה 3 ב-18-23, כאשר תא מס' 4 בעמודה (כלומר, התא בשורה 4) הוא התא הרביעי מביניהם, דהיינו 22. כעת, את החישוב שעשינו אפשר לתאר בתור {% equation %}22=3\cdot6+4{% endequation %}, ובאופן כללי אם אורך כל עמודה במערך הוא {% equation %}s{% endequation %} ואנחנו רוצים לגשת לתא {% equation %}A\left[x\right]\left[y\right]{% endequation %}, אז ניגש אל התא {% equation %}x\cdot s+y{% endequation %}.

נחזור אל {% equation %}t=17\left\lfloor x\right\rfloor +\mbox{mod}\left(\left\lfloor y\right\rfloor ,17\right){% endequation %}. כאן הנוסחה היא אותו הדבר: ספציפית, {% equation %}s=17{% endequation %}, כלומר במערך שלנו אורך כל עמודה הוא 17 (זהו <strong>גובה</strong> התמונה). כמו כן {% equation %}\mbox{mod}\left(\left\lfloor y\right\rfloor ,17\right){% endequation %} בעצם בא לנטרל את {% equation %}k{% endequation %} מתוך {% equation %}y{% endequation %}: הרי אמרנו ש-{% equation %}k\le y\le k+16{% endequation %}, כלומר אפשר לכתוב {% equation %}y=k+y^{\prime}{% endequation %} כאשר {% equation %}0\le y^{\prime}\le16{% endequation %}; אז {% equation %}y^{\prime}=\mbox{mod}\left(\left\lfloor y\right\rfloor ,17\right){% endequation %}.

כעת הכל ברור - אני מקווה! מה שקורה הוא ש-{% equation %}a{% endequation %} (שהוא, כזכור {% equation %}\frac{k}{17}{% endequation %}) הוא <strong>מערך דו ממדי של ביטים שמקודד כמערך חד ממדי</strong>. ה"קידוד" הוא בדיוק הייצוג הבינארי של {% equation %}a{% endequation %}, ומה שנוסחת טאפר עושה הוא לדגום אותו ביט-ביט. הביטים שנוסחת טאפר קוראת יהיו 0 או 1, ולכן השוואה לחצי תצליח רק כשהביט הוא 1.

אלו מכם שיסתכלו על הקוד שמייצר את התמונות מתוך המספרים למעלה יראו שזה מה שאני עושה - לוקח את המספר, מחלק ב-17 ואז אוכל אותו ביט ביט ומחליט על פי מה לצייר. המימוש הוא פשוט ביותר (אם כי נדרשת ספריה למספרים גדולים) וכל העסק הוא פשוט למדי אחרי שחושבים עליו קצת.

כל זה לא מפחית, לטעמי, מתחושת הפליאה הראשונית, ומכמה שההתעסקות בנוסחה הזו כיפית. והנה מה שיש לשחר אבן-דר מנדל <strong></strong> לומר על זה:
<a href="{{site.baseurl}}{{site.post_images}}/2013/03/tupper_shachar.jpg"><img src="{{site.baseurl}}{{site.post_images}}/2013/03/tupper_shachar.jpg" alt="tupper_shachar" width="480" height="324" class="alignnone size-full wp-image-2406" /></a>
