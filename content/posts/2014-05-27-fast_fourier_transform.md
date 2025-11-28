---
id: 3106
title: "התמרת פורייה המהירה"
date: 2014-05-27 19:10:00
layout: post
categories: 
  - אנליזה מתמטית
  - מבני נתונים ואלגוריתמים
tags: 
  - התמרת פורייה המהירה
---
בפוסט הקודם הצגתי את התמרת פורייה הבדידה, והבאתי דוגמה אחת לשימוש בה - כפל מהיר של פולינומים. אמרתי גם שכדי שהכפל באמת יהיה מהיר, עלינו לדעת לבצע את התמרת פורייה מהר; ואמרתי גם שהתמרת פורייה הבדידה מיוחדת בכך שהיא עוסקת בכמות סופית של מידע, ולכן אפשר לתכנת אותה במחשב בצורה פשוטה. כפי שאתם ודאי מנחשים מכל זה, הפוסט הנוכחי יהיה הרבה יותר מוטה לכיוון של מדעי המחשב מאשר הפוסטים הקודמים על פורייה; בפרט, אני הולך לדבר על שאלות של <strong>סיבוכיות </strong>ולהציג <strong>אלגוריתמים</strong>.

אבל ראשית, בואו ניזכר מהי התמרת פורייה הבדידה. אני הולך להשתמש בפוסט הזה בסימונים קצת שונים מאלו שהשתמשתי בהם בפוסט הקודם, כי הסימונים הישנים יהיו פחות נוחים לי. על כן אני ממליץ לאלו מכם שקראו את הפוסט הקודם לשכוח מהכל ולהתחיל מחדש. בכל הנוגע לסימונים, זאת אומרת.

אנחנו מסמנים את <strong>שורש היחידה הפרמיטיבי ה-{% equation %}n{% endequation %}-י</strong> בסימון {% equation %}\omega_{n}=e^{\frac{2\pi i}{n}}{% endequation %}, והחזקות שלו {% equation %}\left(\omega_{n}^{0},\omega_{n}^{1},\dots,\omega_{n}^{n-1}\right){% endequation %} הן כל {% equation %}n{% endequation %} שורשי היחידה מסדר {% equation %}n{% endequation %}. הקלט להתמרת פורייה הבדידה היא סדרה {% equation %}\left(a_{0},a_{1},\dots,a_{n-1}\right){% endequation %} של {% equation %}n{% endequation %} מספרים מרוכבים (האינדקס מתחיל מ-0 כי אנחנו במדעי המחשב, כמובן) והפלט הוא סדרה {% equation %}\left(b_{0},b_{1},\dots,b_{n-1}\right){% endequation %} של סדרה של מספרים מרוכבים, כך שמתקיים הקשר הבא בין הסדרות, לכל {% equation %}0\le k&lt;n{% endequation %}:

{% equation %}b_{k}=\sum_{t=0}^{n-1}a_{t}\omega_{n}^{-kt}{% endequation %} (<strong>משוואת אנליזה</strong>)

{% equation %}a_{k}=\frac{1}{n}\sum_{t=0}^{n-1}b_{t}\omega_{n}^{kt}{% endequation %} (<strong>משוואת סינתזה</strong>)

למעשה, בפוסט הקודם המשוואות נראו טיפה אחרת (ה-{% equation %}\frac{1}{n}{% endequation %} הופיע במשוואת האנליזה דווקא) אבל ההבדל אינו מהותי ומעכשיו המשוואות שיעניינו אותי הן אלו שהצגתי כאן.

במבט ראשון, לא נראה שיש בכלל צורך באלגוריתם כלשהו - המשוואות שמאפשרות לנו לחשב את {% equation %}b_{k}{% endequation %} לכל {% equation %}k{% endequation %} הן פשוטות מאוד. פשוט כופלים שורשי יחידה ב-{% equation %}a_{t}{% endequation %}-ים ומחברים. מה הסיפור? ובכן, פשוט מאוד: יש {% equation %}n{% endequation %} איברים {% equation %}b_{t}{% endequation %} שאנחנו רוצים לחשב, ולכל אחד מהם נצטרך לבצע {% equation %}n{% endequation %} פעולות של כפל ו-{% equation %}n{% endequation %} פעולות של חיבור. סה"כ {% equation %}\Theta\left(n^{2}\right){% endequation %} פעולות. זה לא המון, אבל זה גם לא מעט. אם {% equation %}n=1000{% endequation %} זה אומר שנזדקק למיליון פעולות בערך.

