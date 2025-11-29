---
title: "מה הקטע עם התפלגות נורמלית? (חלק ג': על תוחלת וסטיית תקן)"
layout: post
categories:
  - הסתברות
tags:
  - התפלגות נורמלית
image: "/assets/img/2025/histogram_12.png"
description: "מה זה תוחלת ושונות, איך קשורים מרקוב וצ'בישב, ועל הקסם שבהפיכת המתמטיקה למדע אמפירי"
---


<h2>מבוא</h2>

בסדרת הפוסטים הנוכחית אנחנו מנסים להבין למה ההתפלגות הנורמלית {% equation %}f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}{% endequation %} נראית כמו שהיא נראית. <a href="https://gadial.net/2025/02/03/normal_distribution_2/">בפוסט הקודם</a> הבנו מה הפונקציה הזו בכלל אומרת - זו <strong>פונקציית צפיפות ההסתברות</strong> של ההתפלגות הנורמלית, כלומר אם {% equation %}X{% endequation %} הוא המשתנה המקרי שמתואר על ידי הפונקציה הזו, אז {% equation %}P\left(a\le X\le b\right)=\int_{a}^{b}\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}dx{% endequation %}. בפוסט הקודם גם ראינו מאיפה ה-{% equation %}\pi{% endequation %} הגיע - זה קבוע נרמול שנדרש כדי שיתקיים {% equation %}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{x^{2}}{2}}=1{% endequation %}. אבל מה הם ה-{% equation %}\mu{% endequation %} וה-{% equation %}\sigma{% endequation %} שמופיעים בנוסחה? אלו שני פרמטרים שמאפיינים לא רק את ההתפלגות הזו, אלא כל התפלגות שהיא: <strong>התוחלת</strong> {% equation %}\mu{% endequation %} של ההתפלגות, <strong>וסטיית התקן</strong> {% equation %}\sigma{% endequation %} שלה. באופן לא פורמלי, תוחלת של התפלגות היא הממוצע שלה, וסטיית התקן מלמדת אותנו כמה גדול הפיזור של ההתפלגות סביב הממוצע הזה. מה שמפליא הוא כמה מידע על ההתפלגות נמצא כבר בשני הערכים המספריים הללו - וההמחשה לזה היא בדיוק <strong>משפט הגבול המרכזי</strong>, שאומר שאם אנחנו יודעים את התוחלת וסטיית התקן של התפלגות, אז נדע בדיוק איך נראה מה שמתקבל מסכומים גדולים של משתנים מקריים בלתי תלויים בעלי ההתפלגות הזו.

בואו נעבור להגדרות פורמליות, ונראה איך זה בא לידי ביטוי בהתפלגות נורמלית ובהתפלגויות אחרות שראינו.

<h2>תוחלת</h2>

מה זה "ממוצע"? אם למשל יש לנו את סדרת המספרים {% equation %}10,30,50,60,90{% endequation %} הממוצע שלה היא הסכום של כל המספרים חלקי כמה מספרים יש: {% equation %}\frac{10+30+50+60+90}{5}=\frac{240}{5}=48{% endequation %}. מה המשמעות של המספר הזה, 48? אפשר לחשוב על זה כך: אם נחליף כל איבר בסדרה ב-48, נקבל סדרה {% equation %}48,48,48,48,48{% endequation %} שסכום האיברים שלה שווה לסכום אברי הסדרה המקורית.

את הרעיון הזה אפשר להכליל קצת: אם למשל הסדרה שלנו היא {% equation %}30,60,60{% endequation %} אז הממוצע שלה הוא {% equation %}50{% endequation %}, אבל אפשר גם "לאחד" את שני ה-60-ים ולהגיד שיש בסדרה שלנו שני איברים: האיבר {% equation %}30{% endequation %} עם <strong>המשקל</strong> 1, והאיבר {% equation %}60{% endequation %} עם <strong>המשקל</strong> 2. מה שאנחנו עושים הוא לסכום את האיברים כשכל אחד מוכפל במשקל שלו, ולחלק בסכום הכולל של המשקלים. אולי קל יותר להבין את זה עם נוסחה: אם יש לנו את הסדרה {% equation %}a_{1},a_{2},\ldots,a_{n}{% endequation %} ואת המשקלים {% equation %}w_{1},\ldots,w_{n}{% endequation %} אז <strong>הממוצע המשוקלל</strong> הוא {% equation %}\frac{\sum_{i=1}^{n}w_{i}a_{i}}{\sum_{i=1}^{n}w_{i}}{% endequation %}. כאשר כל המשקלים הם 1 אנחנו מקבלים את הגדרת הממוצע הקודמת.

ההגדרה של ממוצע משוקלל לא דורשת שום דבר מהמשקלים, חוץ מכך שהסכום שלהם יהיה שונה מאפס (אחרת יקרה משהו מוזר כשמנסים לחלק) אבל כמובן, ההגדרה הזו יוצאת פשוטה במיוחד אם {% equation %}0\le w_{i}\le1{% endequation %} ובנוסף {% equation %}\sum_{i=1}^{n}w_{i}{% endequation %}; אנחנו מקבלים שהממוצע המשוקלל הוא פשוט {% equation %}\sum_{i=1}^{n}w_{i}a_{i}{% endequation %}.

איך כל זה קשור להסתברות? ובכן, הסתברות היא בדיוק המקרה שבו יש לנו איברים {% equation %}0\le w_{i}\le1{% endequation %} שמסתכמים ל-1: אם יש לנו מרחב הסתברות ו-{% equation %}X{% endequation %} הוא משתנה מקרי שמקבל מספר <strong>סופי</strong> של ערכים, נאמר הערכים {% equation %}a_{1},a_{2},\ldots,a_{n}{% endequation %}, אז אפשר להסתכל על הממוצע המשוקלל {% equation %}\sum_{i=1}^{n}P\left(X=a_{i}\right)\cdot a_{i}{% endequation %}. כלומר, אנחנו לוקחים את הממוצע המשוקלל של ה-{% equation %}a_{i}{% endequation %}-ים כשהמשקולות הן בדיוק ההסתברויות ש-{% equation %}a_{i}{% endequation %} יעלה בגורל. סכום כזה נקרא <strong>תוחלת</strong> ומסומן ב-{% equation %}E\left[X\right]{% endequation %}. אם מרחב המדגם הוא אינסופי העניינים מן הסתם מסתבכים קצת מתמטית אבל הרעיון זהה: {% equation %}\text{E}\left[X\right]=\sum_{i=1}^{\infty}P\left(X=a_{i}\right)\cdot a_{i}{% endequation %} עבור מרחב מדגם אינסופי בדיד, ו-{% equation %}\text{E}\left[X\right]=\int_{-\infty}^{\infty}p\left(x\right)xdx{% endequation %} עבור מרחב מדגם אינסופי רציף.

