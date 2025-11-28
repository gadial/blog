---
title: "טורי טיילור"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - טורי טיילור
---


<h2>מבוא</h2>

אני יכול לשים אצבע מדויקת על אחד מהרגעים שבהם התחלתי להתלהב ממתמטיקה. זה היה בכיתה י"ב. המתמטיקה עבורי הייתה שלל דברים טכניים לא מעניינים במיוחד, שאליהם הצטרף לאחרונה מושג ה<strong>נגזרת</strong> שגם הוא לא הלהיב אותי במיוחד כי לא הבנתי מה בעצם הוא אומר. הספר אמר על גבולות ש"לא נוכל להציג את מושג הגבול במדויק" ואז נתן הסבר שלא הבנתי ממנו כלום. בקיצור, המתמטיקה עבורי הייתה חור שחור.

חור שחור גדול במיוחד היוו פונקציות כמו סינוס וקוסינוס. הבנתי איך מגדירים אותן, אבל לא הבנתי איך <strong>מחשבים</strong> אותן. מה הקסם שהמחשבון עושה כדי לקבל אותן. ואז, במהלך שיעור פיזיקה כלשהו (אהבתי אז פיזיקה הרבה יותר ממתמטיקה) השאלה הזו עלתה והמורה אמר שיסביר את זה לי ולחבר שלי אחרי השיעור. ואז נשארנו ובשתי דקות הוא הראה לי משהו שפוצץ לי את המוח וגרם לי להתחיל לשרבט נגזרות על נייר בהתלהבות ולא להאמין שזה עובד ולהרגיש, אולי בפעם הראשונה, שבאמת יש הגיון עמוק מאחורי כל זה ויש סיבה למה אנחנו עושים את כל הדברים הטכניים הללו.

מה שהמורה הראה לנו הוא מה שנקרא <strong>טור טיילור</strong>. הרעיון בטור טיילור הוא שזה <strong>טור חזקות</strong> (מה שדיברתי עליו <a href="https://gadial.net/2024/04/27/power_series/">בפוסט הקודם</a>) שניתן לחשב מתוך פונקציה {% equation %}f{% endequation %}, ועם קצת מזל הולך להיות שווה ל-{% equation %}f{% endequation %} בתחום שמעניין אותנו. אני אומר "עם קצת מזל" כי למרבה הצער זה לא תמיד עובד, ונראה דוגמאות, אבל כשזה עובד, זה עובד ממש יפה בזכות העובדה שטור חזקות הוא אובייקט פשוט למדי, ולכן ייצוג של פונקציה בעזרת טור חזקות הוא ייצוג מאוד נוח שלה. אני כן רוצה להזהיר שלמרות ההקדמה שלי, טור טיילור של פונקציה הוא <strong>לא בהכרח</strong> הדרך הכי טובה לחשב אותה - לפעמים יש שיטות אפקטיביות עוד יותר. אבל זו שיטה לא רעה.

<h2>מה זה טור טיילור בכלל?</h2>

בואו נתחיל מלהסביר מה זה טור טיילור בכלל. לצורך כך בואו <strong>נניח</strong> שיש לנו פונקציה {% equation %}f\left(x\right):\mathbb{R}\to\mathbb{R}{% endequation %} (כרגע אני מניח שזו פונקציה מהממשיים לעצמם, בהמשך נכניס לתמונה גם מספרים מרוכבים) ו<strong>נניח</strong> שהפונקציה הזו מיוצגת על ידי טור חזקות בעל רדיוס התכנסות {% equation %}R=\infty{% endequation %}, כלומר מתקיים {% equation %}f\left(x\right)=\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} לכל {% equation %}x\in\mathbb{R}{% endequation %} <strong>ונניח</strong> שמותר לנו לגזור את טור החזקות הזה (עוד לא הוכחתי שאפשר לעשות את זה), אז אני אקבל:

{% equation %}f^{\prime}\left(x\right)=\sum_{n=1}^{\infty}na_{n}x^{n-1}{% endequation %}

ועכשיו <strong>נניח</strong> שגם את הטור שקיבלתי עכשיו אפשר לגזור שוב, אז נקבל

{% equation %}f^{\prime\prime}\left(x\right)=\sum_{n=2}^{\infty}n\left(n-1\right)a_{n}x^{n-2}{% endequation %}

וככה באופן כללי נקבל

{% equation %}f^{\left(k\right)}\left(x\right)=\sum_{n=k}^{\infty}n\left(n-1\right)\cdots\left(n-k+1\right)a_{n}x^{n-k}{% endequation %}