מה שאנחנו <strong>רוצים</strong> הוא אלגוריתם שמבצע את כל המהומה הזו עם {% equation %}\Theta\left(n\log n\right){% endequation %} פעולות, כלומר כאשר {% equation %}n=1000{% endequation %} הוא מבצע בערך 7,000 פעולות - ההבדל בין זה ובין מיליון הוא די ברור. להשוואת זמני ריצה בפועל במימושים אמיתיים נגיע בסוף, אבל בינתיים תאמינו לי שזה הבדל גדול.

האלגוריתם שאציג לא יהיה סוף דבר - הוא יהיה שיטה נאיבית יחסית להתמודדות עם הבעיה. זה אומר שיש שיטות מורכבות יותר שאני לא מציג, והוא גם יניח הנחה מוזרה - ש-{% equation %}n{% endequation %} הוא חזקה של 2. עם זאת, הוא ישיג לנו את זמן ה-{% equation %}\Theta\left(n\log n\right){% endequation %} המובטח ויתן תחושה של "איך עושים את הקסם הזה", שזה מה שאני מחפש.

לפני שנצלול לפרטים, הנה הרעיון, וזה רעיון פשוט מאוד. ראשית, בואו נשים לב שאת משוואות האנליזה ניתן לתאר בתור <strong>הצבה של שורשי יחידה בפולינום</strong>. נגדיר את הפולינום {% equation %}A\left(x\right)=\sum_{t=0}^{n-1}a_{t}x^{t}{% endequation %}. כעת נשים לב לכך ש-{% equation %}b_{k}=A\left(\omega_{n}^{-k}\right){% endequation %}. אז אפשר לשאול את השאלה הכללית: בהינתן פולינום {% equation %}A{% endequation %} עם {% equation %}n{% endequation %} מקדמים ו-{% equation %}n{% endequation %} נקודות {% equation %}x_{0},\dots,x_{n-1}{% endequation %}, האם ניתן למצוא את {% equation %}y_{0},\dots,y_{n-1}{% endequation %} המוגדרים על ידי {% equation %}y_{k}=A\left(x_{k}\right){% endequation %} ב-{% equation %}\Theta\left(n\log n\right){% endequation %} פעולות במקום ב-{% equation %}\Theta\left(n^{2}\right){% endequation %}?

זו שאלה טובה, ולמיטב ידיעתי התשובה היא <strong>לא </strong>(אבל אני לא מומחה ואין לי הוכחה כרגע). כלומר, אם אני מנסה לחשב את הערכים של {% equation %}A{% endequation %} בנקודות <strong>שרירותיות כלשהן</strong>, אין לי דרך חכמה לעשות את זה. הקסם של התמרת פורייה המהירה הוא שבמקרה <strong>הספציפי</strong> של שורשי היחידה, דווקא כן אפשר לעשות קיצורי דרך בחישובים. זה אומר שהאלגוריתם יצטרך להסתמך איכשהו על תכונות מיוחדות שיש לשורשי היחידה ולסתם מספרים שרירותיים אין.

הרעיון הבסיסי באלגוריתם הוא פשוט מאוד: <strong>הפרד ומשול</strong>. הדוגמה הקלאסית שצריכה להיות לכם בראש היא זו של <a href="http://www.gadial.net/2012/07/10/all_sorts_of_slow_sorts/">אלגוריתם מיון-מיזוג</a>: הרעיון באלגוריתם המיון הזה הוא לקחת את הרשימה שממיינים, לפצל אותה לשניים, למיין כל תת-רשימה באופן רקורסיבי, ואז למזג את שתי הרשימות הממויינות שהתקבלו, תוך ניצול העובדה ש<strong>קל יחסית</strong> למזג שתי רשימות ממויינות.