למה ממוצע משוקלל כזה הוא מעניין? אנחנו הרי מצפים שהוא ילמד אותנו משהו על המשתנה המקרי {% equation %}X{% endequation %} ולא סתם יהיה הגדרה לשם הגדרה. כאן זו אחת מהסיטואציות הנדירות שבהן המתמטיקה הייתה מדע <strong>אמפירי</strong>: קודם כל התגלתה תופעה, ואחר כך הוכיחו אותה מתמטית. התופעה הייתה האבחנה שאם אנחנו חוזרים על אותו ניסוי הסתברותי מספרי שוב ושוב, <strong>הממוצע</strong> של התוצאות שלנו נוטה להיות יציב יחסית ככל שמספר הניסויים שאנחנו מבצעים גדל. בואו נראה דוגמא קונקרטית לזה עם הטלת קוביה. בימינו, למרבה השמחה, אפשר לרתום את המחשב לניסויים כאלו, אז הנה קוד פייתון קצרצר: 
{% highlight python %}
import random
for N in [10, 100, 1000, 10000, 100000, 1000000]:
  print(f"{N}: {sum([random.randint(1, 6) for _ in range(N)]) / N}")
{% endhighlight %}

 מה שהקוד הזה עושה הוא להטיל קוביה מספר כלשהו של פעמים שמסומן ב-{% equation %}N{% endequation %}, ואז לחשב את ממוצע ההטלות. אנחנו עושים את הניסוי הזה בנפרד עבור ערכי {% equation %}N{% endequation %} מ-{% equation %}10{% endequation %} עד {% equation %}10^{6}{% endequation %}, ולכל אחד מהם אנחנו מדפיסים את הממוצע. כשאני עשיתי את זה, קיבלתי: 

{% highlight python %}
10: 3.1
100: 3.56
1000: 3.372
10000: 3.4951
100000: 3.50129
1000000: 3.499845 
{% endhighlight %}

 די בבירור, הממוצע מתקרב אל {% equation %}3.5{% endequation %}. זו אבחנה אמפירית; אבל אם אנחנו רוצים לדעת לאן הממוצע ישאף אנחנו <strong>לא צריכים</strong> לבצע ניסויים בפועל - אנחנו יכולים פשוט <strong>לחשב</strong> את זה, ואיכשהו מובטח שהמציאות תסתדר בהתאם לחישוב שלנו. הערך שאנחנו מחשבים הוא - הפתעה הפתעה - התוחלת של המשתנה המקרי שמתאר את הניסוי.

במקרה שלנו, {% equation %}X{% endequation %} מקבל כל ערך בין 1 ל-6 בהסתברות {% equation %}\frac{1}{6}{% endequation %} לכל איבר, אז על פי הגדרה {% equation %}E\left[X\right]=\frac{1+2+3+4+5+6}{6}=\frac{21}{6}=3.5{% endequation %}. אין פה הפתעה, אבל מה שכן יש פה הוא חישוב פשוט למדי, שלא מצריך הטלת מיליון קוביות. והיופי פה הוא שזה עובד <strong>תמיד</strong>, לכל משתנה מקרי {% equation %}X{% endequation %} שאנחנו משכפלים {% equation %}n{% endequation %} עותקים זהים שלו שהם בלתי תלויים אחד בשני ומסתכלים על הממוצע של כולם (טוב, <a href="https://gadial.net/2008/07/25/envelope_paradox/">כמעט תמיד</a>).

לתופעה הזו קוראים <strong>חוק המספרים הגדולים</strong>. יש כמה ניסוחים למשפט שאומר "מה הולך פה" והניסוח הנפוץ הוא בדרך כלל של מה שנקרא <strong>החוק החזק של המספרים הגדולים</strong> שלא אוכיח כרגע אבל כן אסביר מה הוא אומר. אנחנו מתחילים עם סדרה אינסופית של משתנים מקריים {% equation %}X_{1},X_{2},X_{3},\ldots{% endequation %} שכולם מתפלגים באותו האופן (כלומר, בעלי אותה פונקצית צפיפות הסתברות) והם בלתי תלויים, במובן הבא: {% equation %}X,Y{% endequation %} הם בלתי תלויים אם לכל שתי קבוצות אפשריות של תוצאות {% equation %}A,B{% endequation %} מתקיים {% equation %}P\left(X\in A\wedge Y\in B\right)=P\left(X\in A\right)P\left(Y\in B\right){% endequation %}; ראינו את זה טיפה בפוסט הקודם ולא אתעכב על זה הפעם.

עכשיו, מכיוון שכל המשתנים מתפלגים אותו דבר, יש להם אותה תוחלת. באופן כללי תוחלת עשויה להיות אינסופית או לא מוגדרת, אבל נניח שכאן היא מספר סופי, {% equation %}E\left[X_{i}\right]=\mu{% endequation %}. במקרה הזה אנחנו יכולים להסתכל על המשתנה המקרי {% equation %}\overline{X}_{n}=\frac{X_{1}+X_{2}\ldots+X_{n}}{n}{% endequation %}, שהוא המשתנה שמתאר את הממוצע (הרגיל, הלא משוקלל) של {% equation %}n{% endequation %} התוצאות הראשונות בסדרת המשתנים המקריים. החוק החזק של המספרים הגדולים אומר שמתקיים {% equation %}\overline{X}_{n}\to\mu{% endequation %} בהסתברות 1. בואו נבין טיפה יותר מה זה אומר בעצם.