עכשיו, מה קורה כשאני מציב {% equation %}x=0{% endequation %} בפונקציה ובכל הנגזרות שלה? אני הולך לאפס כל מקדם מלבד המקדם של {% equation %}x^{0}{% endequation %}, כלומר אני אקבל:

{% equation %}f\left(0\right)=a_{0}{% endequation %}

{% equation %}f^{\prime}\left(0\right)=1\cdot a_{1}{% endequation %}

{% equation %}f^{\prime\prime}\left(0\right)=2\cdot1\cdot a_{2}{% endequation %}

ובאופן כללי:

{% equation %}f^{\left(k\right)}\left(0\right)=k\cdot\left(k-1\right)\cdots1\cdot a_{k}=k!\cdot a_{k}{% endequation %}

כלומר, קיבלתי ייצוג מפורש של מקדמי טור החזקות עבור {% equation %}f{% endequation %} בעזרת הנגזרות של {% equation %}f{% endequation %}:

{% equation %}a_{k}=\frac{f^{\left(k\right)}\left(0\right)}{k!}{% endequation %}

ולכן אפשר לכתוב

{% equation %}f\left(x\right)=\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(0\right)}{n!}x^{n}{% endequation %}

הטור {% equation %}\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(0\right)}{n!}x^{n}{% endequation %} הוא מה שנקרא <strong>טור הטיילור</strong> של {% equation %}f{% endequation %}. שימו לב שהוא מוגדר היטב לכל {% equation %}f{% endequation %} שגזירה אינסוף פעמים ב-{% equation %}x=0{% endequation %}, ואם {% equation %}f{% endequation %} לא גזירה אינסוף פעמים ב-{% equation %}x=0{% endequation %} אז אפשר לקחת טור חזקות סביב נקודה אחרת, {% equation %}a{% endequation %}, כלומר להסתכל על הטור {% equation %}\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(a\right)}{n!}\left(x-a\right)^{n}{% endequation %} - על הטור הזה אומרים שזה טור הטיילור של {% equation %}f{% endequation %} שמפותח סביב {% equation %}x=a{% endequation %}. ההגדרה הזו עובדת לכל {% equation %}f{% endequation %} שגזירה אינסוף פעמים, אבל אני מזהיר ש<strong>לא נכון</strong> שמתקיים השוויון {% equation %}f\left(x\right)=\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(a\right)}{n!}\left(x-a\right)^{n}{% endequation %} אפילו אם {% equation %}f{% endequation %} באמת גזירה אינסוף פעמים ב-{% equation %}a{% endequation %}. ייתכן שטור החזקות הזה בכלל לא יתכנס, וייתכן שאפילו אם הוא מתכנס, הוא לא מתכנס לערך של {% equation %}f\left(x\right){% endequation %}, ואנחנו נראה דוגמאות גם לזה. אבל קודם בואו נראה דוגמאות לסיטואציות שבהן זה עובד יפה יחסית.

<h2>טור טיילור של אקספוננט ופונקציות טריגונומטריות</h2>

הדוגמא הראשונה והקלה ביותר היא הפונקציה {% equation %}f\left(x\right)=e^{x}{% endequation %}, אקספוננט. לא ניכנס כרגע לשאלה מאיפה היא באה ולמה אוהבים אותה (<a href="https://gadial.net/2010/03/27/exponent/">יש לי פוסט עליה</a>), אלא רק נזכיר את התכונה הבסיסית שלה: {% equation %}\left(e^{x}\right)^{\prime}=e^{x}{% endequation %}, היא הנגזרת שלה עצמה. לכן יש לה אינסוף נגזרות ב-{% equation %}x=0{% endequation %} וכשמציבים בהן {% equation %}x=0{% endequation %} מקבלים 1, כלומר {% equation %}f^{\left(n\right)}\left(0\right)=1{% endequation %} לכל {% equation %}n{% endequation %}, מה שנותן את טור הטיילור {% equation %}\sum_{n=0}^{\infty}\frac{x^{n}}{n!}{% endequation %}. לשמחתנו, הטור הזה באמת מתכנס ושווה ל-{% equation %}e^{x}{% endequation %} בכל {% equation %}\mathbb{R}{% endequation %} ולכן אפשר לכתוב

{% equation %}e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\ldots{% endequation %}

זה טור מצויין כדי לחשב את {% equation %}e^{x}{% endequation %} (למרות ששוב, זו לא הדרך <strong>הכי טובה</strong> לחשב את {% equation %}e^{x}{% endequation %}).