גם כן אנחנו הולכים לקחת את הסדרה שאנחנו רוצים לבצע לה התמרה, לפצל אותה לשתי תת-סדרות, למצוא התמרה לכל אחת בנפרד ואז "למזג" את שתי ההתמרות להתמרה אחת, יחסית ביעילות. ברמה הטכנית זה מתבצע בעזרת הפולינום {% equation %}A{% endequation %} שתיארתי: אנחנו מפרקים את {% equation %}A{% endequation %} לשני תת-פולינומים {% equation %}A^{0},A^{1}{% endequation %}, ובמקום לחשב את הערך של {% equation %}A{% endequation %} על שורשי היחידה מסדר {% equation %}n{% endequation %}, אנחנו מחשבים את הערכים של שני תתי-הפולינומים על שורשי היחידה מסדר {% equation %}\frac{n}{2}{% endequation %}. את הערכים הללו אנחנו יכולים "למזג" אחר כך ולקבל את הערכים של {% equation %}A{% endequation %} על שורשי היחידה מסדר {% equation %}n{% endequation %}. זה כל הסיפור; רק צריך להבין איך מתבצע שלב ה"מיזוג" במקרה הנוכחי. רק שימו לב לכך שראינו מדוע הכרחי להניח ש-{% equation %}n{% endequation %} הוא חזקה של 2: אנחנו חייבים ש-{% equation %}n{% endequation %} יתחלק ב-2 כדי הפירוק לשני תתי-פולינומים יעבוד ללא בעיות, ומכיוון שאנו פותרים באופן רקורסיבי גם {% equation %}\frac{n}{2}{% endequation %} יצטרך לקיים את התכונה הזו וכן הלאה (עד למקרה של {% equation %}n=1{% endequation %} שהוא טריוויאלי - ההתמרה של סדרה מאורך 1 הוא הסדרה עצמה).

כלי הנשק המתמטי הבסיסי שלנו כאן הוא התכונה הבאה של שורשי היחידה מסדר {% equation %}n{% endequation %}, כאשר {% equation %}n{% endequation %} הוא מספר זוגי: אם נעלה את כל שורשי היחידה מסדר {% equation %}n{% endequation %} בריבוע, נקבל את כל שורשי היחידה מסדר {% equation %}\frac{n}{2}{% endequation %}, כאשר כל שורש יחידה שכזה מתקבל בדיוק פעמיים. הנה דוגמה קלה: שורשי היחידה מסדר 4 הם המספרים {% equation %}1,i,-1,-i{% endequation %}. אם נעלה אותם בריבוע נקבל את המספרים {% equation %}1,-1,1,-1{% endequation %}, שהם שורשי היחידה מסדר 2, וכל אחד מהם התקבל בדיוק פעמיים. כבר מהדוגמה הזו מתקבל הרושם ש-{% equation %}\frac{n}{2}{% endequation %} שורשי היחידה הראשונים, עד {% equation %}\omega_{n}^{\frac{n}{2}}{% endequation %}, כבר מספיקים כדי "לכסות" את כל שורשי היחידה מסדר {% equation %}\frac{n}{2}{% endequation %}, וש-{% equation %}\frac{n}{2}{% endequation %} השורשים הבאים נותנים בדיוק את אותם ערכים (באותו סדר) כשמעלים אותם בריבוע.

בואו נוכיח את זה פורמלית. האבחנה הכללית היא ש-{% equation %}\omega_{dn}^{dk}=\omega_{n}^{k}{% endequation %}, וזה נובע ישירות מההגדרה: {% equation %}\omega_{dn}^{dk}=e^{\frac{2\pi idk}{dn}}=e^{\frac{2\pi ik}{n}}=\omega_{n}^{k}{% endequation %}. כמו כן, {% equation %}\omega_{n}^{k+n}=\omega_{n}^{k}\cdot\omega_{n}^{n}=\omega_{n}^{k}{% endequation %} (כי {% equation %}\omega_{n}^{n}=1{% endequation %} שהרי {% equation %}\omega_{n}{% endequation %} הוא שורש יחידה מסדר {% equation %}n{% endequation %}). לכן:

מכאן נקבל לכל {% equation %}0\le k&lt;\frac{n}{2}{% endequation %}:

{% equation %}\left(\omega_{n}^{k+\frac{n}{2}}\right)^{2}=\omega_{n}^{2k+n}=\omega_{n/2}^{k+n/2}=\omega_{n/2}^{k}=\omega_{n}^{2k}=\left(\omega_{n}^{k}\right)^{2}{% endequation %}

ראינו שהריבועים של {% equation %}\omega_{n}^{k}{% endequation %} ושל {% equation %}\omega_{n}^{k+\frac{n}{2}}{% endequation %} זהים, אבל למה הם שורש יחידה מסדר {% equation %}\frac{n}{2}{% endequation %}? אה, זה קל: כי {% equation %}\left[\left(\omega_{n}^{k}\right)^{2}\right]^{\frac{n}{2}}=\left(\omega_{n}^{k}\right)^{n}=1{% endequation %}. כעת, האם אנחנו באמת תופסים את <strong>כל</strong> שורשי היחידה מסדר {% equation %}\frac{n}{2}{% endequation %} כך? שוב, די בבירור כן, כי {% equation %}\omega_{n/2}^{k}=\omega_{n}^{2k}=\left(\omega_{n}^{k}\right)^{2}{% endequation %} (כאשר {% equation %}0\le k&lt;\frac{n}{2}{% endequation %}).