ה-{% equation %}\overline{X}_{n}{% endequation %}-ים שהגדרנו מתארים <strong>סדרה</strong> של משתנים שמתארת את הממוצעים ההולכים-ומשתפרים: {% equation %}\overline{X}_{1},\overline{X}_{2},\overline{X}_{3},\ldots{% endequation %}. אם אנחנו דוגמים איבר {% equation %}a{% endequation %} כלשהו במרחב המדגם שלנו, הוא ייתן למשתנים {% equation %}X_{1},X_{2},\dots{% endequation %} ערכים קונקרטיים שהם מספרים ממשיים: {% equation %}X_{1}\left(a\right),X_{2}\left(a\right),\ldots{% endequation %}, ולכן גם בסדרת הממוצעים נקבל ערכים קונקרטיים {% equation %}\overline{X}_{1}\left(a\right),\overline{X}_{2}\left(a\right),\ldots{% endequation %}; כלומר, בהינתן שאנחנו מסתכלים על איבר קונקרטי של מרחב המדגם, קיבלנו סדרה "רגילה" של מספרים ממשיים. על סדרה "רגילה" של ממשיים אפשר לשאול האם היא מקיימת את התכונה {% equation %}\lim_{n\to\infty}\overline{X}_{n}\left(a\right)=\mu{% endequation %}, כלומר האם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|\overline{X}_{n}\left(a\right)-\mu\right|<\varepsilon{% endequation %}. לכל {% equation %}a{% endequation %} במרחב המדגם שלנו התשובה לשאלה הזו היא או "כן" או "לא". החוק החזק של המספרים הגדולים אומר שקבוצת כל ה-{% equation %}a{% endequation %}-ים שעבורה התשובה היא "לא" היא ממידה אפס (זה לא אומר שזה לא יכול לקרות; זה אומר שזה זניח).

אני לא אוכיח כאן את חוק המספרים הגדולים; אני בעיקר משתמש בו כדי לתת מוטיבציה לסיבה שבגללה מושג התוחלת קופץ לנו לפרצוף ודורש שנגדיר אותו. יש עוד שימושים דומים לתוחלת, כשהפשוט שבהם הוא כנראה <strong>אי שוויון מרקוב</strong>: אם {% equation %}X{% endequation %} הוא משתנה מקרי שמקבל רק ערכים אי-שליליים ו-{% equation %}a>0{% endequation %} כלשהו, אז

{% equation %}P\left(X\ge a\right)\le\frac{\text{E}\left[X\right]}{a}{% endequation %}

בניסוח שקול שקצת יותר מאפשר להבין מה הקטע אפשר להכניס את התוחלת לתוך אי השוויון:

{% equation %}P\left(X\ge a\cdot\text{E}\left[X\right]\right)\le\frac{1}{a}{% endequation %}

כלומר, זה נותן הערכה גסה לשאלה מה הסיכוי ש-{% equation %}X{% endequation %} יהיה גדול מפי 2 התוחלת שלו (פחות מחצי), מפי 3 התוחלת שלו (פחות משליש) וכו'. זו באמת הערכה גסה, אבל לעתים קרובות היא מספיקה כדי להוכיח את מה שרוצים לעשות באותו רגע ולכן, בנוסף לפשטות שלו, אי השוויון הזה הוא כלי שימושי מאוד.

ההוכחה של אי שוויון מרקוב מצחיקה בכמה שהיא פשוטה. אני מגדיר משתנה מקרי {% equation %}I{% endequation %} שהוא מה שנקרא <strong>אינדיקטור</strong>: משתנה מקרי שמקבל או 0 או 1, ולכן בעצם נותן "אינדיקציה" לכך שאירוע מסוים קרה או לא. במקרה שלנו:

{% equation %}I=\begin{cases} 1 & X\ge a\\ 0 & X<a \end{cases}{% endequation %}

התוחלת של אינדיקטור, ממש על פי ההגדרה, היא ההסתברות שהאירוע שנותן 1 קרה, כלומר {% equation %}E\left[I\right]=P\left(X\ge a\right){% endequation %}. עכשיו, שימו לב ש-{% equation %}I\le\frac{X}{a}{% endequation %} ותאמינו לי שאפשר פשוט לקחת תוחלת לשני האגפים ולהוציא את הקבוע החוצה, ונקבל

{% equation %}P\left(X\ge a\right)=E\left[I\right]=\frac{E\left[X\right]}{a}{% endequation %}

אתם כמובן לא אמורים להאמין לי שפשוט אפשר לעשות את זה, אבל אני לא אוכיח את זה הפעם. את הקטע עם "להוציא את הקבוע החוצה" אפשר להכליל - התוחלת מקיימת תכונה מועילה מאוד שנקראת <strong>לינאריות</strong>: אם {% equation %}X,Y{% endequation %} הם משתנים מקריים כלשהם (שיכולים להיות גם תלויים) ו-{% equation %}\alpha,\beta{% endequation %} הם קבועים מספריים, אז {% equation %}\text{E}\left[\alpha X+\beta Y\right]=\alpha\text{E}\left[X\right]+\beta\text{E}\left[Y\right]{% endequation %} (ואפשר להכליל את זה לסכום סופי כלשהו של משתנים מקריים).

הראיתי את המושג האבסטרקטי של תוחלת ואיזו דוגמא מסכנה עם הטלת קוביה, אבל זה לא מספיק, בואו נראה דוגמא קונקרטית - מה שנקרא <strong>התפלגות בינומית</strong>. בהתפלגות בינומית יש לנו ניסוי בסיסי שחוזר על עצמו עם הסתברות {% equation %}p{% endequation %} להצליח ו-{% equation %}q=1-p{% endequation %} להיכשל בכל פעם; כבר ראינו שאם חוזרים על הניסוי {% equation %}n{% endequation %} פעמים אז ההסתברות לקבל בדיוק {% equation %}k{% endequation %} הצלחות היא {% equation %}p\left(X=k\right)={n \choose k}p^{k}q^{n-k}{% endequation %}. לכן, התוחלת של המשתנה המקרי הזה היא

{% equation %}\text{E}\left[X\right]=\sum_{k=0}^{n}k{n \choose k}p^{k}q^{n-k}{% endequation %}

יש טריק מתמטי לא מסובך שמאפשר לחשב את הסכום הזה, אבל למרבה השמחה הוא עובד באופן קצת יותר כללי ויאפשר לחשב לא רק את {% equation %}\text{E}\left[X\right]{% endequation %} אלא גם את {% equation %}\text{E}\left[X^{t}\right]{% endequation %} לכל חזקה טבעית {% equation %}t{% endequation %}, וזה הולך לעזור לנו בקרוב (הערכים {% equation %}\text{E}\left[X^{t}\right]{% endequation %} נקראים <strong>המומנטים</strong> של המשתנה המקרי {% equation %}X{% endequation %} ויש להם חשיבות באופן כללי). הסכום במקרה הכללי יותר הזה הוא

{% equation %}\text{E}\left[X^{t}\right]=\sum_{k=0}^{n}k^{t}{n \choose k}p^{k}q^{n-k}{% endequation %}