בואו נעבור עכשיו לפונקציות הטריגונומטריות - סינוסים וקוסינוסים. גם עליהן <a href="https://gadial.net/2010/03/31/sine_and_cosine_via_ode/">יש לי פוסט</a> שמנסה להסביר את אחת מהדרכים שבהן הן צצות - בתור פתרונות של המשוואה הדיפרנציאלית {% equation %}f^{\prime\prime}=-f{% endequation %}, מה שאומר שלנגזרות שלהן יש "מחזור מאורך 4" - אחרי שגוזרים אותן 4 פעמים חוזרים לפונקציה המקורית. זה נובע מכך ש:

{% equation %}\left(\sin x\right)^{\prime}=\cos x{% endequation %}

{% equation %}\left(\cos x\right)^{\prime}=-\sin x{% endequation %}

בנוסף, {% equation %}\sin0=0{% endequation %} ו-{% equation %}\cos0=1{% endequation %}. אלו מספיקים לנו כדי למצוא את טורי טיילור של הפונקציות הללו - ולמרבה השמחה, גם הפעם הטורים הללו שווים לפונקציות בכל {% equation %}\mathbb{R}{% endequation %} (נקודה שצריך להזכיר היא שכאן {% equation %}\sin,\cos{% endequation %} הן פונקציות שמניחות שהקלט שלהן נתון <a href="https://gadial.net/2008/01/11/radians/">ברדיאנים</a>, לא במעלות; אם היה נתון במעלות הנוסחאות לא היו יפות כל כך). נקבל:

{% equation %}\sin x=\sin\left(0\right)x^{0}+\cos\left(0\right)x^{1}-\frac{\sin\left(0\right)}{2}x^{2}-\frac{\cos\left(0\right)}{6}x^{3}+\ldots{% endequation %}

כל פעם שכתוב {% equation %}\sin\left(0\right){% endequation %} זה הולך להתאפס, ולכן נישאר רק עם האיברים במקומות <strong>האי-זוגיים</strong>. עבורם, {% equation %}\cos\left(0\right)=1{% endequation %} ולכן ההשפעה של המקדם תהיה רק בכך שפעם מחברים ופעם מחסרים; ואסור לשכוח את ה-{% equation %}n!{% endequation %} שבמכנה. כלומר, אני אקבל:

{% equation %}\sin x=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\ldots{% endequation %}

ובכתיב קומפקטי:

{% equation %}\sin x=\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{x^{2n+1}}{\left(2n+1\right)!}{% endequation %}

עבור קוסינוס נקבל

{% equation %}\cos x=\cos\left(0\right)x^{0}-\sin\left(0\right)x^{1}-\frac{\cos\left(0\right)}{2}x^{2}+\frac{\sin\left(0\right)}{6}x^{3}+\ldots{% endequation %}

כלומר הפעם נשארים רק האיברים במקומות <strong>הזוגיים</strong>, וגם הם מזפזפים בין פלוס למינוס:

{% equation %}\cos x=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+\ldots{% endequation %}

ובכתיב קומפקטי:

{% equation %}\cos x=\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{x^{2n}}{\left(2n\right)!}{% endequation %}

שימו לב למשהו נחמד שקורה כאן: הטורים של {% equation %}\sin x,\cos x{% endequation %} נראים כאילו לקחנו את הטור של {% equation %}e^{x}{% endequation %} ופירקנו אותו לשני טורים - אחד עם האיברים במקומות הזוגיים והשני עם האיברים במקומות האי זוגיים. רק שאז גם כפלנו חלק מהאיברים הללו במינוס 1, וזה קצת פחות ברור, עד שחושבים על הרעיון הגאוני של להכניס לתמונה <strong>מספרים מרוכבים</strong>. את כל מה שאני עושה כאן צריך כמובן להצדיק מתמטית, אבל בואו בינתיים נזרום עם ההנחה שזה חוקי, ניקח את הטור של {% equation %}e^{x}{% endequation %}, ונציב בתוכו {% equation %}ix{% endequation %} במקום סתם {% equation %}x{% endequation %}. נקבל:

{% equation %}e^{ix}=1+ix+\frac{\left(ix\right)^{2}}{2!}+\frac{\left(ix\right)^{3}}{3!}+\frac{\left(ix\right)^{4}}{4!}+\ldots={% endequation %}

{% equation %}=1+ix-\frac{x^{2}}{2!}-i\frac{x^{3}}{3!}+\frac{x^{4}}{4!}+i\frac{x^{5}}{5!}-\frac{x^{6}}{6!}-\ldots={% endequation %}

{% equation %}=\left(1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\ldots\right)+i\left(x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\ldots\right)={% endequation %}

{% equation %}=\cos x+i\sin x{% endequation %}