אז אם לסכם: הריבועים של {% equation %}\omega_{n}^{0},\omega_{n}^{1},\omega_{n}^{2},\dots,\omega_{n}^{\frac{n}{2}-1}{% endequation %} נותנים בדיוק את כל שורשי היחידה מסדר {% equation %}\frac{n}{2}{% endequation %}, והם זהים (גם בסדר שלהם) לריבועים של {% equation %}\omega_{n}^{\frac{n}{2}},\omega_{n}^{\frac{n}{2}+1},\dots,\omega_{n}^{n-1}{% endequation %}. עכשיו אפשר לעבור לאלגוריתם עצמו.

כזכור, אנחנו מתבוננים בפולינום {% equation %}A\left(x\right)=\sum_{t=0}^{n-1}a_{t}x^{t}{% endequation %} ורוצים לחשב את ההצבה של שורשי היחידה בו. מה שנעשה יהיה לפרק אותו לשני פולינומים - זה של המקדמים במקומות הזוגיים, וזה של המקדמים במקומות האי זוגיים. נגדיר:

{% equation %}A^{0}\left(x\right)=\sum_{t=0}^{\frac{n}{2}-1}a_{2t}x^{t}=a_{0}x^{0}+a_{2}x^{1}+a_{4}x^{2}+\dots+a_{n-2}x^{\frac{n}{2}-1}{% endequation %}

{% equation %}A^{1}\left(x\right)=\sum_{t=0}^{\frac{n}{2}-1}a_{2t+1}x^{2t+1}=a_{1}x^{0}+a_{3}x^{1}+a_{5}x^{2}+\dots+a_{n-1}x^{\frac{n}{2}-1}{% endequation %}

שימו לב - החזקות של ה-{% equation %}x{% endequation %}-ים הן רציפות, מ-1 ועד {% equation %}\frac{n}{2}-1{% endequation %}, ולכן קיבלנו שני פולינומים ממעלה נמוכה בחצי מזו של {% equation %}A\left(x\right){% endequation %}, שפשוט מחלקים ביניהם את המקדמים שלו.

עכשיו, אפשר לתאר את {% equation %}A\left(x\right){% endequation %} בעזרת שני הפולינומים הללו בצורה הפשוטה הבאה:

{% equation %}A\left(x\right)=A^{0}\left(x^{2}\right)+xA^{1}\left(x^{2}\right){% endequation %}

אם אתם לא מאמינים, נסו לבצע את החישוב בעצמכם, זה קל.

המסקנה פשוטה:

{% equation %}A\left(\omega_{n}^{k}\right)=A^{0}\left(\omega_{n}^{2k}\right)+\omega_{n}^{k}A^{1}\left(\omega_{n}^{2k}\right)=A^{0}\left(\omega_{n/2}^{k}\right)+\omega_{n}^{k}A^{1}\left(\omega_{n/2}^{k}\right){% endequation %}

וכפי שראינו, עבור {% equation %}k\ge\frac{n}{2}{% endequation %} אין צורך לחשב את הערכים של {% equation %}A^{0},A^{1}{% endequation %} על {% equation %}\omega_{n}^{k}{% endequation %} במפורש, אפשר להשתמש בערך שלו על {% equation %}\omega_{n}^{k-\frac{n}{2}}{% endequation %}. <strong>זו</strong> הנקודה שבה אנחנו מנצלים את שורשי היחידה כדי לחסוך משהו.

הנה פסאודו-קוד של האלגוריתם. מכיוון שאני חסיד גדול של גישת "לתת פסאודו-קוד שבאמת אפשר להריץ", הוא כתוב עבור מערכת האלגברה הממוחשבת Sage, שמשתמשת בשפה שהיא כמעט פייתון, עם כמה הרחבות (למשל, הסימן של החזקה). הדברים היחידים שנאלצתי לכתוב כאן ולא הייתי כותב בפסאודו קוד הם I במקום i בשביל השורש של מינוס 1, והמרה מפורשת של {% equation %}\frac{n}{2}{% endequation %} למספר שלם, אחרת Sage לא מוכן לבצע פעולות מודולו {% equation %}\frac{n}{2}{% endequation %}.