כי הדרך היחידה שבה הערך {% equation %}k^{t}{% endequation %} יכול להתקבל על ידי המשתנה {% equation %}X^{t}{% endequation %} היא אם הערך {% equation %}k{% endequation %} יתקבל על ידי המשתנה {% equation %}X{% endequation %}, כלומר <strong>ההסתברות</strong> היא אותו דבר וכל מה שהשתנה הוא שמופיע בתחילת הסכום {% equation %}k^{t}{% endequation %} במקום סתם {% equation %}k{% endequation %}.

עכשיו, קודם כל שימו לב שאם {% equation %}k=0{% endequation %} האיבר שמתאים למקרה הזה הוא פשוט אפס, כלומר אפשר לכתוב

{% equation %}\text{E}\left[X^{t}\right]=\sum_{k=1}^{n}k^{t}{n \choose k}p^{k}q^{n-k}{% endequation %}

הטריק הוא עכשיו לפתוח את ההגדרה של {% equation %}{n \choose k}=\frac{n!}{k!\left(n-k\right)!}{% endequation %} ולקבל

{% equation %}k{n \choose k}=k\cdot\frac{n!}{k!\left(n-k\right)!}=n\frac{k}{k!}\cdot\frac{\left(n-1\right)!}{\left(n-k\right)!}=n\frac{\left(n-1\right)!}{\left(k-1\right)!\left(n-k\right)!}=n{n-1 \choose k-1}{% endequation %}

נציב את זה אצלנו ועל הדרך נוציא {% equation %}p{% endequation %} אחד החוצה כדי להקטין את החזקה של {% equation %}p{% endequation %} באחד:

{% equation %}\sum_{k=1}^{n}k^{t}{n \choose k}p^{k}q^{n-k}=np\sum_{k=1}^{n}k^{t-1}{n-1 \choose k-1}p^{k-1}q^{n-k}{% endequation %}

עכשיו נבצע החלפת משתנה {% equation %}i=k-1{% endequation %}. כלומר כש-{% equation %}k=1{% endequation %} אז {% equation %}i=0{% endequation %} ואילו כש-{% equation %}k=n{% endequation %} אז {% equation %}i=n-1{% endequation %}, ולכן

{% equation %}np\sum_{k=1}^{n}k^{t-1}{n-1 \choose k-1}p^{k-1}q^{n-k}=np\sum_{i=0}^{n-1}\left(i+1\right)^{t-1}{n-1 \choose i}p^{i}q^{n-i-1}{% endequation %}

עכשיו בואו נסתכל על הביטוי שקיבלנו בסכום:

{% equation %}\sum_{i=0}^{n-1}\left(i+1\right)^{t-1}{n-1 \choose i}p^{i}q^{n-i-1}{% endequation %}

חוץ מה-{% equation %}\left(i+1\right)^{t-1}{% endequation %} בהתחלה זה נראה בדיוק כמו סכום על ההסתברויות של משתנה בינומי אחר שאסמן {% equation %}Y{% endequation %}, עם {% equation %}n-1{% endequation %} נסיונות ואותן הסתברויות הצלחה וכישלון {% equation %}p,q{% endequation %}. ה-{% equation %}\left(i+1\right)^{t-1}{% endequation %} בתחילת הסכום נראה קצת מוזר אבל אם חושבים על זה, רואים שהסכום פשוט שווה אל {% equation %}\text{E}\left[\left(Y+1\right)^{t-1}\right]{% endequation %}. כלומר קיבלנו

{% equation %}\text{E}\left[X^{t}\right]=np\text{E}\left[\left(Y+1\right)^{t-1}\right]{% endequation %}

במקרה הבסיס שבו {% equation %}t=1{% endequation %} אז {% equation %}\left(Y+1\right)^{t-1}{% endequation %} הוא פשוט הקבוע 1 ולכן התוחלת שלו היא 1 ולכן קיבלנו

{% equation %}\text{E}\left[X\right]=np{% endequation %}

אבל עם הנוסחה נוכל לחשב בקלות גם את {% equation %}\text{E}\left[X^{2}\right]{% endequation %}, למשל. כי:

{% equation %}\text{E}\left[X^{2}\right]=np\text{E}\left[Y+1\right]=np\left(\text{E}\left[Y\right]+1\right)=np\left(\left(n-1\right)p+1\right){% endequation %}

כאן למשל השתמשתי בלינאריות של התוחלת. אבל למה בעצם {% equation %}\text{E}\left[X^{2}\right]{% endequation %} מעניין אותי? או, אנחנו בדיוק מגיעים אל זה.

<h2>שונות וסטיית תקן</h2>

ראינו זה עתה שאם {% equation %}X{% endequation %} הוא משתנה בינומי שמתאר ספירה של הצלחות בניסוי שחוזר על עצמו {% equation %}n{% endequation %} פעמים עם הסתברות הצלחה {% equation %}p{% endequation %} בכל פעם, אז התוחלת שלו היא {% equation %}np{% endequation %}. ראינו גם שהתוחלת של התוצאה בהטלת קובייה הוגנת היא {% equation %}3.5{% endequation %}. אז אם נבחר את הפרמטרים של {% equation %}X{% endequation %} להיות {% equation %}n=7,p=\frac{1}{2}{% endequation %} נקבל שהתוחלת של {% equation %}X{% endequation %} היא גם {% equation %}3.5{% endequation %}: התוחלת של "הטל מטבע הוגן 7 פעמים וספור כמה פעמים התקבל עץ" היא אותה תוחלת כמו של "הטל קוביה הוגנת ובדוק מה יצא". אבל אלו בבירור ניסויים שונים למדי זה מזה - בהטלת קוביה לכל תוצאה יש אותו סיכוי, ובניסוי הבינומי אין סימטריה כזו ויש גם ערכים כמו 0 ו-7 שלא יכולים לצוץ בהטלת קוביה. עוד משחק שאני יכול לעשות הוא לשחק "הטלת מטבע" עם מטבע שהערך של צד אחד שלו הוא 0 והערך של הצד השני שלו הוא 7: גם במקרה הזה נקבל תוחלת {% equation %}3.5{% endequation %}.

אם אני לוקח את שלושת הניסויים השונים הללו ועושה עליהם את מה שעשיתי בפוסט הראשון בסדרה, כלומר מצייר את העקומה של ההתפלגות הנורמלית שמקרבת את מה שמקבלים אם חוזרים על הניסוי 100 פעמים וסוכמים את התוצאות - זה מה שאני אקבל:

<img src="{{site.baseurl}}{{site.post_images}}/2025/histogram_12.png" alt=""/>

יש כאן שלוש עקומות נורמליות, שניסיתי לצבוע בצבעים שונים כדי להבדיל ביניהן (אבל אני לא בטוח אם הצבעים ייראו שונים לכל הקוראים). העקומה שמגיעה הכי גבוהה, שצבועה באדום, מתאימה למשתנה הבינומי; האמצעית, שצבועה בכחול, מתאימה למשתנה של הקוביה; והתחתונה, הירוקה, מתאימה למשתנה של המטבע עם הערכים 0 ו-7.

מה הסיבה להבדל? ככל שעקומה נורמלית היא יותר גבוהה, כך זה אומר שרוב ההסתברות שהיא מייצגת מתארת טווח קטן יחסית. המקרה הקיצוני ביותר הוא המשתנה המקרי שפשוט מחזיר {% equation %}3.5{% endequation %} תמיד, שיתואר על ידי קו אנכי בודד בדיוק ב-{% equation %}350{% endequation %}. הסיבה שהעקומה הירוקה, הנמוכה, היא כל כך "רחבה" היא שהניסוי שהיא מתארת הוא בעל רק שני ערכים, ששניהם במרחק לא זניח מהתוחלת עצמה ולכן כל אי-אחידות בתוצאות של ההגרלה (נניח, יתרון של 9 הטלות שנתנו 7 במקום 0) "מושך" את הסכום הכולל רחוק מהממוצע הצפוי. זו האינטואיציה, אבל אנחנו רוצים את המתמטיקה הקונקרטית - מדד מספרי שיאפשר לנו לתאר עד כמה סטייה מהתוחלת היא משהו נפוץ או נדיר.

אם {% equation %}X{% endequation %} הוא משתנה מקרי ו-{% equation %}\mu=\text{E}\left[X\right]{% endequation %} היא התוחלת שלו, אפשר להסתכל על משתנה מקרי חדש, {% equation %}Y=X-\mu{% endequation %}. זה המשתנה המקרי המקורי, רק שעכשיו הוא מנורמל כך שהתוחלת שלו תהיה 0. מכיוון שמה שמעניין אותנו הוא גודל ה"סטייה מהממוצע", והגודל הזה הוא פשוט {% equation %}\left|Y\right|{% endequation %}, אפשר לשאול את עצמנו <strong>מה הסטייה הממוצע מהממוצע</strong>, כלומר {% equation %}\text{E}\left[\left|Y\right|\right]{% endequation %}. זה אמנם מדד מתבקש למדי, אבל הוא פחות מועיל מאשר אפשר היה לקוות. פונקציית הערך המוחלט היא לא "נחמדה" מבחינה מתמטית - בפרט, היא לא גזירה ב-0. עניין אחר הוא שהיא מאותו סדר גודל כמו {% equation %}Y{% endequation %} ודווקא יש עניין בכך שנעבור אל "סדר הגודל הבא". זה מוביל אותנו להגדרה שאולי נראית פחות טבעית ממבט ראשון אבל היא שימושית בצורה בלתי נתפסת: {% equation %}\text{Var}\left(X\right)=\text{E}\left[Y^{2}\right]=\text{E}\left[\left(X-\mu\right)^{2}\right]{% endequation %} כאשר Var כאן הוא קיצור של Variance, <strong>שונות</strong>. העלאה בריבוע נותנת לנו את היתרונות שרצינו: היא משמשת בתור סוג של ערך מוחלט כי {% equation %}a^{2}{% endequation %} זה אותו דבר כמו {% equation %}\left|a\right|^{2}{% endequation %}; זה עובר לסדר הגודל השני (חשבו על העלאה בריבוע בתור העלאה של סדר הגודל; איך זה באמת חשוב, נראה אחר כך). וזו פונקציה נחמדה לעבודה מבחינה מתמטית.

דבר אחד שקל לראות הוא נוסחה אלטרנטיבית לתוחלת שמתקבלת מכך שפותחים במפורש את הביטוי, מה שאני אדגים במקרה של הסתברות בדידה:

{% equation %}\text{Var}\left(X\right)=\text{E}\left[\left(X-\mu\right)^{2}\right]=\sum_{a}p\left(X=a\right)\left(a-\mu\right)^{2}={% endequation %}

{% equation %}=\sum_{a}P\left(X=a\right)a^{2}-2\mu\sum_{a}P\left(X=a\right)a+\mu^{2}\sum_{a}P\left(X=a\right)={% endequation %}

{% equation %}=\text{E}\left[X^{2}\right]-2\mu\text{E}\left[X\right]+\mu^{2}=\text{E}\left[X^{2}\right]-2\mu^{2}+\mu^{2}=\text{E}\left[X^{2}\right]-\mu^{2}=\text{E}\left[X^{2}\right]-\text{E}\left[X\right]^{2}{% endequation %}

בואו נוודא שהבנו מה הולך פה. את הביטוי המקורי פיצלתי לשלושה סכומים על פי הפתיחה של הסוגריים {% equation %}\left(a-\mu\right)^{2}=a^{2}-2a\mu+\mu^{2}{% endequation %}. הסכום הראשון היה {% equation %}\sum_{a}P\left(X=a\right)a^{2}{% endequation %} שזו ממש ההגדרה הפורמלית של {% equation %}\text{E}\left[X^{2}\right]{% endequation %}. הסכום השני היה קבוע כפול {% equation %}\sum_{a}P\left(X=a\right)a{% endequation %} שזו ההגדרה הפורמלית של {% equation %}\text{E}\left[X\right]{% endequation %}, ואחרי שהשתמשתי בכך ש-{% equation %}\text{E}\left[X\right]=\mu{% endequation %} קיבלתי את הערך שרציתי. 

הנוסחה {% equation %}\text{Var}\left(X\right)=\text{E}\left[X^{2}\right]-\text{E}\left[X\right]^{2}{% endequation %} בהחלט נראית לי יפה ושימושית יותר מאשר {% equation %}\text{E}\left[\left(X-\mu\right)^{2}\right]{% endequation %}; היא מציגה את השונות בעזרת שני המומנטים הראשונים של {% equation %}X{% endequation %}, שיותר קל לחשב ישירות. עשיתי את זה קודם, בדוגמה למעלה, עבור התפלגות בינומית: קיבלנו ש-{% equation %}\text{E}\left[X\right]=np{% endequation %} ואילו {% equation %}\text{E}\left[X^{2}\right]=np\left(\left(n-1\right)p+1\right){% endequation %}, ולכן עכשיו אני אוכל לחשב בקלות את השונות של התפלגות בינומית:

{% equation %}\text{Var}\left(X\right)=np\left(\left(n-1\right)p+1\right)-\left(np\right)^{2}=np\left[\left(n-1\right)p+1-np\right]={% endequation %}

{% equation %}=np\left(np-p+1-np\right)=np\left(1-p\right)=npq{% endequation %}

ובסופו של דבר קיבלנו ביטוי פשוט ואלגנטי מאוד עבור השונות. עבור המשתנה הבינומי הקונקרטי שתיארתי למעלה, של ספירת העצים ב-7 הטלות של מטבע הוגן, הפרמטרים היו {% equation %}n=7,p=q=0.5{% endequation %} ולכן התוחלת היא {% equation %}\frac{7}{2}=3.5{% endequation %} כפי שכבר ראינו, והשונות היא {% equation %}\frac{7}{4}=1.75{% endequation %}.

עבור תוחלת ראיתי שמתקיימת תכונת <strong>לינאריות</strong> מועילה מאוד: {% equation %}\text{E}\left[\alpha X+\beta Y\right]=\alpha\text{E}\left[X\right]+\beta\text{E}\left[Y\right]{% endequation %}. עבור שונות אין לנו משהו עד כדי כך נוח, אבל עדיין יש לנו נוסחה מועילה: {% equation %}\text{Var}\left(\alpha X+\beta\right)=\alpha^{2}\text{Var}\left(X\right){% endequation %}. כלומר - חיבור של <strong>קבוע</strong> לא משפיע (חיבור של משתנה מקרי אחר מסבך את הכל), והכפלה בקבוע מכילה את השונות באותו קבוע בריבוע.

עכשיו, העובדה שהשונות כוללת העלאה בריבוע היא מצד אחד חיובית מהסיבות שציינתי, ומצד שני אנחנו עדיין רוצים לקבל מדד דומה שהוא "מסדר גודל אחד פחות" ובכל זאת מתנהג נחמד. דרך פשוטה לקבל את זה היא להגדיר {% equation %}\sigma=\sqrt{\text{Var}\left(X\right)}{% endequation %} - גם פונקציית השורש היא נחמדה יחסית, ומורידה את סדר הגודל. ה-{% equation %}\sigma{% endequation %} הזה חשוב מספיק כדי שיקבל שם בפני עצמו: <strong>סטיית התקן</strong> של {% equation %}X{% endequation %}, ולעתים קרובות יותר נוח פשוט לכתוב {% equation %}\sigma^{2}{% endequation %} בתור השונות של {% equation %}X{% endequation %} במקום {% equation %}\text{Var}\left(X\right){% endequation %}. את התוצאה שראינו לפני רגע אפשר לתאר גם בתור "אם כופלים את {% equation %}X{% endequation %} ב-{% equation %}\alpha{% endequation %} כופלים את סטיית התקן של {% equation %}X{% endequation %} ב-{% equation %}\alpha{% endequation %}".

בואו נראה עכשיו שימוש בשונות כדי לשפר את היכולת שלנו להבין את {% equation %}X{% endequation %} בעזרת מעין שדרוג של אי-שוויון מרקוב שלוקח גם את השונות בחשבון ונקרא <strong>אי-שוויון צ'בישב</strong>.

הרעיון הוא כזה. כזכור, אי-שוויון מרקוב מדבר על משתנה מקרי <strong>אי-שלילי</strong> {% equation %}X{% endequation %} ועבורו, לכל {% equation %}a>0{% endequation %} , הוא נותן

{% equation %}P\left(X\ge a\right)=\frac{E\left[X\right]}{a}{% endequation %}

עכשיו, אם {% equation %}X{% endequation %} הוא משתנה מקרי <strong>כלשהו</strong>, לאו דווקא אי שלילי, אז בואו ניזכר ש-{% equation %}\text{Var}\left(X\right){% endequation %} הוגדרה בתור התוחלת של משתנה מקרי שהוא <strong>כן</strong> אי-שלילי: {% equation %}\sigma^{2}=\text{Var}\left(X\right)=\text{E}\left[Z\right]{% endequation %} כאשר {% equation %}Z=\left(X-\mu\right)^{2}{% endequation %}. על ה-{% equation %}Z{% endequation %} הזה אני כן יכול להשתמש באי שוויון מרקוב; בואו נראה מה קורה אם אנחנו לוקחים {% equation %}k>0{% endequation %} כלשהו ומשתמשים במרקוב עם {% equation %}a=k^{2}{% endequation %}:

{% equation %}P\left(Z\ge a\right)\le\frac{\text{E}\left[Z\right]}{a}{% endequation %}

כלומר

{% equation %}P\left(\left(X-\mu\right)^{2}\ge k^{2}\right)\le\frac{\text{E}\left[\left(X-\mu\right)^{2}\right]}{k^{2}}=\frac{\sigma^{2}}{k^{2}}{% endequation %}

עכשיו, בואו נביט על {% equation %}\left(X-\mu\right)^{2}\ge k^{2}{% endequation %}. הדבר הזה קורה אם ורק אם {% equation %}\left|X-\mu\right|\ge k{% endequation %}, ולכן ההסתברות של שני אי השוויונים זהה, כלומר אני יכול לכתוב

{% equation %}P\left(\left|X-\mu\right|\ge k\right)\le\frac{\sigma^{2}}{k^{2}}{% endequation %}

זה אי-שוויון צ'בישב. כמו עם אי-שוויון מרקוב, לפעמים קל יותר להבין מה הוא אומר אם "מכניסים את סטיית התקן אל אי השוויון", כלומר אם אני מנסח אותו על ידי

{% equation %}P\left(\left|X-\mu\right|\ge k\sigma\right)\le\frac{1}{k^{2}}{% endequation %}