כלומר, קיבלנו את הנוסחה {% equation %}e^{ix}=\cos x+i\sin x{% endequation %} שנקראת <strong>נוסחת אוילר</strong> ומפורסמת במיוחד כשמציבים בתוכה {% equation %}x=\pi{% endequation %} כי מכיוון ש-{% equation %}\cos\pi=-1{% endequation %} ו-{% equation %}\sin\pi=0{% endequation %}, מקבלים

{% equation %}e^{i\pi}=-1{% endequation %}

ואחרי העברת אגפים:

{% equation %}e^{i\pi}+1=0{% endequation %}

וזו באמת נוסחה מבדרת ביותר כי היא מחברת ביחד חמישה מהסלבריטיז של המתמטיקה: {% equation %}0,1,e,i,\pi{% endequation %}. אבל האם כדי לקבל אותה היה לי מותר לעשות את המעברים שביצעתי? ובכן, אני אדבר על זה בפוסט נפרד, כשאתחיל לדבר ברצינות על פונקציות מרוכבות (כן, השורה התחתונה היא "כן").

<h2>טור טיילור של הטור ההנדסי המתכנס ואיך זה קשור לקומבינטוריקה</h2>

בואו עכשיו נסתכל לרגע על הסיפור מהכיוון ההפוך - נתחיל מטור טיילור ונעבור לפונקציה שנותנת אותו: הטור ההנדסי המתכנס, {% equation %}1+x+x^{2}+\ldots{% endequation %} שמתכנס ל-{% equation %}\left|x\right|<1{% endequation %} וראינו כבר שנותן {% equation %}\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}{% endequation %}. כמובן, גם בהכרזה שלי שזה טור הטיילור של הפונקציה מסתתר משפט: שאין לפונקציה ייצוג באמצעות שני טורי פונקציות שונים. אבל לא צריך להאמין למשפט כאן, אפשר פשוט לגזור את {% equation %}\frac{1}{1-x}{% endequation %}. נכתוב {% equation %}\left(\frac{1}{1-x}\right)=\left(1-x\right)^{-1}{% endequation %} ונגזור על פי כלל השרשרת:

{% equation %}\left[\left(1-x\right)^{-1}\right]^{\prime}=-\left(1-x\right)^{-2}\cdot\left(1-x\right)^{\prime}=\frac{1}{\left(1-x\right)^{2}}{% endequation %}

באופן דומה אפשר לגזור את {% equation %}\frac{1}{\left(1-x\right)^{n}}{% endequation %}:

{% equation %}\left[\left(1-x\right)^{-n}\right]^{\prime}=-n\left(1-x\right)^{-\left(n+1\right)}\cdot\left(1-x\right)^{\prime}=\frac{n}{\left(1-x\right)^{n+1}}{% endequation %}

כלומר, בכל פעם שבה גוזרים משהו מהצורה {% equation %}\frac{1}{\left(1-x\right)^{n}}{% endequation %} התוצאה היא גם כפל ב-{% equation %}n{% endequation %} וגם הגדלת מעריך החזקה שבמכנה. זה מאפשר לנו לקבל באינדוקציה את הנגזרת ה-{% equation %}n{% endequation %}-ית של {% equation %}\frac{1}{1-x}{% endequation %}: {% equation %}\left(\frac{1}{1-x}\right)^{\left(n\right)}=\frac{n!}{\left(1-x\right)^{n+1}}{% endequation %}, ולכן כשנציב את זה בנוסחה לטור טיילור באמת נקבל

{% equation %}\frac{1}{1-x}=\sum_{n=0}^{\infty}\frac{n!}{\left(1-0\right)^{n+1}}\cdot\frac{x^{n}}{n!}=\sum_{n=0}^{\infty}x^{n}{% endequation %}

כלומר, כאן ה-{% equation %}n!{% endequation %} שתמיד מופיע בנוסחה של טור טיילור מצומצם עם מה שצץ לנו בסדרת הנגזרות.

עוד משהו חמוד שאפשר לעשות עם הטור {% equation %}\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}{% endequation %}, עכשיו כשאנחנו יודעים מה הנגזרת של {% equation %}\frac{1}{1-x}{% endequation %}, הוא לגזור את שני האגפים יחד ולקבל

{% equation %}\frac{1}{\left(1-x\right)^{2}}=\sum_{n=1}^{\infty}nx^{n-1}=1+2x+3x^{2}+4x^{3}+\ldots{% endequation %}

בשוויון הזה השתמשתי <a href="https://gadial.net/2019/02/13/coupon_collector_problem/">בפוסט על בעיית איסוף הקופונים</a>, כשחישוב תוחלת נתן לי באופן טבעי את הטור, והיה לי נוח לעבור ממנו לייצוג הקומפקטי {% equation %}\frac{1}{\left(1-x\right)^{2}}{% endequation %}, וזו כמובן רק דוגמא אחת - השוויונות הללו הם כלי עבודה בסיסי במתמטיקה.