<div class="code-block">
{% highlight python %}
def fft(a):
  n = len(a)
  if (n == 1):
    return a
  omega = e^(2*pi*I/n)
  a0 = [a[2*k] for k in range(n/2)]
  a1 = [a[2*k+1] for k in range(n/2)]
  b0 = fft(a0)
  b1 = fft(a1)
  b = [b0[k % Integer(n/2)] + omega^k*b1[k % Integer(n/2)] for k in range(n)]
  return b
{% endhighlight %}
</div>

כמובן, הקוד הזה מסתיר בתוכו מורכבות בסיסית ש-Sage מטפל בה אוטומטית אבל בשפות תכנות פשוטות אין אותה - אריתמטיקה עם שורשי היחידה {% equation %}\omega_{n}^{k}{% endequation %}. אנחנו מעלים אותם בחזקות, ומחברים אותם, ובלאגן שלם. מי שירצה לממש את התמרת פורייה יצטרך, כמובן, לממש קודם את החלק שמתעסק באריתמטיקה של המספרים הללו (ולכן של מספרים מרוכבים בכלל). לרוב פשוט מתבססים על ספריות קיימות.

קל לנתח את סיבוכיות האלגוריתם על ידי מבט בקוד. בשורות 6-7 ("הפיצול") יש לנו לולאות עם זמן {% equation %}O\left(n\right){% endequation %} לכל אחת, וכך גם בשורה 10 ("המיזוג"). בשורות 8-9 יש לנו קריאה רקורסיבית לאלגוריתם עם קלט שגודלו חצי מהגודל הנוכחי. אז סיבוכיות האלגוריתם נתונה על ידי פתרון המשוואה {% equation %}T\left(n\right)=2T\left(\frac{n}{2}\right)+\Theta\left(n\right){% endequation %} - אותה משוואה של מיון מיזוג, שפתרונה הוא {% equation %}T\left(n\right)=\Theta\left(n\log n\right){% endequation %}.

מכאן גם קל לממש את האלגוריתם עבור ההתמרה ההפוכה. אפשר לכתוב את כל הקוד מחדש, אבל בשביל מה? הנוסחה, כזכור, היא {% equation %}a_{k}=\frac{1}{n}\sum_{t=0}^{n-1}b_{t}\omega_{n}^{kt}{% endequation %}. היא מאוד דומה לנוסחה של התמרה רגילה. אולי אפשר לחשב את ההתמרה ההפוכה בעזרת שימוש בהתמרה הרגילה? יש שני הבדלים בין ההתמרה הרגילה וההפוכה. ראשית, יש את הכפל ב-{% equation %}\frac{1}{n}{% endequation %}; ושנית, יש את הסימן של החזקה של שורש היחידה: הנוסחה של ההתמרה הרגילה היא {% equation %}b_{k}=\sum_{t=0}^{n-1}a_{t}\omega_{n}^{-kt}{% endequation %} ושם יש מינוס בחזקה, בעוד שכרגע אין.

התעלול המרכזי שנשתמש בו הוא שאנחנו כבר יודעים ש-{% equation %}\left(\omega_{n}^{k}\right)^{0}=\left(\omega_{n}^{k}\right)^{n}{% endequation %} ולכן {% equation %}\left(\omega_{n}^{k}\right)^{-t}=\left(\omega_{n}^{k}\right)^{n-t}{% endequation %}. לכן אפשר לכתוב את נוסחת ההתמרה הרגילה גם כך:

{% equation %}b_{k}=\sum_{t=0}^{n-1}a_{t}\omega_{n}^{-kt}=\sum_{t=0}^{n-1}a_{t}\left(\omega_{n}^{k}\right)^{n-t}=\sum_{r=1}^{n}a_{n-r}\left(\omega_{n}^{k}\right)^{r}{% endequation %}

כאן ביצעתי את החלפת המשתנה {% equation %}r=n-t{% endequation %}.

אם נסמן {% equation %}a_{n}\triangleq a_{0}{% endequation %} אפשר לכתוב את הסכום האחרון שלמעלה בתור {% equation %}\sum_{r=0}^{n-1}a_{n-r}\left(\omega_{n}^{k}\right)^{r}{% endequation %}, שנראה קצת יותר מוכר.