אם למשל נציב {% equation %}k=2{% endequation %} נקבל את הטענה הבאה: לכל משתנה מקרי {% equation %}X{% endequation %}, הסיכוי שהוא יקבל ערך שהמרחק שלו מהתוחלת של {% equation %}X{% endequation %} הוא יותר משתי סטיות תקן הוא {% equation %}\frac{1}{4}=25\%{% endequation %}. לי זה מרגיש כמו טענה כללית להפתיע, כי לא משנה בכלל כמה {% equation %}X{% endequation %} מורכב ומתוחכם - מרגע שחישבנו את התוחלת ואת סטיית התקן שלו, אנחנו יודעים בדיוק מה האיזור שבו 75\% מהערכים ש-{% equation %}X{% endequation %} נותן הולכים ליפול. יותר מכך - בגלל שבמכנה יש {% equation %}k^{2}{% endequation %} ולא {% equation %}k{% endequation %}, זה אומר לנו שהסיכוי של מישהו להיות במרחק של הרבה סטיות תקן צונח מהר - צונח באופן <strong>ריבוע</strong>. אם הסיכוי להיות במרחק 2 סטיות תקן היה 25\%, עבור 3 סטיות תקן הוא נופל אל {% equation %}\frac{1}{9}=11.111\ldots\%{% endequation %}, ועבור 4 סטיות תקן הוא כבר {% equation %}\frac{1}{16}=6.25\%{% endequation %} וכשנרצה להיות במרחק 10 סטיות תקן הסיכוי כבר יהיה {% equation %}\frac{1}{100}=1\%{% endequation %}, וכן הלאה. ככל שסטיית התקן של {% equation %}X{% endequation %} גדולה יותר כך האיזור שבו רוב הערכים שלו יכולים ליפול הוא רחב יותר, אבל אם נחלק את המרחב לאיזורים שהרוחב של כל אחד מהם הוא {% equation %}\sigma{% endequation %}, נדע בדיוק מה ההסתברות של איבר ליפול בכל אחד מהאיזורים הללו. זו המחשה חזקה מאוד לכוח שיש לשני מספרים בודדים {% equation %}\mu,\sigma{% endequation %} לתאר את {% equation %}X{% endequation %}.

<h2>חזרה אל ההתפלגות הנורמלית</h2>

עכשיו כשהכרנו את המושגים של תוחלת ושונות/סטיית תקן אפשר לחזור סוף סוף אל ההתפלגות הנורמלית. הגדרתי אותה בעזרת פונקציית צפיפות ההסתברות {% equation %}f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}{% endequation %}, ועכשיו אפשר לחזור למה שאמרתי בתחילת הפוסט אבל כשיש לנו את ההגדרות הרלוונטיות: ה-{% equation %}\mu{% endequation %} וה-{% equation %}\sigma{% endequation %} הללו הם בדיוק התוחלת וסטיית התקן של ההתפלגות הנורמלית ש-{% equation %}\mu,\sigma{% endequation %} הם הפרמטרים שלה. כלומר, אנחנו מגדירים משתנה מקרי {% equation %}N\left(\mu,\sigma\right){% endequation %} על ידי פונקציית הצפיפות {% equation %}f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}{% endequation %}, וכשנחשב את התוחלת וסטיית התקן שלו הנוסחאות יתנו לנו בדיוק {% equation %}\mu,\sigma{% endequation %}, וזה בדיוק מה שאני רוצה להראות עכשיו. דבר אחד שכדאי לשים אליו לב לפני כן הוא שאפשר להגדיר את ההתפלגות הנורמלית גם בלי להגדיר בכלל סטיית תקן: הרי {% equation %}\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}{% endequation %} ולכן אם היינו למשל בוחרים לסמן את השונות שאנחנו רוצים ב-{% equation %}\tau{% endequation %} אז היינו מקבלים שהתפלגות נורמלית עם תוחלת {% equation %}\mu{% endequation %} ושונות {% equation %}\tau{% endequation %} מתוארת על ידי {% equation %}f\left(x\right)=\frac{1}{\sqrt{2\pi\tau}}e^{-\left(x-\mu\right)^{2}/2\tau}{% endequation %}. הבחירה להשתמש ב-{% equation %}\sigma{% endequation %} היא עניין של קונבנציה (ומן העבר השני, אנשים גם כותבים לפעמים {% equation %}\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(\frac{x-\mu}{\sigma}\right)^{2}/2}{% endequation %} כדי שהנוסחה תכלול רק את {% equation %}\sigma{% endequation %} ולא את {% equation %}\sigma^{2}{% endequation %}).

ראשית, הנה טריק מועיל כדי למצוא תוחלת ושונות של דברים. כזכור, ראינו

{% equation %}\text{E}\left[\alpha X+\beta Y\right]=\alpha\text{E}\left[X\right]+\beta\text{E}\left[Y\right]{% endequation %}

{% equation %}\text{Var}\left(\alpha X+\beta\right)=\alpha^{2}\text{Var}\left(X\right){% endequation %}

אז באופן כללי, אם אנחנו רוצים למצוא תוחלת ושונות של משתנה {% equation %}X{% endequation %} אבל זה קשה לנו, אפשר לנסות להגדיר משתנה "מנורמל" {% equation %}Z=\frac{X-\mu}{\sigma}{% endequation %} ולקבל

{% equation %}\text{E}\left[X\right]=\sigma\text{E}\left[Z\right]+\mu{% endequation %}

{% equation %}\text{Var}\left(X\right)=\sigma^{2}\text{Var}\left(Z\right){% endequation %}

אני אשתמש בזה במקרה שלנו. נניח ש-{% equation %}X{% endequation %} הוא משתנה מקרי שמתפלג נורמלית עם פרמטרים {% equation %}\mu,\sigma{% endequation %}, כלומר {% equation %}f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(\frac{x-\mu}{\sigma}\right)^{2}/2}{% endequation %}. אם אני מגדיר את המשתנה החדש {% equation %}Z=\frac{X-\mu}{\sigma}{% endequation %} אני אקבל פונקציית צפיפות הסתברות {% equation %}f\left(z\right)=\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}{% endequation %}. כדי לראות את זה נשים לב לכך ש:

{% equation %}P\left(a\le Z\le b\right)=P\left(\sigma a+\mu\le X\le\sigma b+\mu\right)=\int_{\sigma a+\mu}^{\sigma b+\mu}\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(\frac{x-\mu}{\sigma}\right)^{2}/2}dx{% endequation %}

ועל האינטגרל הזה אפשר לבצע את החלפת המשתנים {% equation %}z=\frac{x-\mu}{\sigma}{% endequation %} שנותנת לנו {% equation %}dz=\frac{dx}{\sigma}{% endequation %}, כלומר מקבלים {% equation %}P\left(a\le Z\le b\right)=\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}{% endequation %}.