אפשר כמובן להמשיך עם זה הלאה ולגזור עוד את הפונקציה והטור, על פי החישובים שכבר ראינו, ולקבל

{% equation %}\frac{2}{\left(1-x\right)^{3}}=\sum_{n=2}^{\infty}n\left(n-1\right)x^{n-2}{% endequation %}

או, בייצוג היותר מקובל,

{% equation %}\frac{1}{\left(1-x\right)^{3}}=\sum_{n=2}^{\infty}\frac{n\left(n-1\right)}{2}x^{n-2}{% endequation %}

ובאופן כללי:

{% equation %}\frac{1}{\left(1-x\right)^{k}}=\sum_{n=k}^{\infty}\frac{n\left(n-1\right)\cdots\left(n-k+1\right)}{k!}x^{n-k}{% endequation %}

הביטוי {% equation %}\frac{n\left(n-1\right)\cdots\left(n-k+1\right)}{k!}{% endequation %} מזכיר קומבינטוריקה, ולא במקרה. אפשר לכתוב {% equation %}n\left(n-1\right)\cdots\left(n-k+1\right)=\frac{n!}{\left(n-k\right)!}{% endequation %}, ולכן לקבל

{% equation %}\frac{n\left(n-1\right)\cdots\left(n-k+1\right)}{k!}=\frac{n!}{k!\left(n-k\right)!}={n \choose k}{% endequation %}

ולכן קיבלנו

{% equation %}\frac{1}{\left(1-x\right)^{k}}=\sum_{n=k}^{\infty}{n \choose k}x^{n-k}{% endequation %}

וזה ביטוי שימושי מאוד כשמנסים למצוא <strong>פונקציות יוצרות</strong> לבעיות קומבינטוריות - אבל זה נושא לפעם אחרת.

<h2>טור טיילור של לוגריתם</h2>

שמחים וטובי לב מההצלחות שלנו עד עכשיו, אנחנו רוצים לרוץ ולטפל בפונקציה המסובכת הבאה שכולנו מכירים: {% equation %}\ln x{% endequation %}, הפונקציה ההופכית של {% equation %}e^{x}{% endequation %}. כזכור, {% equation %}\ln x=y{% endequation %} אם {% equation %}e^{y}=x{% endequation %}. זה בפרט אומר ש-{% equation %}\ln0{% endequation %} זה ביטוי <strong>לא מוגדר</strong> כי אין {% equation %}y{% endequation %} כך ש-{% equation %}e^{y}=0{% endequation %}. בכלל, הפונקציה לא מוגדרת לשום {% equation %}x\le0{% endequation %}, כך שאפשר לשכוח מטור טיילור שעובד בכל {% equation %}\mathbb{R}{% endequation %}. מצד שני אנחנו עדיין רוצים <strong>משהו</strong>. אז כאן אפשר טיפה להתחכם. במקום לדבר על הפונקציה {% equation %}\ln x{% endequation %}, נדבר על הפונקציה {% equation %}\ln\left(1-x\right){% endequation %}, שכן מוגדרת ב-{% equation %}x=0{% endequation %} ואפילו מאוד פשוטה שם: {% equation %}\ln\left(1-0\right)=\ln1=0{% endequation %}, ואני הולך למצוא עבורה טור טיילור שעובד לכל {% equation %}\left|x\right|<1{% endequation %}. לכאורה לדבר על הפונקציה הזו ממש מגביל אותנו כי נראה שאני יכול לחשב את {% equation %}\ln{% endequation %} רק עבור ערכים בתחום שמ-0 עד 2, אבל בפועל אפשר לחשב באמצעות הפונקציה הזו את {% equation %}\ln{% endequation %} המקורית לכל ערך שנרצה: נניח שאנחנו רוצים לחשב את {% equation %}\ln t{% endequation %} עבור {% equation %}t>0{% endequation %}, אז נגדיר {% equation %}x=1-\frac{1}{t}{% endequation %} ועכשיו נשים לב לשני דברים:

<ol> <li>מכיוון ש-{% equation %}t>0{% endequation %} אז {% equation %}0<\frac{1}{t}<1{% endequation %} ולכן {% equation %}0<x<1{% endequation %} ובפרט אנחנו בתחום שבו טור הטיילור של {% equation %}\ln\left(1-x\right){% endequation %} מתכנס;</li>