אם כן, אם נתונה לי הסדרה {% equation %}c_{0},c_{1},\dots,c_{n-1}{% endequation %} ואני רוצה לבצע עליה את ההתמרה ההפוכה, אני בעצם רוצה לחשב התמרת פורייה רגילה על הסדרה {% equation %}a_{0},\dots,a_{n-1}{% endequation %} המוגדרת על ידי המשוואה:

{% equation %}\sum_{r=0}^{n-1}a_{n-r}\left(\omega_{n}^{k}\right)^{r}=\frac{1}{n}\sum_{t=0}^{n-1}c_{t}\left(\omega_{n}^{k}\right)^{t}{% endequation %}

זה נותן לי את השוויונות הבאים:

{% equation %}a_{n-t}=\frac{1}{n}c_{t}{% endequation %} כאשר {% equation %}0\le t&lt;n{% endequation %}

כלומר, {% equation %}a_{t}=\frac{1}{n}c_{n-t}{% endequation %} כאשר {% equation %}0&lt;t\le n{% endequation %}. עבור {% equation %}a_{0}{% endequation %} כזכור מתקיים {% equation %}a_{0}=a_{n}{% endequation %}.

אם לסכם את מה שעשינו כאן, ה-{% equation %}a{% endequation %}-ים שלנו מתקבלים מה-{% equation %}c{% endequation %}-ים בצורה הבאה: את כל ה-{% equation %}c{% endequation %}-ים כופלים ב-{% equation %}\frac{1}{n}{% endequation %}; את האיבר הראשון שלהם משאירים ללא שינוי; את הסדר של היתר הופכים. במילים אחרות, אם {% equation %}c=\left(1,2,3,4\right){% endequation %} אז נקבל {% equation %}a=\left(\frac{1}{4},1,\frac{3}{4},\frac{1}{2}\right){% endequation %}. זה יוצא מאוד פשוט בקוד פייתון, שבו יש קונבנציה שאינדקסים שליליים ברשימה עוברים עליה מהסוף להתחלה:

<div class="code-block">
{% highlight python %}
def inverse_fft(b):
  n = len(b)
  return fft([b[k] / n for k in reversed(range(-(n-1),1))])
{% endhighlight %}
</div>

ומכאן קצרה הדרך לקוד עבור קונבולוציה:

<div class="code-block">
{% highlight python %}
def convolution(a,b):
  a_pad = a + [0 for i in range(len(a))]
  b_pad = b + [0 for i in range(len(b))]
  A = fft(a_pad)
  B = fft(b_pad)
  return inverse_fft([A[k]*B[k] for k in range(len(A))])[0:len(a)+len(b)-1]
{% endhighlight %}
</div>

הקוד הזה הוא נאיבי, במובן זה שהוא מניח ששתי הרשימות הן באותו האורך (ושהאורך הזה הוא חזקה של 2). יותר מזה, הוא גם עושה משהו מוזר - "מרפד" כל רשימה עם אפסים באופן שמכפיל את גודלה. למה? ובכן, כי שיקרתי קצת בפוסט הקודם: יצרתי את הרושם שקונבולוציה של שתי רשימות סופיות של מספרים אוטומטית מניחה שכל שאר המקומות הם 0, וזה אכן מה שצפוי שיהיה ומה שאנחנו משתמשים בו כשאנחנו כופלים פולינומים, למשל, אבל זה <strong>לא</strong> מה שהתמרת פורייה הבדידה עובדת איתו. זכרו שהתמרת פורייה הבדידה מתייחסת לרשימה של מספרים כאילו הם מייצגים פונקציה <strong>מחזורית</strong>, כלומר מחוץ לגבולות הרשימה הפונקציה מתחילה לחזור על עצמה. זה אומר שהקונבולוציה שאותה התמרת פורייה יודעת להפוך לכפל היא כזו שמניחה שהפונקציה היא מחזורית. הריפוד הוא פשוט דרך להתחמק מזה - אנחנו שמים אפסים בכל המקומות שעשויים להשפיע על החישוב, ואז מתעלמים מהאיברים ה"מיותרים" שנוצרו במהלך חישוב הקונבולוציה. זה מרגיש מלוכלך נורא, אבל זה למעשה לא פתרון כזה גרוע.

סיימנו לבינתיים עם FFT ועם התמרות פורייה למיניהן, אבל כמובן שהסיפור רק מתחיל כאן; פורייה נהיה מעניין כשמשתמשים בו בפועל. אני מקווה להציג בעתיד (אולי הלא רחוק) כמה שימושים מעניינים באמת.