המסקנה? אם {% equation %}X{% endequation %} התפלג נורמלית עם פרמטרים {% equation %}\mu,\sigma{% endequation %} אז {% equation %}Z=\frac{X-\mu}{\sigma}{% endequation %} מתפלג נורמלית עם פרמטרים {% equation %}0,1{% endequation %}. עכשיו אני אוכיח ש-{% equation %}\text{E}\left[Z\right]=0{% endequation %} וש-{% equation %}\text{Var}\left(Z\right)=1{% endequation %} ואז אסיק ש-

{% equation %}\text{E}\left[X\right]=\sigma\text{E}\left[Z\right]+\mu=\mu{% endequation %}

{% equation %}\text{Var}\left(X\right)=\sigma^{2}\text{Var}\left(Z\right)=\sigma^{2}{% endequation %}

וזו הטענה הכללית שאני רוצה.

עכשיו, {% equation %}\text{E}\left[Z\right]{% endequation %} זה קל - זה יוצא 0 בגלל שפונקציית הצפיפות {% equation %}\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}{% endequation %} היא סימטרית ביחס ל-0 כי {% equation %}z^{2}{% endequation %} היא פונקציה סימטרית ביחס ל-0. זה הופך את האינטגרל שמחשבים עבור התוחלת לאינטגרל של פונקציה <strong>אנטיסימטרית</strong> בגלל ההכפלה ב-{% equation %}z{% endequation %}. הנה משהו פורמלי קצת יותר:

{% equation %}\text{E}\left[Z\right]=\int_{-\infty}^{\infty}z\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}=\lim_{a\to\infty}\int_{-a}^{a}z\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}={% endequation %}

{% equation %}=\frac{1}{\sqrt{2\pi}}\lim_{a\to\infty}\left.e^{-z^{2}/2}\right|_{-a}^{a}=\frac{1}{\sqrt{2\pi}}\lim_{a\to\infty}\left(e^{-a^{2}/2}-e^{-a^{2}/2}\right)={% endequation %}

{% equation %}\frac{1}{\sqrt{2\pi}}\lim_{a\to\infty}0=0{% endequation %}

המעבר מאינטגרל אינסופי בשני הכיוונים לגבול כש-{% equation %}a{% endequation %} שואף לאינסוף של אינטגרל מ-{% equation %}-a{% endequation %} אל {% equation %}a{% endequation %} הוא <strong>לא תקין</strong> באופן כללי אבל בפוסט הקודם כבר אמרנו שבמקרה הנוכחי זה תקין (אבל אפשר להסתדר גם אם עושים שני אינטגרלים, זה פשוט יוצא מסורבל יותר). אז זה מסיים עם התוחלת ומראה שכדי לחשב את השונות צריך פשוט לחשב את {% equation %}\text{E}\left[Z^{2}\right]{% endequation %}. זה יהיה טיפה יותר מסובך ויצריך טריק אינטגרציה סטנדרטי: <strong>אינטגרציה בחלקים</strong>. בואו ניזכר את הטריק הזה הולך.

עבור נגזרות, אחת מהנוסחאות החשובות ביותר היא מה יוצאת הגזירה של מכפלה של פונקציות: {% equation %}\left(uv\right)^{\prime}=u^{\prime}v+uv^{\prime}{% endequation %}. זו אחת מהנוסחאות הבודדות שצרובות בי עוד מהתיכון. עכשיו, אם מעבירים אגפים, מקבלים מן הסתם {% equation %}u^{\prime}v=\left(uv\right)^{\prime}-uv^{\prime}{% endequation %} ואם (ועכשיו אני עובר לקצת נפנוף ידיים) לוקחים אינטגרל לשני האגפים מקבלים {% equation %}\int u^{\prime}v=uv-\int uv^{\prime}{% endequation %}. לכן אם קשה לנו לבצע אינטגרציה לפונקציה שלנו, אנחנו בודקים אם יש דרך נוחה לפרק אותה למכפלה של שתי פונקציות שלאחת מהן (שאנחנו קוראים לה {% equation %}u^{\prime}{% endequation %}) כן קל לנו להוציא אינטגרל, את השניה (שאנחנו קוראים לה {% equation %}v{% endequation %}) קל לנו לגזור, ואז אנחנו מקווים שאחרי שנוציא אינטגרל לאחת ונגזרת לשניה, המכפלה של <strong>זה</strong> תהיה משהו שקל לנו למצוא לו אינטגרל. לפעמים זה נכשל קטסטרופלית ולפעמים, כמו עכשיו, זה עובד יופי. הרי 

{% equation %}\text{E}\left[Z^{2}\right]=\int_{-\infty}^{\infty}z^{2}\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}{% endequation %}

ולפני רגע, בחישוב התוחלת, ראינו שקל לנו להוציא את האינטגרל של {% equation %}u^{\prime}=z\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}{% endequation %} והאינטגרל יוצא {% equation %}u=\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}{% endequation %}, וכמובן שאת {% equation %}v=z{% endequation %} קל לגזור ולקבל {% equation %}v^{\prime}=1{% endequation %}. כמו כן {% equation %}uv{% endequation %} הולך לצאת בדיוק הביטוי לתוחלת שראינו לפני רגע שהאינטגרל שלו הוא 0, ו-{% equation %}uv^{\prime}{% endequation %} הולך לצאת בדיוק פונקציית הצפיפות המקורית שראינו כבר (בפוסט הקודם, ולא בקלות) שהאינטגרל שלה יוצא 1. זה מסיים (בנפנוף ידיים) את ההוכחה.

אז אם לסכם עוד סיכום ביניים: אנחנו מנסים להבין למה פונקציית הצפיפות של ההתפלגות הנורמלית נראית ככה: {% equation %}f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(x-\mu\right)^{2}/2\sigma^{2}}{% endequation %}. בינתיים הבנו ש-{% equation %}\pi{% endequation %} שם בתור קבוע נרמול שמגיע בבסיסו מכך ש-{% equation %}2\pi{% endequation %} הוא היקף מעגל היחידה; ואנחנו רואים עכשיו ש-{% equation %}\mu,\sigma{% endequation %} שמופיעים פה מבטיחים שהתוחלת וסטיית התקן של ההתפלגות יהיו {% equation %}\mu,\sigma{% endequation %}; אבל עדיין לא ברור לנו הדבר העיקרי - מה הקטע עם ה-{% equation %}e{% endequation %} הזה? למה הצורה של העקומה היא (עד כדי קבועים) {% equation %}e^{-x^{2}}{% endequation %}? אני לא רואה איך לענות לשאלה הזו בלי להגיע אל היעד שלנו: <strong>משפט הגבול המרכזי</strong>. את זה נעשה בפוסט הבא. 