<li>על ידי העברת אגפים נקבל {% equation %}\frac{1}{t}=1-x{% endequation %}, כלומר {% equation %}t=\frac{1}{1-x}{% endequation %}, וכעת אפשר להשתמש בתכונה של לוגריתמים: {% equation %}\ln\left(t\right)=\ln\left(\frac{1}{1-x}\right)=-\ln\left(1-x\right){% endequation %}</li>

</ol>

כלומר, על ידי חישוב {% equation %}\ln\left(1-x\right){% endequation %} וכפל במינוס אחד, מקבלים את {% equation %}\ln t{% endequation %} וזה לכל ערך של {% equation %}t{% endequation %} שנרצה (ושוב אני מזהיר - זו לא הדרך הכי יעילה לחשב את {% equation %}\ln{% endequation %}! אבל זה עובד).

אוקיי, אז בואו נמצא את טור הטיילור של {% equation %}\ln\left(1-x\right){% endequation %}. 

מה הנגזרת של {% equation %}\ln x{% endequation %}? מחדו"א אנחנו יודעים ש-{% equation %}\left(\ln x\right)^{\prime}=\frac{1}{x}{% endequation %}. לכן עם כלל השרשרת נקבל

{% equation %}\left[\ln\left(1-x\right)\right]^{\prime}=-\frac{1}{1-x}{% endequation %}

הופה! פגשנו את ידידנו הותיק {% equation %}\frac{1}{1-x}{% endequation %}, ש<strong>לגמרי במקרה</strong> לפני רגע בחלק הקודם של הפוסט חישבנו את כל הנגזרות שלו מכאן ועד אינסוף. אבל אנחנו לא באמת חייבים לעבור שוב דרך הנוסחה הכללית של טור טיילור, אלא אפשר לקחת את טור הטיילור של {% equation %}\frac{1}{1-x}{% endequation %} ולבצע עליו <strong>אינטגרציה איבר איבר</strong>. במילים אחרות, אנחנו מתחילים מהשוויון

{% equation %}\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}{% endequation %}

שאנחנו כבר מכירים, כופלים ב-{% equation %}-1{% endequation %} ואז לוקחים אינטגרל ומקבלים:

{% equation %}\ln\left(1-x\right)=-\int_{0}^{x}\frac{1}{1-t}dt=-\int_{0}^{x}\sum_{n=0}^{\infty}t^{n}dt={% endequation %}

{% equation %}=-\sum_{n=0}^{\infty}\int_{0}^{x}t^{n}dt=-\sum_{n=0}^{\infty}\frac{x^{n+1}}{n+1}{% endequation %}

כאן השתמשתי באחד המשפטים <a href="https://gadial.net/2024/02/24/sequences_and_series_of_functions/">שהראיתי על טורי פונקציות</a>: אם טור מתכנס במ"ש, אז אפשר לבצע עליו אינטגרציה איבר-איבר (שימו לב שחישבתי אינטגרל <strong>מסוים</strong> בתור דרך לקבל אינטגרל לא מסוים ספציפי). כמובן שצריך להצדיק את זה שהטור מתכנס במ"ש במקרה הזה, אבל אנחנו אפילו לא צריכים משפטים כלליים על טורי טיילור: אנחנו כבר יודעים לחשב את רדיוס ההתכנסות של {% equation %}\sum_{n=0}^{\infty}x^{n}{% endequation %} ולדעת שהוא {% equation %}R=1{% endequation %}, ולכן הטור מתכנס במ"ש בכל תחום {% equation %}\left|x\right|<r<R{% endequation %} שנרצה.

לסיכום, קיבלנו את הנוסחה

{% equation %}\ln\left(1-x\right)=-\sum_{n=1}^{\infty}\frac{x^{n}}{n}=-x-\frac{x^{2}}{2}-\frac{x^{3}}{3}-\ldots{% endequation %}

כדי לחשב ערכים קטנים של {% equation %}\ln{% endequation %}, בין {% equation %}0{% endequation %} ל-2, נוח יותר לקחת את הנוסחה הזו ולהציב בה {% equation %}y=-x{% endequation %} ולקבל

{% equation %}\ln\left(1+y\right)=y-\frac{y^{2}}{2}+\frac{y^{3}}{3}-\ldots{% endequation %}

ואז להשתמש בנוסחה הזו תוך שאנחנו מציבים בה ישירות ערכים של {% equation %}-1<y<1{% endequation %}.

עבור ערכי {% equation %}y{% endequation %} שמקיימים {% equation %}\left|y\right|>1{% endequation %} הטור יתבדר בודאות (ראינו את זה כשהוכחנו שזה מה שרדיוס התכנסות עושה) ועבור {% equation %}y=-1{% endequation %} ברור לנו שהוא יתפוצץ כי {% equation %}\ln0{% endequation %} מתפוצץ, אבל מה עם {% equation %}y=1{% endequation %}? באופן כללי, על מספר שיושב "על" רדיוס ההתכנסות הטור עדיין יכול להתכנס - ואם הוא מתכנס, אז הנוסחה של טור טיילור עדיין עובדת (גם אם זה צריך להוכיח). במקרה של {% equation %}y=1{% endequation %}, הטור שאנחנו מקבלים הוא טור מוכר ואהוב במתמטיקה - <strong>הטור ההרמוני המתחלף</strong>:

{% equation %}1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\ldots{% endequation %}

הטור הזה הוא הדוגמא הראשונה שנותנים כשמציגים את מבחן ההתכנסות לטורים של לייבניץ, שאומר שאם {% equation %}a_{n}{% endequation %} היא סדרה חיובית ששואפת לאפס, אז הטור {% equation %}\sum_{n=0}^{\infty}\left(-1\right)^{n}a_{n}{% endequation %} מתכנס. מכאן שהטור ההרמוני המתחלף מתכנס, ועל פי הנוסחה שראינו, כשמציבים בה {% equation %}y=1{% endequation %}:

{% equation %}1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\ldots=\ln2{% endequation %}

<h2>מתי העניינים לא כל כך נחמדים?</h2>

מה שעשיתי עד עכשיו כלל תיאור של שלל טורי טיילור עם מעט מאוד הצדקה למה שעשיתי. זה חשוב בשביל שיהיה לנו כיף, אבל מאוד מסוכן באופן כללי, ולכן בפוסט הבא אני הולך לתת את המשפטים הפורמליים שמצדיקים את הדברים שעשיתי עד כה. לפני שנגיע לזה, אני רוצה בפוסט הזה לראות איך דברים יכולים להישבר: הדוגמא הקלאסית היא פונקציה {% equation %}f\left(x\right){% endequation %} שגזירה אינסוף פעמים ב-{% equation %}x=0{% endequation %} ולכן אפשר להגדיר את הטור {% equation %}\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(0\right)}{n!}x^{n}{% endequation %}; ויותר מזה, הטור הזה גם יתכנס לכל {% equation %}x\in\mathbb{R}{% endequation %}, אבל <strong>לא יתקיים</strong> ש-{% equation %}f\left(x\right)=\sum_{n=0}^{\infty}\frac{f^{\left(n\right)}\left(0\right)}{n!}x^{n}{% endequation %} עבור {% equation %}x\ne0{% endequation %}.

הפונקציה הרלוונטית היא

{% equation %}f\left(x\right)=\begin{cases} e^{-\frac{1}{x^{2}}} & x\ne0\\ 0 & x=0 \end{cases}{% endequation %}

מה הנגזרת שלה? עבור {% equation %}x\ne0{% endequation %} אפשר לקחת סביבה של {% equation %}x{% endequation %} שבה {% equation %}f\left(y\right)=e^{-\frac{1}{y^{2}}}{% endequation %} לכל {% equation %}y{% endequation %} בסביבה, ולכן אפשר לחשב את הנגזרת ב-{% equation %}x{% endequation %} על פי כלל השרשרת:

{% equation %}\left(e^{-\frac{1}{x^{2}}}\right)^{\prime}=e^{-\frac{1}{x^{2}}}\cdot\left[-\frac{1}{x^{2}}\right]^{\prime}=\frac{2}{x^{3}}e^{-\frac{1}{x^{2}}}\cdot{% endequation %}

החלק המעניין הוא הנגזרת ב-{% equation %}x=0{% endequation %}, שאותה נצטרך לחשב ישירות על פי הנוסחה:

{% equation %}f^{\prime}\left(0\right)=\lim_{h\to0}\frac{f\left(h\right)-f\left(0\right)}{h}=\lim_{h\to0}\frac{e^{-\frac{1}{h^{2}}}}{h}{% endequation %}

זה גבול קצת טריקי: בדרך כלל בגבולות כאלו קל להשתמש ב<strong>כלל לופיטל</strong> אבל כאן הגזירה של המונה רק תסבך אותנו עוד יותר. גישה אחרת היא להשתמש בכלל הסנדוויץ': אם אני אוכיח ש-{% equation %}0\le e^{-\frac{1}{h^{2}}}\le h^{2}{% endequation %} אז מכך ש-

{% equation %}0=\lim_{h\to0}\frac{0}{h}\le\lim_{h\to0}\frac{e^{-\frac{1}{h^{2}}}}{h}\le\lim_{h\to0}\frac{h^{2}}{h}=\lim_{h\to0}h=0{% endequation %} 

אני אקבל ש-{% equation %}\lim_{h\to0}\frac{e^{-\frac{1}{h^{2}}}}{h}=0{% endequation %}. אי השוויון {% equation %}0\le e^{-\frac{1}{h^{2}}}{% endequation %} הוא מובן מאליו כי {% equation %}e{% endequation %} בחזקת משהו זה תמיד חיובי; בשביל {% equation %}e^{-\frac{1}{h^{2}}}\le h^{2}{% endequation %} אני אלך, איך לא, לטור הטיילור של {% equation %}e^{x}{% endequation %}:

{% equation %}e^{x}=1+x+\frac{x^{2}}{^{2!}}+\frac{x^{3}}{3!}+\ldots{% endequation %}

בפרט, לכל {% equation %}x{% endequation %} <strong>חיובי</strong>, כל איברי הטור חיוביים ולכן לכל {% equation %}n{% endequation %} מתקיים {% equation %}e^{x}\ge\frac{x^{n}}{n!}{% endequation %}, כלומר {% equation %}\frac{1}{e^{x}}\le\frac{n!}{x^{n}}{% endequation %}, כלומר {% equation %}e^{-x}\le\frac{n!}{x^{n}}{% endequation %}. במקרה שלנו נציב {% equation %}x=\frac{1}{h^{2}}{% endequation %} (שימו לב ש-{% equation %}x{% endequation %} חיובי תמיד כי {% equation %}h^{2}{% endequation %} חיובי תמיד), ונציב {% equation %}n=1{% endequation %} ונקבל {% equation %}e^{-\frac{1}{h^{2}}}=e^{-x}\le\frac{1!}{x}=h^{2}{% endequation %}. זה מסיים את ההוכחה שהנגזרת של {% equation %}f{% endequation %} היא

{% equation %}f^{\prime}\left(x\right)=\begin{cases} \frac{2}{x^{3}}e^{-\frac{1}{x^{2}}} & x\ne0\\ 0 & x=0 \end{cases}{% endequation %}

אבל לא גמרנו פה! אנחנו רוצים ש-{% equation %}f{% endequation %} תהיה גזירה <strong>אינסוף</strong> פעמים באפס, בשביל זה צריך לחשב גם את הנגזרת של {% equation %}f^{\prime}{% endequation %} וכן הלאה, ואת הנגזרת של {% equation %}\frac{2}{x^{3}}e^{-\frac{1}{x^{2}}}{% endequation %} כבר יותר קשה לחשב, אבל אני לא צריך כי אני יכול לנפנף בידיים: כשאני גוזר את הפונקציה הזו, אני אקבל {% equation %}e^{-\frac{1}{x^{2}}}{% endequation %} כפול כל מני גורמים שמתקבלים מכפל וחילוק של {% equation %}e^{-\frac{1}{x^{2}}}{% endequation %} בחזקות של {% equation %}x{% endequation %}. מספיק אם כך להראות שלא משנה כמה החזקה של האיקס שבה כופלים גבוהה, עדיין הגבול יוצא אפס - כלומר, להראות ש-{% equation %}\lim_{h\to0}\frac{e^{-\frac{1}{h^{2}}}}{h^{k}}=0{% endequation %} לכל {% equation %}k{% endequation %}. בשביל לראות את זה נשתמש בסנדוויץ' כמו קודם. כזכור, ראינו ש-{% equation %}e^{-x}\le\frac{n!}{x^{n}}{% endequation %} לכל {% equation %}n{% endequation %}; ה"לכל {% equation %}n{% endequation %}" הזה הוא הכוח שלי. אני פשוט אציב {% equation %}n=k{% endequation %} ו-{% equation %}x=\frac{1}{h^{2}}{% endequation %} ואקבל 

{% equation %}e^{-\frac{1}{h^{2}}}\le k!h^{2k}{% endequation %}, ואז

{% equation %}\lim_{h\to0}\frac{e^{-\frac{1}{h^{2}}}}{h^{k}}\le\lim_{h\to0}\frac{k!h^{2k}}{h^{k}}=\lim_{h\to0}k!h^{k}=0{% endequation %}

מה שמסיים את ההוכחה גם במקרה הזה: לכל {% equation %}k{% endequation %}, קיבלנו ש-{% equation %}f^{\left(k\right)}\left(0\right)=0{% endequation %}. זה אומר שבפרט, טור הטיילור של הפונקציה הזו הוא פשוט 0, אבל כמובן שהפונקציה איננה זהותית אפס. זו האנומליה שרצינו.

יפה, אז כאן סיימנו עם הכיף והמשחקים ובפוסט הבא יגיעו הסבל והטרחנות של המשפטים הפורמליים. יהיה כיף! 