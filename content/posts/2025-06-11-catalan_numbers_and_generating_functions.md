---
title: "פונקציות יוצרות ומספרי קטלן"
layout: post
categories:
  - קומבינטוריקה
tags:
  - מספרי קטלן
  - פונקציות יוצרות
---


<h2>מבוא</h2>

<a href="https://gadial.net/2025/05/31/catalan_numbers/">בפוסט הקודם</a> שלי כתבתי על מספרי קטלן, סדרת המספרים {% equation %}1,1,2,5,14,42,\ldots{% endequation %}. הראיתי נוסחת נסיגה עבורה, {% equation %}C_{n+1}=\sum_{k=0}^{n}C_{k}C_{n-k}{% endequation %}; הראיתי נוסחה סגורה עבורה, {% equation %}C_{n}=\frac{1}{n+1}{2n \choose n}{% endequation %}; והראיתי שלל בעיות ספירה שמספרי קטלן פותרים, משילושים של מצולעים, עבור בעצים בינאריים וכלה במגדלי קפלר. רק דבר אחד לא הראיתי, למרות שהוא מושג מרכזי וחשוב בקומבינטוריקה באופן כללי: את <strong>הפונקציה היוצרת</strong> של מספרי קטלן. לא עשיתי את זה כי זה היה מעלה פי כמה את רמת הטכניות של הפוסט ומרחיק אותי מהנושא המעניין בו, שהוא מספרי קטלן עצמם; אבל עכשיו אחרי שהתרגלנו אליהם (או דילגנו לגמרי על הפוסט הקודם כי אנחנו רוצים את האקשן שיהיה כאן) אפשר להפנות זרקור אל פונקציות יוצרות בכלל, וזו של מספרי קטלן בפרט.

כמיטב מסורת הבלוג, <a href="https://gadial.net/2011/08/07/generating_functions_hardcore_1/">כבר יש לי פוסט על הנושא הזה</a>, כולל אזכור של מספרי קטלן, אבל הפעם אני רוצה <strong>לחפור</strong> ולהציג נושאים שרק נגעתי בהם בעבר ברמת פורמליות הרבה יותר גדולה. זה אומר שהפוסט יהיה טכני יחסית, ויילך ויסתבך ככל שאתקדם, אבל נגיע לפונקציה היוצרת של קטלן יחסית מהר; האתגר יהיה להבין למה הפונקציה היוצרת הזו "חוקית" וכמה אפשר להכליל את זה. אני אגלה מראש כבר עכשיו שהפונקציה היוצרת היא {% equation %}C\left(x\right)=\frac{1-\sqrt{1-4x}}{2x}{% endequation %}, אבל - מה זה בעצם אומר? ואיך מגיעים לזה? בשביל זה אני אצטרך לדבר קצת על דברים.

<h2>למה פונקציות יוצרות זה כמו פולינומים, רק פשוט יותר</h2>

הרעיון בפונקציות יוצרות הוא לקודד סדרות מספרים כמו מספרי קטלן בתור <strong>טורי חזקות פורמליים</strong>. זה דורש הגדרה של מה זה בכלל טור חזקות פורמלי, ואם לא מכירים אותם המושג הזה קצת מוזר בהתחלה אז אפשר להתחיל עם אובייקטים יותר ידידותיים: <strong>פולינומים</strong>. התיאור הכללי שלנו של פולינום הוא 

{% equation %}a\left(x\right)=\sum_{n=0}^{d}a_{n}x^{n}{% endequation %}

כאשר {% equation %}d{% endequation %} הוא <strong>דרגת</strong> הפולינום - החזקה הגבוהה ביותר שלו שהמקדם שלה שונה מאפס. עכשיו, על פולינומים אפשר להגדיר פעולות חיבור וכפל, אז בשביל להדגים את זה בואו נציג שני פולינומים מדרגות {% equation %}d_{1},d_{2}{% endequation %}:

{% equation %}a\left(x\right)=\sum_{n=0}^{d_{1}}a_{n}x^{n}{% endequation %}

{% equation %}b\left(x\right)=\sum_{n=0}^{d_{2}}b_{n}x^{n}{% endequation %}

עכשיו החיבור מוגדר "איבר-איבר":

{% equation %}a\left(x\right)+b\left(x\right)=\sum_{n=0}^{\max\left\{ d_{1},d_{2}\right\} }\left(a_{n}+b_{n}\right)x^{n}{% endequation %}

וזה בסך הכל יפה מאוד חוץ מהאיכסה של ה-{% equation %}\max\left\{ d_{1},d_{2}\right\} {% endequation %} למעלה שגם מצריך אותנו לענות על שאלות קשות כמו מה המקדמים של פולינום מעבר לדרגה המקסימלית שלו (אפס. הם אפס).

מה עם כפל? כאן זה טיפה יותר מסובך אבל לא בצורה חריגה. בואו נתחיל עם דוגמא:

{% equation %}\left(a_{1}x+a_{0}\right)\left(b_{1}x+b_{0}\right)=a_{1}b_{1}x^{2}+\left(a_{0}b_{1}+a_{1}b_{0}\right)x^{1}+a_{0}b_{0}x^{0}{% endequation %}

כדאי לחשב את הדוגמא הזו ידנית, או אפילו משהו עם איבר אחד נוסף לאחד הפולינומים, כדי לקבל תחושה טובה של "מה הולך פה". מה שמקבלים הוא שהמקדם של כל חזקה של {% equation %}x^{n}{% endequation %} הוא <strong>סכום</strong> של איברים, כשכל איבר הוא <strong>מכפלה</strong> של מקדם של {% equation %}a\left(x\right){% endequation %} ומקדם של {% equation %}b\left(x\right){% endequation %}, כשהמקדמים נבחרים כך שסכום האינדקסים של שניהם יוצא {% equation %}n{% endequation %}.

כדי לכתוב נוסחה כללית עבור זה, קודם כל אני אכתוב

{% equation %}a\left(x\right)\cdot b\left(x\right)=\sum_{n=0}^{d_{1}+d_{2}}c_{n}x^{n}{% endequation %}

ועכשיו אפשר להגיד מהו כל מקדם {% equation %}c_{n}{% endequation %} שכזה:

{% equation %}c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %}

עד כאן - חומר לא הכי קל טכנית אבל מאוד בסיסי, הרי משתמשים בפולינומים כמעט בכל מקום במתמטיקה אוניברסיטאית. אבל אפשר להצמיד לו שתי נקודות מבט שהן טיפונת פחות נפוצות:

ראשית, אפשר לחשוב על הפולינומים כאילו הם מקודדים <strong>סדרת מספרים</strong> - סדרת המקדמים שלהם. בצורה הזו, חיבור פולינומים מתורגם לחיבור נקודתי של שתי סדרות, וכפל פולינומים מתורגם לפעולת <strong>קונבולוציה</strong> של הסדרות. חיבור נקודתי אנחנו מכירים, אבל קונבולוציה היא פעולה שיכול לקחת זמן עד שפוגשים אותה בשם הזה לראשונה (אני נתקלתי בה בלימודים רק בסמסטר מתקדם יחסית - וכמובן, באותו סמסטר היא הופיעה שוב ושוב בשלל קורסים שונים ובלתי תלויים; עבורי במקום לומר "אפקט באדר-מיינהוף" אפשר לומר "אפקט הקונבולוציה") אבל הנה, אנחנו רואים שבעצם הכרנו אותה מאז ומעולם, או לפחות מאז שהכרנו כפל פולינומים.

שנית, שתי הפעולות הללו של חיבור וכפל הופכות את הפולינומים <strong>לחוג</strong>. אני לא אניח שהמושג הזה מוכר כאן; לסטודנטים יכול לקחת טיפה זמן עד שהם נתקלים בו לראשונה, למרות החשיבות העצומה שלו למתמטיקה, אבל אני מניח שאנחנו כן מכירים <strong>שדות</strong>, כי כבר באלגברה לינארית מתעסקים איתם. שדות הן קבוצות עם פעולת חיבור וכפל שמתנהגות ממש נחמד - אפילו נחמד <strong>מדי</strong>. למשל, אפשר לחלק בכל איבר. כשעוברים לדבר על <strong>חוג</strong> אנחנו משאירים את הדרישות של ההתנהגות הנחמדה מפעולת החיבור, וממשיכים לדרוש את חוק הפילוג ("דיסטריביוטיביות") אבל מכפל אנחנו דורשים הרבה פחות; שיהיה אסוציאטיבי וזהו בערך. עכשיו, פולינומים דווקא מתנהגים לא רע בכלל - הכפל הוא קומוטטיבי, יש לו יחידה ואי אפשר בטעות לקבל אפס על ידי הכפלה של שני איברים שאינם אפס: זה הופך פולינומים למה שנקרא <strong>תחום שלמות</strong>, שזה משהו שהאבטיפוס שלו הוא המספרים השלמים. כשהמקדמים של הפולינומים הם מעל שדה {% equation %}F{% endequation %} אנחנו מסמנים את חוג הפולינומים המתאים ב-{% equation %}F\left[x\right]{% endequation %}, משתמשים בו לשלל מטרות יפות (למשל, בנייה של שדות שמרחיבים את {% equation %}F{% endequation %}) וכולם מרוצים.

אבל אני לא רוצה לדבר על פולינומים. אני רוצה לדבר על טורי חזקות פורמליים.

מה ההבדל בין פולינומים לטורי חזקות פורמליים? פשוט מאוד. הנה פולינום:

{% equation %}a\left(x\right)=\sum_{n=0}^{d}a_{n}x^{n}{% endequation %}

הנה טור חזקות פורמלי:

{% equation %}a\left(x\right)=\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}

כלומר, במקום סכום של {% equation %}d+1{% endequation %} איברים, יש לנו סכום של אינסוף איברים. לראות סכום כזה מייד מעלה את השאלה הקשה - <strong>למה זה מתכנס</strong>? אבל כשמדברים על "טור חזקות פורמלי" ה"פורמלי" אומר בדיוק שהטור קיים גם בלי לעמוד בדרישות התכנסות כלשהן. זו הנקודה שנשמעת הכי חשודה בסיפור אז בואו נעשה את זה לאט.

בהחלט <strong>יש</strong> משמעות לשאלות התכנסות כשאני לוקח טור כמו {% equation %}\sum_{n=0}^{\infty}\frac{1}{2^{n}}{% endequation %} ושואל מה הסכום שלו. כאן יש לנו סדרה {% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty}{% endequation %}של מספרים ממשיים, {% equation %}a_{n}=\frac{1}{2^{n}}{% endequation %}. אנחנו יודעים לחבר שני מספרים ממשיים, ובאינדוקציה גם שלושה, ארבעה וכן הלאה - כל מספר <strong>סופי</strong> שלהם. אבל להתאים מספר קונקרטי לסכום של <strong>אינסוף</strong> מביניהם - זה כבר דורש טכניקות נוספות, ולא בהכרח תמיד יעבוד. אפשר לכתוב {% equation %}\sum_{n=0}^{\infty}\frac{1}{2^{n}}=2{% endequation %} בעזרת השיטה המקובלת לסכימה של טור אינסופי, אבל היא גם תאלץ אותנו לכתוב {% equation %}\sum_{n=0}^{\infty}2^{n}=\infty{% endequation %}. העניין הוא שבשני המקרים הללו, בין אם הטור מתכנס ובין אם לא, אף אחד לא חושב שיש בעיה עם קיום <strong>הסדרה</strong>: גם הסדרה {% equation %}\left\{ \frac{1}{2^{n}}\right\} _{n=0}^{\infty}{% endequation %} וגם הסדרה {% equation %}\left\{ 2^{n}\right\} _{n=0}^{\infty}{% endequation %} הן אובייקטים שאנחנו לא מערערים על הקיום שלהם, אלא רק תוהים לגבי השאלה האם לאותם אובייקטים אפשר להתאים מספר שיתאר במובן מסויים את הסכום שלהם.

עם טורי חזקות פורמליים זה אותו דבר. אם הסימון {% equation %}\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} מעורר בנו אי נוחות כי אנחנו מצפים, כשאנחנו רואים סכום, שהוא יתכנס למשהו, הרי שלראות את {% equation %}\left(a_{0},a_{1},a_{2},\ldots\right){% endequation %} לא יעורר בנו את אותו סוג של אי נוחות, אבל שני אלו הם פשוט סימונים שונים לאותו דבר. כמו שהרברט וילף כותב ב-generatingfunctionology שלו: פונקציות יוצרות הן חבל כביסה שעליו אנחנו תולים מספרים לתצוגה.

אחרי שאנחנו מוכנים לקבל את <strong>הקיום</strong> של אובייקט כמו {% equation %}a\left(x\right)=\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}, אפשר לעבור לדבר על מה שעושים איתו - ומה שעושים איתו הוא <strong>אלגברה</strong>, כלומר פעולות כמו חיבור וכפל. ראינו את ההגדרה עבור פולינומים; איך היא תשתנה עבור טורי חזקות? ובכן, עבור חיבור היא תהפוך מ-

{% equation %}a\left(x\right)+b\left(x\right)=\sum_{n=0}^{\max\left\{ d_{1},d_{2}\right\} }\left(a_{n}+b_{n}\right)x^{n}{% endequation %}

אל

{% equation %}a\left(x\right)+b\left(x\right)=\sum_{n=0}^{\infty}\left(a_{n}+b_{n}\right)x^{n}{% endequation %}

עבור כפל היא תהפוך מ-

{% equation %}a\left(x\right)\cdot b\left(x\right)=\sum_{n=0}^{d_{1}+d_{2}}c_{n}x^{n}{% endequation %}

אל

{% equation %}a\left(x\right)\cdot b\left(x\right)=\sum_{n=0}^{\infty}c_{n}x^{n}{% endequation %}

כאשר בשני המקרים

{% equation %}c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %}

במילים אחרות, ההגדרה הפכה להיות <strong>אלגנטית יותר</strong> כי לא צריך להסתבך עם הדרגות המעצבנות של הפולינומים. למה זה עובד, למרות שבטור חזקות יש אינסוף איברים? כי גם בהגדרת החיבור וגם בהגדרת הכפל, הערך של כל מקדם הוא סכום <strong>סופי</strong> של איברים. המקדמים הם לא איברים פורמליים בעצמם; הם מספרים ממשיים (או מרוכבים, או איברים בשדה אחר). אז ביטוי כמו {% equation %}a_{n}+b_{n}{% endequation %} הוא סכום של שני מספרים ממשיים, וסכום כזה בוודאי קיים; וביטוי כמו {% equation %}\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %} הוא סכום יותר מורכב אבל עדיין כזה שכולל רק מספר <strong>סופי</strong> של מחוברים. אם היו אינסוף מחוברים, אז היינו בצרות. אבל אנחנו לא בצרות, ובדיוק כמו שעבור הפולינומים קיבלנו חוג שמסומן ב-{% equation %}F\left[x\right]{% endequation %}, גם עבור טורי חזקות קיבלנו חוג, ואפילו תחום שלמות (ואפילו תחום שלמות עם כל מני תכונות אלגבריות נחמדות שלא אכנס אליהן) שמסומן ב-{% equation %}F\left[\left[x\right]\right]{% endequation %}.

<h2>קצת חימום טכני - הטור ההנדסי האינסופי ומספרי פיבונאצ'י</h2>

בואו נראה שתי דוגמאות פשוטות לעבודה עם פונקציות יוצרות. ראשית, ניקח את הסדרה הממש פשוטה {% equation %}a_{n}=1{% endequation %}, כלומר את הפונקציה היוצרת {% equation %}1+x+x^{2}+x^{3}+\ldots{% endequation %}. אם נכפול אותה ב-{% equation %}\left(1-x\right){% endequation %}, שהוא הפונקציה היוצרת {% equation %}\sum_{n=0}^{\infty}b_{n}x^{n}{% endequation %} עם

{% equation %}b_{n}=\begin{cases} 1 & n=0\\ -1 & n=1\\ 0 & n>1 \end{cases}{% endequation %}

{% equation %}\left(1+x+x^{2}+x^{3}+\ldots\right)\left(1-x\right)=\sum_{n=0}^{\infty}c_{n}x^{n}{% endequation %}

כאשר {% equation %}c_{0}=a_{0}b_{0}=1{% endequation %} ו-{% equation %}c_{1}=a_{0}b_{1}+a_{1}b_{0}=b_{1}+b_{0}=0{% endequation %}

ובאופן כללי, בגלל שכל ה-{% equation %}a_{n}{% endequation %}-ים הם 1 אז בעצם {% equation %}\sum_{k=0}^{n}a_{k}b_{n-k}=\sum_{k=0}^{n}b_{n-k}{% endequation %}, ומכיוון שסכום כל ה-{% equation %}b{% endequation %}-ים החל מ-{% equation %}b_{0}{% endequation %} ועד למקום כלשהו הוא סכום של 1, מינוס 1 ועוד אפסים, נקבל {% equation %}c_{n}=0{% endequation %} לכל {% equation %}n>0{% endequation %}. המסקנה היא ש-

{% equation %}\left(1+x+x^{2}+x^{3}+\ldots\right)\left(1-x\right)=1{% endequation %}

במילים אחרות, בחוג {% equation %}F\left[\left[x\right]\right]{% endequation %} האיבר {% equation %}1+x+x^{2}+\ldots{% endequation %} הוא <strong>הפיך</strong> וההופכי שלו הוא {% equation %}\left(1-x\right){% endequation %}. כדי לתאר את זה בצורה שקל לנו לעכל, אוהבים לסמן את זה כך:

{% equation %}1+x+x^{2}+\ldots=\frac{1}{1-x}{% endequation %}

קרוב לודאי שאתם מכירים את השוויון הזה בתור נוסחת הסכום של סדרה הנדסית מתכנסת - אבל כאן הוכחנו את הנכונות שלו בלי שיקולי התכנסות! ה"מחיר" הוא שאי אפשר להציב ערכים ב-{% equation %}x{% endequation %} ולצפות שהשויון יתקיים עבורם; למשל אם נציב {% equation %}x=2{% endequation %} נקבל את הסכום הידוע לשמצה {% equation %}1+2+4+8+\ldots=-1{% endequation %} (שנראה מופרך אבל הוא בעצם לא מופרך בכלל, אם אנחנו לא במספרים הממשיים אלא <a href="https://gadial.net/2014/01/18/sum_of_naturals/">במקום קסום אחר</a>).

בואו נעבור לדוגמא קצת יותר מחוכמת: סדרת פיבונאצ'י. הסדרה הזו מוגדרת על ידי הגדרה רקורסיבית: {% equation %}F_{0}=1,F_{1}=1{% endequation %} ו-{% equation %}F_{n}=F_{n-1}+F_{n-2}{% endequation %}. הגדרה רקורסיבית שכזו נותנת לנו דרך פשוטה לגלות מה הפונקציה היוצרת של הסדרה {% equation %}F_{0},F_{1},F_{2},\ldots{% endequation %}. ראשית כל, נכתוב

{% equation %}F\left(x\right)=\sum_{n=0}^{\infty}F_{n}x^{n}{% endequation %}

עכשיו, היינו רוצים להציב במקום {% equation %}F_{n}{% endequation %} את {% equation %}F_{n}=F_{n-1}+F_{n-2}{% endequation %}, אבל אי אפשר לעשות את זה מיידית, כי עבור {% equation %}n=0,1{% endequation %} הנוסחה הזו לא מתקיימת. אז נפריד את הסכום לשני האיברים הראשונים וכל היתר:

{% equation %}F\left(x\right)=\left(1\cdot x^{0}+1\cdot x^{1}\right)+\sum_{n=2}^{\infty}F_{n}x^{n}=\left(1+x\right)+\sum_{n=2}^{\infty}\left(F_{n-1}+F_{n-2}\right)x^{n}{% endequation %}

{% equation %}=\left(1+x\right)+\sum_{n=2}^{\infty}F_{n-1}x^{n}+\sum_{n=2}^{\infty}F_{n-2}x^{n}{% endequation %}

המטרה שלי היא לנסות לגרום לשני הסכומים הללו להיראות כמו הסכום המקורי שהגדיר את הפונקציה היוצרת של פיבונאצ'י. בואו נסתכל על {% equation %}\sum_{n=2}^{\infty}F_{n-2}x^{n}{% endequation %} קודם - אני יכול לשנות את אינדקס הסכימה. כלל אצבע שקל לזכור הוא - אני יכול <strong>להגדיל</strong> את האינדקס באיזה ערך שאני רוצה (במקרה הנוכחי, 2) בתנאי שאני <strong>מקטין</strong> את הערך ההתחלתי באותה כמות. כלומר: 

{% equation %}\sum_{n=2}^{\infty}F_{n-2}x^{n}=\sum_{n=0}^{\infty}F_{n}x^{n+2}=x^{2}\sum_{n=0}^{\infty}F_{n}x^{n}=x^{2}F\left(x\right){% endequation %}

עבור {% equation %}\sum_{n=2}^{\infty}F_{n-1}x^{n}{% endequation %} זה יהיה טיפה טריקי יותר כי אם אני אגדיל את אינדקס הסכימה ב-1, אני עדיין לא אקבל את {% equation %}F\left(x\right){% endequation %} בסכום, כי:

{% equation %}\sum_{n=2}^{\infty}F_{n-1}x^{n}=\sum_{n=1}^{\infty}F_{n}x^{n+1}=x\sum_{n=1}^{\infty}F_{n}x^{n}{% endequation %}

הסכום פה מתחיל מ-1, לא מ-0. כדי לטפל בזה אני יכול <strong>לחבר ולחסר</strong> את אותו איבר, שבמקרה הנוכחי הוא {% equation %}F_{0}x^{0}=1{% endequation %} (למעשה, בחרתי להתחיל את פיבונאצ'י מ-1 ולא מ-0 כדי להדגים את ההתמודדות עם הקושי הזה). כלומר, אני אכתוב

{% equation %}x\sum_{n=1}^{\infty}F_{n}x^{n}=x\left(\sum_{n=0}^{\infty}F_{n}x^{n}-1\right)=xF\left(x\right)-x{% endequation %}

ולכן מכל זה קיבלנו

{% equation %}F\left(x\right)=\left(1+x\right)+x^{2}F\left(x\right)+xF\left(x\right)-x=\left(x^{2}+x\right)F\left(x\right)+1{% endequation %}

עכשיו אפשר להעביר את {% equation %}F\left(x\right){% endequation %} אגף ולהוציא גורם משותף - אלו פעולות תקינות בכל חוג. נקבל:

{% equation %}F\left(x\right)\left(1-x^{2}-x\right)=1{% endequation %}

מה שהייתי רוצה לעשות עכשיו הוא <strong>לחלק</strong> ב-{% equation %}1-x^{2}-x{% endequation %}. האם מותר לי? כבר ראיתי שאפשר לחלק ב-{% equation %}\left(1-x\right){% endequation %}, אבל מה עם דברים מורכבים יותר? תכף אני אוכיח שכל עוד המקדם החופשי הפיך, תמיד אפשר לחלק, אז התוצאה היא שאני יכול לכתוב

{% equation %}F\left(x\right)=\frac{1}{1-x^{2}-x}{% endequation %}

וזו הפונקציה היוצרת של מספרי פיבונאצ'י (כשהם מתחילים מ-1 ולא מ-0). בשביל מה זה היה טוב? מה אפשר לעשות איתה שלא יכלנו לעשות בלעדיה? זה סיפור אחר - אפשר למשל לקבל ממנה את הנוסחה הסגורה למספרי פיבונאצ'י, או הערכות אסימפטוטיות על קצב הגידול שלה; כל זה מצריך לקחת את הפונקציה היוצרת ולזרוק עליה כלים סטנדרטיים שיודעים לטפל באנליזה של פונקציות רציונליות. הדגש פה הוא על <strong>סטנדרטיים</strong> - זו הסיבה שמתמטיקאים אוהבים פונקציות יוצרות, זו דרך קומפקטית לייצר סדרות, שאחר כך אפשר להשתמש עליה בכל המתמטיקה שאנחנו מכירים.

כדי לסיים את החלק הזה אני צריך להוכיח את מה שטענתי קודם: ש-{% equation %}a\left(x\right)=\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %} הוא הפיך אם ורק אם {% equation %}a_{0}{% endequation %} הפיך. הרעיון בבסיסו הוא אותו רעיון כמו ההיפוך של {% equation %}1+x+x^{2}+\ldots{% endequation %} רק שהפעם במקום לזרוק מהשמיים את ההופכי אני אסביר איך מוצאים אותו.

אם קיים הופכי, {% equation %}b\left(x\right)=\sum_{n=0}^{\infty}b_{n}x^{n}{% endequation %}, מה המקדמים שלו <strong>חייבים</strong> להיות? אנחנו יודעים ש-{% equation %}a\left(x\right)b\left(x\right)=1{% endequation %} (כי זו ההגדרה של הופכי), כלומר אם נכתוב {% equation %}a\left(x\right)\cdot b\left(x\right)=\sum_{n=0}^{\infty}c_{n}x^{n}{% endequation %} אז {% equation %}c_{0}=1{% endequation %} ו-{% equation %}c_{n}=0{% endequation %} לכל {% equation %}n>0{% endequation %}.

מהשוויון הראשון אנחנו מקבלים {% equation %}a_{0}b_{0}=1{% endequation %}. כלומר, אם {% equation %}a\left(x\right){% endequation %} היה הפיך אז השוויון הזה מראה לנו ש-{% equation %}a_{0}{% endequation %} הפיך ו-{% equation %}b_{0}{% endequation %} הוא ההופכי שלו; זה כיוון אחד של ההוכחה. הכיוון המורכב יותר הוא להניח ש-{% equation %}a_{0}{% endequation %} הפיך ולכן באמת קיים לו הופכי {% equation %}b_{0}{% endequation %}, וזה נותן לנו את <strong>ההתחלה</strong> של הבניה של {% equation %}b\left(x\right){% endequation %}, אבל צריך להראות שאפשר לבנות גם את יתר המקדמים.

למרבה המזל, יתר המקדמים מתקבלים מאליהם, בדרך אינדוקטיבית. נניח שכבר ידועים לנו המקדמים {% equation %}b_{0},\ldots,b_{n-1}{% endequation %} ונבנה את {% equation %}b_{n}{% endequation %}. מכיוון ש-{% equation %}n>0{% endequation %} אז {% equation %}c_{n}=0{% endequation %} ולכן השוויון {% equation %}c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %} שמגדיר את המקדם במכפלה נותן לנו:

{% equation %}0=\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %}

כלומר

{% equation %}a_{0}b_{n}=-\sum_{k=1}^{n}a_{k}b_{n-k}{% endequation %}

עכשיו, אמרנו כבר ש-{% equation %}a_{0}{% endequation %} הפיך, אז אפשר לחלק בו - כלומר, לכפול ב-{% equation %}b_{0}{% endequation %}, ולקבל:

{% equation %}b_{n}=-b_{0}\sum_{k=1}^{n}a_{k}b_{n-k}{% endequation %}

אגף ימין מורכב כולו מפעולת <strong>חוקיות</strong> בחוג {% equation %}F{% endequation %} שמעליו אנחנו מגדירים את {% equation %}F\left[\left[x\right]\right]{% endequation %}, כך שהבניה עובדת וזה מסיים את ההוכחה! לא רק שהוכחנו ש-{% equation %}a\left(x\right){% endequation %} הפיך, גם עשינו את זה בדרך קונסטרוקטיבית שמוצאת את ההופכי שלו. 

<h2>הפונקציה היוצרת של מספרי קטלן</h2>

עד כאן, הכל טוב, אז בואו נתמודד עם האתגר המרכזי שלנו - מציאת הפונקציה היוצרת של מספרי קטלן.

יש כמה דרכים להגיע אל הפונקציה היוצרת של מספרי קטלן, ואחת הפשוטות שבהן היא להניח שכבר מצאנו את נוסחת הנסיגה שלהם, שראינו בפוסט הקודם: {% equation %}C_{n+1}=\sum_{k=0}^{n}C_{k}C_{n-k}{% endequation %}, עם תנאי ההתחלה {% equation %}C_{0}=1{% endequation %}. הנוסחה הזו גם מזכירה קצת את זו של פיבונאצ'י ולכן הטכניקה שבה השתמשנו עבור פיבונאצ'י נראית מבטיחה כאן - אבל אפילו עוד יותר מכך, הנוסחה הזו מזכירה את איך שמכפלת פולינומים עובדת: {% equation %}c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}{% endequation %}. רק הקטע הזה עם ה-{% equation %}n+1{% endequation %} טיפה שונה. בואו נראה איך זה יסתדר לנו.

נתחיל עם להגדיר את הפונקציה היוצרת: {% equation %}C\left(x\right)=\sum_{n=0}^{\infty}C_{n}x^{n}{% endequation %}. עכשיו, בואו נכפיל את {% equation %}C\left(x\right){% endequation %} <strong>בעצמה</strong> כדי לנסות לקבל משהו שנראה כמו הנוסחה למכפלת פולינומים. אני אסמן את ההכפלה של {% equation %}C\left(x\right){% endequation %} בעצמה ב-{% equation %}C\left(x\right)^{2}{% endequation %} - גם זה סימון סטנדרטי לגמרי בחוגים באופן כללי, ואני מקפיד על הפדנטיות הזו רק כי עוד רגע יגיעו דברים לא לגמרי סטנדרטיים.

{% equation %}C\left(x\right)^{2}=\sum_{n=0}^{\infty}A_{n}x^{n}{% endequation %}

כאשר

{% equation %}A_{n}=\sum_{k=0}^{n}C_{k}C_{n-k}{% endequation %}

זה מה שנובע מהנוסחה למכפלת פולינומים. אבל בנוסף לכך אנחנו מכירים את נוסחת הנסיגה של קטלן, {% equation %}C_{n+1}=\sum_{k=0}^{n}C_{k}C_{n-k}{% endequation %}, ולכן משילוב של שתיהן אנחנו מקבלים ש-

{% equation %}A_{n}=C_{n+1}{% endequation %}

כלומר

{% equation %}C\left(x\right)^{2}=\sum_{n=0}^{\infty}C_{n+1}x^{n}{% endequation %}

הייתי רוצה להשתמש באותו טריק כמו פיבונאצ'י כדי להמיר את אגף ימין ל-{% equation %}C\left(x\right){% endequation %}, אבל יש לי כאן בעיה. קודם, בפיבונאצ'י, הסכימה התחילה ממשהו גדול מ-0, והמקדם בפנים היה בעל אינדקס קטן מ-{% equation %}n{% endequation %}, ולכן היה קל לתקן את זה - הגדלנו את האינדקס, הקטנו את הערך ההתחלתי. כאן, לעומת זאת, הסכימה מתחילה מ-0, כלומר מהערך הנכון, והאינדקס הוא גדול מ-{% equation %}n{% endequation %}. אז נעשה משהו טיפה שונה: קודם כל נכפול את שני האגפים ב-{% equation %}x{% endequation %} (פעולה מותרת בחוג), ונקבל

{% equation %}xC\left(x\right)^{2}=\sum_{n=0}^{\infty}C_{n+1}x^{n+1}=\sum_{n=1}^{\infty}C_{n}x^{n}=\sum_{n=0}^{\infty}C_{n}x^{n}-C_{0}=C\left(x\right)-1{% endequation %}

אחרי העברת אגפים נקבל

{% equation %}xC\left(x\right)^{2}-C\left(x\right)+1=0{% endequation %}

וזו... משוואה ריבועית? עכשיו אפשר לנפנף ממש מהר בידיים כמו שחלק מהספרים עושים: להגיד שנוסחת השורשים מלמדת אותנו ש-{% equation %}C\left(x\right)=\frac{1\pm\sqrt{1-4x}}{2x}{% endequation %} ושהפתרון ה"נכון" מבין השניים הוא זה עם המינוס, כי אם נסתכל על {% equation %}\frac{1+\sqrt{1-4x}}{2x}{% endequation %} נראה שכש-{% equation %}x{% endequation %} שואף ל-0 המונה שואף ל-2 ולכן הביטוי שואף לאינסוף למרות שהוא אמור לשאוף ל-{% equation %}C_{0}=1{% endequation %} ולעומת זאת עבור {% equation %}\frac{1-\sqrt{1-4x}}{2x}{% endequation %} קל לראות שזה עובד עם כלל לופיטל, וסיימנו! גילינו את הנוסחה לפונקציה היוצרת של מספרי קטלן, {% equation %}C\left(x\right)=\frac{1-\sqrt{1-4x}}{2x}{% endequation %}. זהו, אפשר לסגור את הפוסט.

<h2>אפשר לסגור את הפוסט, או שלא</h2>

אוקיי, בואו לא נסגור עדיין את הפוסט.

חשוב לי להדגיש שכל מה שראינו פה הוא <strong>נכון</strong>. זה למעשה מה שאוילר עשה במכתב הראשון שבו הוא סיפר לגולדבך על מספרי קטלן. אבל בבירור לא עשיתי את זה ברמת הפורמליות שבה התייחסתי לטורי חזקות פורמליים בכל יתר הפוסט, ומה שעוד יותר גרוע - פתאום ברגע האחרון עירבתי מושגים מאנליזה ודיברתי על להשאיף את {% equation %}x{% endequation %} לאפס ועל כלל לופיטל... זה בלאגן שלם. לכן אני רוצה להקדיש את החלק הזה של הפוסט, שיהיה יותר מורכב מתמטית ממה שעשינו עד עכשיו, כדי להסביר למה הכל בסדר.

הרגע האחרון שבו הכל היה באמת בסדר פורמלית היה כשקיבלתי את המשוואה {% equation %}xC\left(x\right)^{2}-C\left(x\right)+1=0{% endequation %}. הדבר הבא שעשיתי היה להזכיר את <strong>נוסחת השורשים</strong>. נוסחת השורשים היא הכלי הסטנדרטי שלנו לפתרון משוואה ריבועית, והיא נכונה בהרבה סיטואציות, לא רק במספרים הממשיים והמרוכבים. בואו נראה את זה: אני נמצא בחוג {% equation %}R{% endequation %} כלשהו, עם איברים {% equation %}a,b,c\in R{% endequation %}, ואני מחפש ערך של {% equation %}x\in R{% endequation %} שמקיים

{% equation %}ax^{2}+bx+c=0{% endequation %}

<a href="https://gadial.net/2023/12/16/quadratic_equations/">יש לי פוסט</a> שמסביר מה עושים עכשיו, אבל אני אתן פה תיאור טיפה שונה. ראשית, נכפול את שני אגפי המשוואה ב-{% equation %}4a{% endequation %} ונקבל

{% equation %}4a^{2}x^{2}+4abx+4ac=0{% endequation %}

זה עדיין מתקיים בכל חוג {% equation %}R{% endequation %}. עכשיו, נסתכל על הביטוי {% equation %}\Delta=b^{2}-4ac{% endequation %} ("הדיסקרימיננטה"). גם הביטוי הזה - קיים בכל חוג {% equation %}R{% endequation %}. נחבר אותו לשני האגפים ונקבל

{% equation %}4a^{2}x^{2}+4abx+b^{2}=\Delta{% endequation %}

עכשיו אגף שמאל נראה בדיוק כמו משהו בריבוע: {% equation %}4a^{2}x^{2}+4abx+b^{2}=\left(2ax+b\right)^{2}{% endequation %}. <strong>גם זה עדיין נכון בכל חוג</strong>. כלומר, קיבלנו

{% equation %}\left(2ax+b\right)^{2}=\Delta{% endequation %}

עכשיו מגיע המעבר ה"בעייתי":

{% equation %}2ax+b=\pm\sqrt{\Delta}{% endequation %}

המעבר הזה בעייתי לא רק בגלל שאנחנו בחוג כללי - אפילו אם היינו עובדים מעל הממשיים, {% equation %}\mathbb{R}{% endequation %}, הוא עדיין היה בעייתי אם {% equation %}\Delta{% endequation %} היה שלילי. אז במקום לראות אותו כ"בעייתי" אפשר לחשוב על זה כאילו אנחנו מוסיפים הנחה: אנחנו אומרים - <strong>נניח</strong> שקיים {% equation %}\alpha\in R{% endequation %} כך ש-{% equation %}\alpha^{2}=\Delta{% endequation %}, אז במקרה הזה אפשר לכתוב {% equation %}\left(2ax+b\right)^{2}=\alpha^{2}{% endequation %}. אבל האם עכשיו אפשר להסיק ש-{% equation %}2ax+b=\pm\alpha{% endequation %}? ובכן, לא.

בואו נראה דוגמא: החוג {% equation %}R=\mathbb{Z}_{8}=\left\{ 0,1,\ldots,7\right\} {% endequation %} עם חיבור וכפל מודולו 8. בחוג הזה מתקיים ש-{% equation %}1^{2}=3^{2}=5^{2}=7^{2}=1{% endequation %}, ולכן אם {% equation %}x^{2}=y^{2}{% endequation %} זה לא אומר ש-{% equation %}x=\pm y{% endequation %} כי למשל מה אם {% equation %}y=1{% endequation %} ואילו {% equation %}x=3{% endequation %}?

אז אילו תנאים צריך לדרוש מהחוג שלנו כדי ש-{% equation %}x^{2}=y^{2}{% endequation %} יגרור {% equation %}x=\pm y{% endequation %}? בואו ננסה להוכיח את זה ונראה את התנאים צצים בדרך.

נתחיל עם {% equation %}x^{2}=y^{2}{% endequation %}. נעביר את {% equation %}y{% endequation %} אגף (לא דורש כלום) ונקבל {% equation %}x^{2}-y^{2}=0{% endequation %}, שאפשר לכתוב גם בתור {% equation %}\left(x-y\right)\left(x+y\right)=0{% endequation %}. הופס, הוספנו דרישה! רואים מה היא? השתמשתי בדיסטריביוטיביות, אבל זה לא העניין כאן אלא זה שאם נפתח את הסוגריים, נקבל

{% equation %}\left(x-y\right)\left(x+y\right)=x^{2}-yx+xy-y^{2}{% endequation %}

כלומר, אני הנחתי ש-{% equation %}xy=yx{% endequation %} וזה קורה באופן כללי רק אם החוג <strong>קומוטטיבי</strong>. אבל אוקיי, {% equation %}R\left[\left[x\right]\right]{% endequation %} שלנו הוא קומוטטיבי אם {% equation %}R{% endequation %} עצמו הוא קומוטטיבי (ואצלנו {% equation %}R{% endequation %} הוא הממשיים/המרוכבים). אז בינתיים זו דרישה קלילה יחסית (אבל שמראה יפה כמה חוגים לא קומוטטיביים - למשל חוגי מטריצות - הם עולמות משוגעים בפני עצמם).

עכשיו, קיבלתי {% equation %}\left(x-y\right)\left(x+y\right)=0{% endequation %}, כלומר יש לי מכפלה של שני איברים ששווה אפס. האם בכלל ייתכן שמכפלה של שני איברים תיתן אפס למרות ששניהם שונים מאפס? זה לא משהו שיש באינטואיציה המתמטית היומימית שלנו כי זה לא קורה בשלמים והרחבותיהם, אבל זה <strong>כן</strong> קורה ב-{% equation %}\mathbb{Z}_{8}{% endequation %} שהבאתי כאן בתור דוגמה, למשל {% equation %}2\cdot4=0{% endequation %}. לכן בתורת החוגים יש מונחים סטנדרטיים לסיפור הזה: אנחנו אומרים ש-{% equation %}a,b{% endequation %} הם <strong>מחלקי אפס</strong> אם {% equation %}ab=0{% endequation %} למרות ש-{% equation %}a,b\ne0{% endequation %}, וקוראים לחוג (קומוטטיבי בד"כ) בלי מחלקי אפס <strong>תחום שלמות</strong>. בתחומי שלמות, ש-{% equation %}\mathbb{Z}{% endequation %} הוא מעין אבטיפוס שלהם, אפשר לבצע "צמצום": אם {% equation %}ax=ay{% endequation %} אז {% equation %}x=y{% endequation %} זו הדוגמא הפשוטה, אבל גם {% equation %}x^{2}=y^{2}{% endequation %} גורר {% equation %}x=\pm y{% endequation %} הוא דוגמא לצמצום, ואנחנו מקבלים אותו כי אם יש לנו {% equation %}\left(x-y\right)\left(x+y\right)=0{% endequation %} בתחום שלמות, או ש-{% equation %}x-y=0{% endequation %} או ש-{% equation %}x+y=0{% endequation %}, אין אפשרות אחרת.

למרבה השמחה, {% equation %}R\left[\left[x\right]\right]{% endequation %} הוא תחום שלמות אם {% equation %}R{% endequation %} הוא תחום שלמות, כי אם {% equation %}a\left(x\right)b\left(x\right)=0{% endequation %} אז בפרט {% equation %}a_{0}b_{0}=0{% endequation %} ואם אנחנו מעל תחום שלמות אז בלי הגבלת הכלליות, {% equation %}b_{0}=0{% endequation %}. עכשיו, {% equation %}a_{0}b_{1}+a_{1}b_{0}=0{% endequation %}, כלומר {% equation %}a_{0}b_{1}=0{% endequation %} ונקבל שגם {% equation %}b_{1}=0{% endequation %} וכן הלאה באינדוקציה.

אם כן, חזרה למשוואות ריבועיות: מה שראינו הוא שמעל תחום שלמות, <strong>אם</strong> קיים {% equation %}\alpha{% endequation %} כך ש-{% equation %}\alpha^{2}=\Delta{% endequation %} אז אפשר לומר {% equation %}2ax+b=\pm\alpha{% endequation %}. עכשיו אפשר להעביר אגף ולקבל 

{% equation %}2ax=-b\pm\alpha{% endequation %}

כדי להתקדם מכאן, אנחנו צריכים שאפשר יהיה לחלק ב-{% equation %}2a{% endequation %} וזה כמובן לא נכון בכל חוג, אפילו לא בתחום שלמות, זה הרי לא נכון אפילו ב-{% equation %}\mathbb{Z}{% endequation %}. אבל אם אפשר לחלק ב-{% equation %}2a{% endequation %} - כלומר, אם {% equation %}2a{% endequation %} הוא <strong>הפיך</strong> בחוג שלנו - אז נקבל 

{% equation %}x=\frac{-b\pm\alpha}{2a}{% endequation %}

וכדי לא לכתוב {% equation %}\alpha{% endequation %} מעדיפים לכתוב

{% equation %}x=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}{% endequation %}

מתוך הבנה ש-{% equation %}\sqrt{b^{2}-4ac}{% endequation %} הוא <strong>סימון</strong> שאומר "איבר בחוג שכשמעלים אותו בריבוע מקבלים {% equation %}b^{2}-4ac{% endequation %}, בהנחה שקיים כזה".

זה האופן שבו צריך לקרוא את המשוואה {% equation %}C\left(x\right)=\frac{1\pm\sqrt{1-4x}}{2x}{% endequation %} שקיבלנו עבור מספרי קטלן. מה שהיא אומרת, ברמה הפורמלית ביותר, הוא "אם קיים טור חזקות פורמלי {% equation %}a\left(x\right){% endequation %} כך ש-{% equation %}a\left(x\right)^{2}=1-4x{% endequation %}, אז {% equation %}C\left(x\right){% endequation %} הוא או {% equation %}\frac{1+a\left(x\right)}{2x}{% endequation %} או {% equation %}\frac{1-a\left(x\right)}{2x}{% endequation %}, אנחנו לא סגורים על איזה משניהם נכון".

אבל רגע, לא סיימנו! צריך להצדיק גם את החלוקה ב-{% equation %}2x{% endequation %}. להצדיק חלוקה ב-{% equation %}2{% endequation %} זה קל, הרי {% equation %}2{% endequation %} הוא הפיך. אבל לחלק ב-{% equation %}2x{% endequation %}? הרי לפני רגע אמרתי שטור חזקות הוא הפיך אם ורק אם האיבר החופשי שלו הוא הפיך, וב-{% equation %}2x{% endequation %}, כשאני חושב עליו בתור טור חזקות, האיבר החופשי הוא 0, כלומר לא הפיך. <strong>אופס</strong>.

העניין הוא שכן אפשר סוג של "לחלק" ב-{% equation %}x{% endequation %}. לפעמים. הנה דוגמא לאיך זה עובד. נניח ש-{% equation %}a\left(x\right)=a_{1}x+a_{2}x^{2}+\ldots{% endequation %}, כלומר יש לנו טור חזקות שהמקדם החופשי שלו הוא 0. אז אפשר <strong>להוציא החוצה</strong> את {% equation %}x{% endequation %} ולקבל {% equation %}a\left(x\right)=x\left(a_{1}+a_{2}x+\ldots\right){% endequation %} ואז אפשר לכתוב {% equation %}a_{1}+a_{2}x+\ldots=\frac{a\left(x\right)}{x}{% endequation %}. כלומר, את הפעולה "חלוקה ב-{% equation %}x{% endequation %}" אפשר לראות בתור "הזזה שמאלה של כל האיברים בסדרה שמתחילה ב-0" - אם היה לנו את הסדרה {% equation %}\left(0,a_{1},a_{2},\ldots\right){% endequation %} אחרי ביצוע הפעולה הזו קיבלנו את הסדרה {% equation %}\left(a_{1},a_{2},\ldots\right){% endequation %}.

עוד יותר פורמלית, מה שאנחנו רואים במשוואה {% equation %}C\left(x\right)=\frac{1\pm a\left(x\right)}{2x}{% endequation %} הוא בעצם את {% equation %}2xC\left(x\right)=1\pm a\left(x\right)^{2}{% endequation %}. אם נגלה שיש {% equation %}a\left(x\right){% endequation %} כך ש-{% equation %}1-a\left(x\right)=x\cdot b\left(x\right){% endequation %} כלשהו, אז נוכל לכתוב {% equation %}2xC\left(x\right)=xb\left(x\right){% endequation %} ואז נוכל <strong>לצמצם</strong> ב-{% equation %}x{% endequation %}, כי אנחנו בתחום שלמות, ולקבל {% equation %}2C\left(x\right)=b\left(x\right){% endequation %}, כלומר {% equation %}C\left(x\right)=\frac{b\left(x\right)}{2}{% endequation %}. זה התוכן הפורמלי של הכתיב {% equation %}C\left(x\right)=\frac{1-\sqrt{1-4x}}{2x}{% endequation %}.

העניין הזה גם מסביר לנו למה אנחנו בוחרים מינוס ולא פלוס, גם בלי שנזדקק ישירות להסברים אנליטיים: אם קיים {% equation %}a\left(x\right){% endequation %} כך ש-{% equation %}a\left(x\right)^{2}=1-4x{% endequation %}, אז המקדם החופשי שלו מקיים {% equation %}a_{0}^{2}=1{% endequation %} (כי {% equation %}1{% endequation %} הוא המקדם החופשי של המכפלה, {% equation %}1-4x{% endequation %}) ובגלל שאנחנו בתחום שלמות, {% equation %}a_{0}=\pm1{% endequation %}. כשמשתמשים בסימן {% equation %}\sqrt{\cdot}{% endequation %} עבור מספרים ממשיים הכוונה היא תמיד ללקיחת השורש החיובי, אז גם כאן נוכל להשתמש במוסכמה שלוקחים את ה-{% equation %}a\left(x\right){% endequation %} עם המקדם החופשי {% equation %}a_{0}=1{% endequation %}. עכשיו, אם אנחנו רוצים שהביטוי {% equation %}\frac{1\pm a\left(x\right)}{2x}{% endequation %} יהיה מוגדר היטב, צריך שהמקדם החופשי של {% equation %}1\pm a\left(x\right){% endequation %} יהיה 0, וזה יעבוד עבור חיסור ולא יעבוד עבור חיבור.

כמובן, עדיין נותרה לנו שאלה אחת: <strong>למה</strong> אנחנו יודעים ש-{% equation %}\sqrt{1-4x}{% endequation %} קיים בכלל? אני יכול לכתוב {% equation %}a\left(x\right)^{2}=1-4x{% endequation %} ולנסות לפתור את המשוואה ולחלץ את המקדמים של {% equation %}a\left(x\right){% endequation %}, כמו שעשיתי עבור הופכי. אבל אני יכול גם לחפור יותר עמוק...

<h2>חופרים יותר עמוק</h2>

אני מניח שאנחנו מכירים את הבינום של ניוטון, ואם לא - <a href="https://gadial.net/2010/06/22/newton_binom/">יש לי על זה פוסט</a>. זו הנוסחה החביבה

{% equation %}\left(a+b\right)^{n}=\sum_{k=0}^{n}{n \choose k}a^{k}b^{n-k}{% endequation %}

שנכונה לכל {% equation %}n{% endequation %} טבעי ו-{% equation %}a,b{% endequation %} כלשהם, אפילו איברים בחוג <strong>קומוטטיבי</strong> כללי.

זו נוסחה שימושית ונהדרת עם הוכחה קומבינטורית מקסימה וכל זה מתואר בפוסט שלי. אני רוצה לדבר הפעם על <strong>ההכללה</strong> שלה: מה קורה אם אנחנו רוצים ש-{% equation %}n{% endequation %} לא יהיה מספר טבעי דווקא, אלא מספר ממשי כללי? ובכן, ניוטון דאג גם לזה, ובאמצעות חדו"א אפשר להוכיח את הנוסחה

{% equation %}\left(a+b\right)^{r}=\sum_{k=0}^{\infty}{r \choose k}a^{k}b^{r-k}{% endequation %}

כאשר {% equation %}r\in\mathbb{R}{% endequation %} הוא מספר ממשי כללי, והסימון {% equation %}{r \choose k}{% endequation %} מוגדר בתור

{% equation %}{r \choose k}=\frac{r\left(r-1\right)\left(r-2\right)\cdots\left(r-k+1\right)}{k!}{% endequation %}

זו ממש הכללה ישירה של הבינום הרגיל של ניוטון, שבו {% equation %}{n \choose k}=\frac{n!}{k!\left(n-k!\right)}=\frac{n\left(n-1\right)\left(n-2\right)\cdots\left(n-k+1\right)}{k!}{% endequation %}. העניין הוא שאם {% equation %}n{% endequation %} הוא מספר טבעי, ואם {% equation %}k>n{% endequation %}, אז נקבל {% equation %}{n \choose k}=0{% endequation %} כי במכפלה {% equation %}\left(n-1\right)\ldots\left(n-k+1\right){% endequation %} יופיע מתישהו {% equation %}\left(n-n\right){% endequation %}, כלומר כל המכפלה הזו מוכפלת ב-0 ושווה ל-0 ולכן אנחנו מקבלים ש-{% equation %}\left(a+b\right)^{n}{% endequation %} הוא לא סכום אינסופי אלא סופי (ליתר דיוק - הוא סכום אינסופי שכל אבריו הם 0 החל ממקום מסויים).

אם לעומת זאת {% equation %}r{% endequation %} הוא לא מספר טבעי, אז {% equation %}\left(r-r\right){% endequation %} לא יופיע במכפלה ולכן היא אף פעם לא תתאפס. לכן צריך לעבור לסכום אינסופי ולקוות ממש חזק שהוא יתכנס.

בואו נראה דוגמא. נניח ש- {% equation %}a=-4x{% endequation %} ו-{% equation %}b=1{% endequation %} ו-{% equation %}r=\frac{1}{2}{% endequation %}, אז נקבל

{% equation %}\sqrt{1-4x}=\left(-4x+1\right)^{\frac{1}{2}}=\sum_{k=0}^{\infty}{1/2 \choose k}\left(-4x\right)^{k}=\sum_{k=0}^{\infty}\left(-4\right)^{k}{1/2 \choose k}x^{k}{% endequation %}

הנוסחה הזו מאפשר חישוב פשוט של המקדמים של {% equation %}x^{k}{% endequation %} עבור הערכים הראשונים של {% equation %}k{% endequation %} (אני מציע לכם לנסות לחשב בעצמכם, גם אני "מרגיש" את הביטוי רק כשאני עושה את זה):

<ul> <li>{% equation %}\left(-4\right)^{0}{1/2 \choose 0}=1\cdot1=1{% endequation %}</li>


<li>{% equation %}\left(-4\right)^{1}{1/2 \choose 1}=-4\cdot\frac{1}{2}=-2{% endequation %}</li>


<li>{% equation %}\left(-4\right)^{2}{1/2 \choose 2}=16\cdot\frac{1}{2}\cdot\frac{1}{2}\cdot\left(-\frac{1}{2}\right)=-2{% endequation %}</li>


<li>{% equation %}\left(-4\right)^{3}{1/2 \choose 3}=-64\cdot\frac{1}{2\cdot3}\cdot\frac{1}{2}\cdot\left(-\frac{1}{2}\right)\cdot\left(-\frac{3}{2}\right)=-4{% endequation %}</li>

</ul>

מכאן כבר יש לי מספיק אומץ לנסות לכתוב את הביטוי הכללי:

{% equation %}\left(-4\right)^{n}{1/2 \choose n}=\left(-1\right)^{n}2^{n}\cdot2^{n}\cdot\frac{1}{2\cdot3\cdots n}\cdot\frac{1}{2}\cdot\left(-\frac{1}{2}\right)\cdot\left(-\frac{3}{2}\right)\cdots\left(-\frac{2n-3}{2}\right){% endequation %}

{% equation %}=2^{n}\cdot\frac{3\cdot5\cdots\left(2n-3\right)}{2\cdot3\cdots n}=\frac{6\cdot10\cdots\left(4n-6\right)}{2\cdot3\cdots n}{% endequation %}

מה שנותן לנו, אם נציב ערכים קונקרטיים:

{% equation %}\sqrt{1-4x}=1-2x-2x^{2}-4x^{3}-10x^{4}-28x^{5}-84x^{6}-\ldots{% endequation %}

זה כמובן מזכיר את סדרת מספרי קטלן, {% equation %}1,1,2,5,14,42,\ldots{% endequation %}, ולא במקרה: הנוסחה שקיבלנו הייתה {% equation %}C\left(x\right)=\frac{1-\sqrt{1-4x}}{2x}{% endequation %}, כך שמספרי קטלן מתקבלים מ-{% equation %}\sqrt{1-4x}{% endequation %} באופן הבא:

<ol> <li>החליפו את ה-1 שבהתחלה ב-0, והסירו את סימני המינוס (זה החלק של {% equation %}1-{% endequation %} השורש)</li>


<li>הזיזו את הסדרה צעד אחד שמאלה כך שה-0 בהתחלה נעלם (זה החלק של החלוקה ב-{% equation %}x{% endequation %})</li>


<li>חלקו את אברי כל הסדרה ב-2 (זו החלוקה ב-2).</li>

</ol>

במילים אחרות - כן! הבינום המוכלל של ניוטון עובד ונותן לנו את מספרי קטלן! ככה <strong>בדיוק</strong> אוילר גילה את הנוסחה הסגורה למספרי קטלן. לא על ידי תעלול קומבינטורי מרהיב כמו שהראיתי בפוסט הקודם, אלא על ידי "הא, מצאתי את הפונקציה היוצרת, עכשיו בוא ניקח את המתמטיקה הסטנדרטית שלנו ונפעיל אותה על הפונקציה כדי לקבל את סדרת המקדמים".

זה השלב שבו כולם מרוצים... חוץ ממני. כל הקטע הזה של הבינום המוכלל של ניוטון? זו התעסקות בטורי חזקות של חדו"א, לא בטורי חזקות פורמליים. זה לא אומר שזה לא תקין - אפשר בהחלט לומר שזו תוצאה שתקפה רק בתחום ההתכנסות של הטור, אבל זה מספיק כדי לקבל את סדרת המקדמים - אבל אני רוצה לראות כמה רחוק אפשר ללכת כשדבקים <strong>רק</strong> בפורמליות, בלי חדו"א בכלל. עכשיו יש לנו מטרה הרבה יותר ברורה: אנחנו לא רוצים להבין "סתם" איך להתעסק במספרי קטלן פורמלית, אלא איך אפשר להוכיח את <strong>הבינום המוכלל של ניוטון</strong> פורמלית.

<h2>הבינום הפורמלי המוכלל של ניוטון</h2>

נשמור על העניין פשוט ונסתכל על הבינום של ניוטון כשאחד המחוברים הוא 1. כלומר, על הנוסחה

{% equation %}\left(1+x\right)^{r}=\sum_{n=0}^{\infty}{r \choose n}x^{n}{% endequation %}

מה שיש לנו באגף ימין כאן הוא פונקציה יוצרת - הפונקציה היוצרת של הסדרה {% equation %}a_{n}={r \choose n}{% endequation %}. באגף שמאל יש לנו ביטוי שאין לו משמעות פורמלית - לא הגדרנו בשום שלב העלאה בחזקה כללית של פולינומים, או של טורי חזקות. אז אני יכול <strong>להגדיר</strong> את המשמעות של אגף שמאל להיות מה שכתוב באגף ימין; השאלה המעניינת היא האם ההגדרה הזו תסכים עם מה שאנחנו מצפים שיהיה, כלומר אם עבור {% equation %}r{% endequation %} שהוא <strong>מספר טבעי</strong> ההגדרה תתלכד עם ההגדרה הרגילה, ואם יישמרו חוקי החשבון הרגילים של חזקות, שהם מה שעומד מאחורי הרחבת הגדרת החזקה מטבעיים למספרים ממשיים באופן כללי. כלומר, האם יתקיים

{% equation %}\left(1+x\right)^{r}\cdot\left(1+x\right)^{s}=\left(1+x\right)^{r+s}{% endequation %}

ו-{% equation %}\left(\left(1+x\right)^{r}\right)^{s}=\left(1+x\right)^{rs}{% endequation %}

אבל כבר כאן צצה בעיה: הביטוי {% equation %}\left(\left(1+x\right)^{r}\right)^{s}{% endequation %} הוא לא מוגדר היטב, כי הרי {% equation %}\left(1+x\right)^{r}{% endequation %} הוא כבר פונקציה יוצרת עם אינסוף מחוברים, ולא הגדרתי העלאה בחזקה <strong>שלה</strong>, רק של הביטוי הפשוט {% equation %}1+x{% endequation %}. אז אני צריך מראש ללכת על הגדרה כללית יותר. מה בדבר...

{% equation %}\left(1+F\left(x\right)\right)^{r}=\sum_{n=0}^{\infty}{r \choose n}F\left(x\right)^{n}{% endequation %}

כאשר {% equation %}F\left(x\right){% endequation %} היא פונקציה יוצרת כלשהי? ובכן, זה <strong>כמעט</strong> עובד, אבל בואו ננצל את ההזדמנות כדי להציג גם את הדבר הזה בהקשר טיפה יותר כללי: <strong>הרכבה</strong> של פונקציות יוצרות.

אז נניח שיש לנו שתי פונקציות יוצרות

{% equation %}a\left(x\right)=\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}

{% equation %}b\left(x\right)=\sum_{n=0}^{\infty}b_{n}x^{n}{% endequation %}

ואנחנו רוצים להגדיר את ההרכבה, {% equation %}a\left(b\left(x\right)\right){% endequation %}. אם הפונקציות היוצרות היו פונקציות אמיתיות ולא סתם חבלי כביסה, מה שהיה מתקיים (כשרדיוס ההתכנסות היה מתיר את זה) הוא

{% equation %}a\left(b\left(x\right)\right)=\sum_{n=0}^{\infty}a_{n}b\left(x\right)^{n}x^{n}{% endequation %}

הדבר הזה הוא לא ביטוי מפורש. כלומר, זה לא שבהרכבה, המקדם של {% equation %}x^{n}{% endequation %} יהיה {% equation %}a_{n}b\left(x\right)^{n}{% endequation %}. מה שקורה הוא שצריך לקחת את הטור האינסופי {% equation %}b\left(x\right){% endequation %}, לכפול אותו בעצמו {% equation %}n{% endequation %} פעמים (את זה אנחנו יודעים לעשות), לכפול את התוצאה במקדם המספרי {% equation %}a_{n}{% endequation %} ואז להוסיף את זה לטור הכולל שאנחנו בונים. בצורה הזו לאותו {% equation %}x^{n}{% endequation %} יכולות לתרום חזקות רבות ושונות מהצורה {% equation %}b\left(x\right)^{k}{% endequation %}. למעשה, קיימת הסכנה שלאותו {% equation %}x^{n}{% endequation %} יהיו <strong>אינסוף</strong> חזקות שתורמות מחוברים. זה קורה אם ורק אם {% equation %}b_{n}\ne0{% endequation %}. כי למשל, בואו נסתכל על המקרה הפשוט שבו {% equation %}b\left(x\right)=1+x{% endequation %}, אז מהן החזקות?

{% equation %}\left(1+x\right)^{0}=1{% endequation %}

{% equation %}\left(1+x\right)^{1}=1+x{% endequation %}

{% equation %}\left(1+x\right)^{2}=1+2x+x^{2}{% endequation %}

{% equation %}\left(1+x\right)^{3}=1+3x+3x^{2}+x^{3}{% endequation %}

וכן הלאה - אנחנו רואים שכל חזקה החל מ-2 תתרום ל-{% equation %}x^{1}{% endequation %}, למשל. למה? כי מה זה בעצם {% equation %}\left(1+x\right)^{3}{% endequation %}? זו המכפלה {% equation %}\left(1+x\right)\left(1+x\right)\left(1+x\right){% endequation %}. בכל פעם אנחנו בוחרים אחד משני האיברים שבתוך זוג סוגריים ספציפי ומוסיפים אותו למכפלה שלנו. אם בכל פעם היינו חייבים לבחור איבר שהוא לפחות {% equation %}x{% endequation %}, אז כל זוג סוגריים שמשתתף במכפלה היה מגדיל ב-1 לפחות את החזקה של {% equation %}x{% endequation %} בתוצאה הסופית. אבל אם 1 נמצא בסוגריים, אז אפשר לבחור אותו ולא להגדיל את החזקה של {% equation %}x{% endequation %} בתוצאה הסופית. זה היה מבטיח שעבור חזקות מסוימות של {% equation %}x{% endequation %}, אפשר יהיה תמיד לייצר אותן החל ממקום מסוים - לכן המקדם שלהם יהיה אינסופי, וזה לא מוגדר היטב.

אפשר לחזור עכשיו אל ההעלאה בחזקה. במקרה הזה, יש לנו את הפונקציה היוצרת

{% equation %}a\left(x\right)=\left(1+x\right)^{r}=\sum_{n=0}^{\infty}{r \choose n}x^{n}{% endequation %}

כלומר, {% equation %}a_{n}={r \choose n}{% endequation %}, אז אני יכול להציב בה את {% equation %}F\left(x\right){% endequation %} לכל {% equation %}F\left(x\right){% endequation %} שמקיים {% equation %}F_{0}=0{% endequation %}. למשל, עבור {% equation %}\sqrt{1-4x}{% endequation %} הצבתי את {% equation %}F\left(x\right)=-4x{% endequation %}, שבהחלט מקיימת את זה. ומה עם תכונות החזקה שאנחנו רוצים להוכיח?

{% equation %}\left(1+F\left(x\right)\right)^{r}\cdot\left(1+F\left(x\right)\right)^{s}=\left(1+F\left(x\right)\right)^{r+s}{% endequation %}

ו-{% equation %}\left(\left(1+F\left(x\right)\right)^{r}\right)^{s}=\left(1+F\left(x\right)\right)^{rs}{% endequation %}

כדי שזה יהיה מוגדר היטב, {% equation %}\left(1+F\left(x\right)\right)^{r}{% endequation %} צריך להיות מהצורה {% equation %}1+G\left(x\right){% endequation %} כך ש-{% equation %}G_{0}=0{% endequation %}. את זה אפשר לראות ממש מההגדרה:

{% equation %}\left(1+F\left(x\right)\right)^{r}=\sum_{n=0}^{\infty}{r \choose n}F\left(x\right)^{n}=1+\sum_{n=1}^{\infty}{r \choose n}F\left(x\right)^{n}{% endequation %}

ועכשיו נגדיר {% equation %}G\left(x\right)=\sum_{n=1}^{\infty}{r \choose n}F\left(x\right)^{n}{% endequation %} ונשתמש בכך ש-{% equation %}F_{0}=0{% endequation %} בעצמו ולכן כל העלאה בחזקה של {% equation %}F\left(x\right){% endequation %} כוללת רק חזקות של {% equation %}x{% endequation %} החל מ-{% equation %}x^{1}{% endequation %}.

עכשיו אפשר לעבור לעבודה הטכנית עצמה של להוכיח ש-{% equation %}\left(1+x\right)^{r}\cdot\left(1+x\right)^{s}=\left(1+x\right)^{r+s}=\sum_{n=0}^{\infty}{r+s \choose n}x^{n}{% endequation %}. יש לנו כאן כפל של שני טורי חזקות, ואנחנו יודעים בדיוק איך זה עובד. נגדיר

{% equation %}a\left(x\right)=\sum_{n=0}^{\infty}{r \choose n}x^{n}{% endequation %}

{% equation %}b\left(x\right)=\sum_{n=0}^{\infty}{s \choose n}x^{n}{% endequation %}

כלומר

{% equation %}a_{n}={r \choose n}{% endequation %}

{% equation %}b_{n}={s \choose n}{% endequation %}

וכעת

{% equation %}a\left(x\right)b\left(x\right)=\sum_{n=0}^{\infty}c_{n}x^{n}{% endequation %}

כאשר

{% equation %}c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}=\sum_{k=0}^{n}{r \choose k}{s \choose n-k}{% endequation %}

מה שאנחנו <strong>מצפים</strong> לקבל הוא

{% equation %}\sum_{k=0}^{n}{r \choose k}{s \choose n-k}={r+s \choose n}{% endequation %}

אם יש לנו את זה - סיימנו את ההוכחה. למרבה המזל, זה שוויון מפורסם מאוד, שאפילו יש לו שם משלו: שוויון צ'ו-ונדרמונדה. עוד יותר למרבה המזל, זה שוויון שקל מאוד להוכיח <strong>קומבינטורית</strong>, כלומר יש לנו אחלה אינטואיציה למה הוא נכון... אבל רק אם {% equation %}s,r{% endequation %} הם מספרים טבעיים. במקרה הזה, אפשר לחשוב על כך שיש לנו קבוצה של {% equation %}r{% endequation %} חתולים ו-{% equation %}s{% endequation %} כלבים ואנחנו רוצים להרכיב צוות מרגלים שכולל בדיוק {% equation %}n{% endequation %} חברים - זו בעיה של <strong>בחירה בלי חשיבות לסדר ובלי חזרות</strong>, ומכיוון שקבוצת המרגלים הפוטנציאליים הכוללת היא מגודל {% equation %}r+s{% endequation %} יש לנו בסך הכל {% equation %}{r+s \choose n}{% endequation %} אפשרויות. אבל היה אפשר גם לסרבל את זה טיפה: אם היינו מחליטים לקחת לקבוצה שלנו <strong>בדיוק</strong> {% equation %}k{% endequation %} חתולים, אז היו לנו {% equation %}{r \choose k}{% endequation %} אפשרויות לבחור את החתולים, ואחר כך היינו צריכים לבחור עוד {% equation %}n-k{% endequation %} כלבים, ולזה יש {% equation %}{s \choose n-k}{% endequation %} אפשרויות, ולכן מעקרון הכפל יש לנו {% equation %}{r \choose k}{s \choose n-k}{% endequation %} אפשרויות להרכיב צוות שכולל בדיוק {% equation %}k{% endequation %} חתולים. את הסיפור הזה יכלנו לעשות לכל {% equation %}k{% endequation %} בין 0 ל-{% equation %}n{% endequation %}, ועקרון החיבור אומר שמספר האפשרויות הכולל, אם כך, הוא {% equation %}\sum_{k=0}^{n}{r \choose k}{s \choose n-k}{% endequation %}. זה מסיים את ההוכחה הקומבינטורית.

השאלה היא מה עושים עכשיו, כשרוצים להוכיח את השוויון ל-{% equation %}r,s{% endequation %} שהם מספרים ממשיים כלליים. לא ברור איך הגיון קומבינטורי יעזור לנו כאן, אבל למרבה המזל גם לא צריך אותו - אפשר להסתמך על מה שכבר הוכחנו. בשביל זה בואו נדבר לרגע על <strong>פולינומים</strong>.

נניח ש-{% equation %}p\left(x\right),q\left(x\right){% endequation %} הם שני פולינומים. אנחנו יודעים שפולינום ממעלה {% equation %}d{% endequation %} נקבע בצורה יחידה על ידי הערכים שלו ב-{% equation %}d+1{% endequation %} נקודות, ולכן פולינום ממעלה {% equation %}d{% endequation %} שמתאפס ב-{% equation %}d+1{% endequation %} נקודות הוא זהותית פולינום האפס. עכשיו, אם אנחנו יודעים ש-{% equation %}p\left(n\right)=q\left(n\right){% endequation %} <strong>לכל</strong> {% equation %}n\in\mathbb{N}{% endequation %}, אז אנחנו יודעים שהפולינום {% equation %}p-q{% endequation %} מתאפס על <strong>אינסוף</strong> נקודות, ובפרט על מספר נקודות שגדול מהדרגה שלו, ולכן הוא זהותית אפס: {% equation %}p-q=0{% endequation %}, כלומר {% equation %}p=q{% endequation %} - <strong>פולינומים שמזדהים על אינסוף נקודות הם זהים</strong>.

עכשיו בואו נסבך את זה ונהפוך את הפולינומים לבעלי שני משתנים: {% equation %}p\left(x,y\right),q\left(x,y\right){% endequation %}. כאן צריך להיזהר: אם למשל {% equation %}p\left(x,y\right)=x{% endequation %} ו-{% equation %}q\left(x,y\right)=y{% endequation %} אז נקבל ש-{% equation %}p\left(n,n\right)=q\left(n,n\right){% endequation %} עבור אינסוף ערכי {% equation %}n\in\mathbb{N}{% endequation %} אבל זה כמובן לא אומר שהפולינומים הללו זהים. הטיעון צריך להיות קצת יותר עדין. באופן כללי, אם יש שתי קבוצות אינסופיות {% equation %}A,B{% endequation %} כך ש-{% equation %}p\left(a,b\right)=0{% endequation %} לכל {% equation %}a\in A,b\in B{% endequation %}, אז {% equation %}p{% endequation %} הוא פולינום האפס (כלומר, הפואנטה היא ש-{% equation %}p{% endequation %} מתאפס על כל {% equation %}A\times B{% endequation %}, לא רק על איזו תת-קבוצה נחמדה של {% equation %}A\times B{% endequation %}). בואו נוכיח את זה: באופן כללי, {% equation %}p\left(x,y\right)=\sum_{i,j}a_{ij}x^{i}y^{j}{% endequation %}. אפשר לסדר את הסכום הזה לפי חזקות של {% equation %}y{% endequation %}, כלומר לכתוב {% equation %}p\left(x,y\right)=\sum_{j}\left(\sum_{i}a_{ij}x^{i}\right)y^{j}{% endequation %}, ולסמן {% equation %}p_{j}\left(x\right)=\sum_{i}a_{ij}x^{i}{% endequation %}. עכשיו, אם כל ה-{% equation %}p_{j}\left(x\right){% endequation %} הללו הם פולינומי האפס, סיימנו; מקבלים ש-{% equation %}p\left(x,y\right)=\sum_{j}p_{j}\left(x\right)y^{j}=\sum_{j}0\cdot y=0{% endequation %}. אז בואו נניח בשלילה שעבור {% equation %}j{% endequation %} כלשהו, {% equation %}p_{j}\left(x\right){% endequation %} הוא <strong>לא</strong> פולינום האפס. בפרט, קיים ערך קונקרטי, {% equation %}a\in A{% endequation %}, כך ש-{% equation %}p_{j}\left(a\right)\ne0{% endequation %} - כי אם לכל {% equation %}a\in A{% endequation %} היינו מקבלים {% equation %}p_{j}\left(x\right)=0{% endequation %} אז היינו מקבלים פולינום שמתאפס על אינסוף ערכים ולכן הוא זהותית 0. אם כן, {% equation %}p_{j}\left(a\right)\ne0{% endequation %} ולכן אם נסתכל על הפולינום {% equation %}q\left(y\right)=p\left(a,y\right){% endequation %} אנחנו רואים שמצד אחד, {% equation %}q\left(y\right)=\sum_{j}p_{j}\left(a\right)y^{j}{% endequation %} הוא לא פולינום האפס כי <strong>לכל הפחות</strong> המקדם של {% equation %}y^{j}{% endequation %} הוא לא אפס. מצד שני - אנחנו יודעים שלכל אינסוף הערכים {% equation %}b\in B{% endequation %} מתקיים {% equation %}q\left(b\right)=p\left(a,b\right)=0{% endequation %} ולכן זה כן פולינום האפס - סתירה. לב העניין הוא בדיוק בשלב האחרון: ש<strong>לכל</strong> {% equation %}b\in B{% endequation %} מקבלים {% equation %}p\left(a,b\right)=0{% endequation %}, באופן שלא תלוי בזהות של {% equation %}a{% endequation %}.

המסקנה מכל זה היא שאם יש לנו זוג פולינומים בשני משתנים {% equation %}p\left(x,y\right),q\left(x,y\right){% endequation %} כך ש<strong>לכל זוג מספרים טבעיים</strong> {% equation %}r,s{% endequation %} מתקיים {% equation %}p\left(r,s\right)=q\left(r,s\right){% endequation %} אז הפולינום הם זהים, לכל זוג ערכים, כולל ערכים ממשיים (או אפילו מרוכבים). עכשיו נסתכל על הביטוי

{% equation %}\sum_{k=0}^{n}{r \choose k}{s \choose n-k}={r+s \choose n}{% endequation %}

לב העניין הוא שבאופן כללי, {% equation %}{x \choose n}=\frac{x\left(x-1\right)\left(x-2\right)\ldots\left(x-n+1\right)}{n!}{% endequation %} הוא פולינום ב-{% equation %}x{% endequation %}: המונה הוא הרי מכפלה של {% equation %}n{% endequation %} פולינומים ב-{% equation %}x{% endequation %}, אז גם הוא פולינום. לכן גם {% equation %}\sum_{k=0}^{n}{x \choose k}{y \choose n-k}={x+y \choose n}{% endequation %} הוא שוויון של פולינומים - ושוויון שמתקיים לכל הצבה של {% equation %}r,s{% endequation %} טבעיים ב-{% equation %}x,y{% endequation %}. זה מוכיח את השוויון לכל {% equation %}r,s{% endequation %} ממשיים, ולכן מסיים את ההוכחה <strong>הפורמלית</strong> לכך ש-{% equation %}\left(1+x\right)^{r}\cdot\left(1+x\right)^{s}=\left(1+x\right)^{r+s}{% endequation %}, וכמסקנה אנחנו מקבלים ש-{% equation %}\left(1+F\left(x\right)\right)^{r}\cdot\left(1+F\left(x\right)\right)^{s}=\left(1+F\left(x\right)\right)^{r+s}{% endequation %} לכל {% equation %}F\left(x\right){% endequation %} עם {% equation %}F_{0}=0{% endequation %}.

זה מקדם אותנו בצורה משמעותית לתפיסה האינטואיטיבית של {% equation %}\left(1+x\right)^{r}{% endequation %} בתור פעולת החזקה. כדי לראות את זה, בואו נוותר לרגע על שיטת הסימון שבה אנחנו משתמשים ובמקום זה נכתוב

{% equation %}\Phi\left(1+F\left(x\right),r\right)=\sum_{n=0}^{\infty}{r \choose n}F\left(x\right)^{n}{% endequation %}

כלומר, בינתיים פשוט הגדרנו דרך לבנות פונקציה יוצרת חדשה מתוך {% equation %}F\left(x\right){% endequation %}. מה לזה ולפעולת ההעלאה בחזקה? ובכן, ראשית נשים לב לכך שעל פי הגדרה

{% equation %}\Phi\left(1+F\left(x\right),1\right)=\sum_{n=0}^{\infty}{1 \choose n}F\left(x\right)^{n}=F\left(x\right)^{0}+F\left(x\right)^{1}=1+F\left(x\right)=\left(1+F\left(x\right)\right)^{1}{% endequation %}

כלומר, {% equation %}\Phi\left(1+F\left(x\right),1\right){% endequation %} מתלכד עם מה שאנחנו מכירים בתור {% equation %}\left(1+F\left(x\right)\right)^{1}{% endequation %}. שימו לב שאת הביטוי {% equation %}\left(1+F\left(x\right)\right)^{1}{% endequation %} אנחנו מכירים לא בתור "פונקציה יוצרת שהוגדרה מוזר" אלא זו חזקה במשמעות הרגילה שלה בחוגים - כפל של האיבר בעצמו שוב ושוב (פעם אחת, במקרה הזה).

טוב ויפה, אבל כזכור עבדנו קשה כדי להוכיח את התכונה

{% equation %}\Phi\left(1+F\left(x\right),r+s\right)=\Phi\left(1+F\left(x\right),r\right)\Phi\left(1+F\left(x\right),s\right){% endequation %}

ולכן עכשיו אפשר להראות באינדוקציה שלכל {% equation %}n{% endequation %} טבעי, 

{% equation %}\Phi\left(1+F\left(x\right),n+1\right)=\Phi\left(1+F\left(x\right),n\right)\Phi\left(1+F\left(x\right),1\right)={% endequation %}

{% equation %}=\left(1+F\left(x\right)\right)^{n}\left(1+F\left(x\right)\right)^{1}=\left(1+F\left(x\right)\right)^{n+1}{% endequation %}

כאשר גם כאן - החזקה היא במשמעות המקורית והרגילה שלה בחוג, אז הפונקציה {% equation %}\Phi{% endequation %} <strong>מתלכדת</strong> עם המשמעות הרגילה בחוג. כדי להשתכנע שהיא מרחיבה אותה בצורה נכונה, בואו נסתכל למשל על

{% equation %}\Phi\left(1+F\left(x\right),1\right)=\Phi\left(1+F\left(x\right),\frac{1}{2}+\frac{1}{2}\right)=\Phi\left(1+F\left(x\right),\frac{1}{2}\right)^{2}{% endequation %}

במילים אחרות, {% equation %}G\left(x\right)=\Phi\left(1+F\left(x\right),\frac{1}{2}\right){% endequation %} הוא מצד אחד טור חזקות פורמלי מוגדר היטב, שלא נזקקנו לחשבון דיפרנציאלי כדי להגדיר; ומצד שני הוא מקיים {% equation %}G\left(x\right)^{2}=1+F\left(x\right){% endequation %} וכמו כן קל לראות ש-{% equation %}G_{0}=1{% endequation %} ולכן, בסימון שלנו בתחילת הפוסט, {% equation %}G\left(x\right)=\sqrt{1+F\left(x\right)}{% endequation %}, וזה תואם את המשמעות האינטואיטיבית שיש לנו למה העלאה בחזקת {% equation %}\frac{1}{2}{% endequation %} אמורה להיות.

זה עובד גם עבור אפס ועבור מספרים שליליים. אפשר לבדוק ישירות על פי ההגדרה ש-

{% equation %}\Phi\left(1+F\left(x\right),0\right)=\sum_{n=0}^{\infty}{0 \choose n}F\left(x\right)^{n}=1{% endequation %}

מה שמתאים להעלאה "רגילה" בחזקת 0, ועכשיו עבור שליליים:

{% equation %}1=\Phi\left(1+F\left(x\right),0\right)=\Phi\left(1+F\left(x\right),n-n\right)={% endequation %}

{% equation %}=\Phi\left(1+F\left(x\right),n\right)\Phi\left(1+F\left(x\right),-n\right){% endequation %}

כלומר קיבלנו ש-{% equation %}\Phi\left(1+F\left(x\right),-n\right)=\frac{1}{\Phi\left(1+F\left(x\right),n\right)}{% endequation %}. הצעד האחרון דורש כזכור שהאיבר החופשי של {% equation %}\Phi\left(1+F\left(x\right),n\right){% endequation %} לא יהיה 0, ואנחנו כבר יודעים שהוא 1, אז הכל בסדר.

זה נחמד כי זה מחזיר אותנו לתחילת הפוסט, שבו הוכחנו בדרך די ישירה ש-{% equation %}1+x+x^{2}+\ldots=\frac{1}{1-x}{% endequation %}. עכשיו זה אמור לנבוע מההגדרה הכללית יותר שלנו. נסמן {% equation %}F\left(x\right)=x+x^{2}+\ldots{% endequation %} ונקבל

{% equation %}\Phi\left(1+F\left(x\right),-1\right)=\sum_{n=0}^{\infty}{-1 \choose n}F\left(x\right)^{n}=\frac{1}{0!}F\left(x\right)^{0}+\frac{\left(-1\right)}{1!}F\left(x\right)^{1}+\frac{\left(-1\right)\left(-2\right)}{2!}F\left(x\right)^{2}+\ldots{% endequation %}

באופן כללי, האיבר ה-{% equation %}n{% endequation %}-י בסכום יהיה {% equation %}\frac{\left(-1\right)\left(-2\right)\cdots\left(-n\right)}{n!}=\frac{\left(-1\right)^{n}n!}{n!}=\left(-1\right)^{n}{% endequation %}, כלומר אנחנו מקבלים

{% equation %}1-F\left(x\right)+F\left(x\right)^{2}-F\left(x\right)^{3}+\ldots{% endequation %}

בכמה דרכים {% equation %}x^{n}{% endequation %}, עבור {% equation %}n\ge2{% endequation %}, יכול להתקבל כאן? אם נסתכל על {% equation %}F\left(x\right)^{k}{% endequation %}, הוא כולל {% equation %}k{% endequation %} זוגות סוגריים שמכל אחד מהם בוחרים חזקה של {% equation %}x{% endequation %} כך שהחזקות מסתכמות אל {% equation %}n{% endequation %} - זה כמו לספור כמה פתרונות יש למשוואה {% equation %}a_{1}+\ldots+a_{k}=n{% endequation %}. מה שכן, שימו לב שהסוגריים לא כוללים את {% equation %}x^{0}{% endequation %} אז הפתרונות הם <strong>בטבעיים חיוביים</strong>. זו בעיה קלה, קומבינטורית: זה כמו לשאול כמה פתרונות בשלמים אי-שליליים יש ל-{% equation %}a_{1}+\ldots+a_{k}=n-k{% endequation %} וזו בדיוק בחירה בלי חשיבות לסדר ועם חזרות של {% equation %}n-k{% endequation %} פעמים מתוך {% equation %}k{% endequation %} איברים - הפתרון הוא {% equation %}{\left(n-k\right)+k-1 \choose k-1}={n-1 \choose k-1}{% endequation %}. עכשיו, זה נתן לנו את המקדם של {% equation %}x^{n}{% endequation %} באיבר {% equation %}F\left(x\right)^{k}{% endequation %}, אבל כדי לקבל את המקדם הכולל של {% equation %}x^{n}{% endequation %} צריך לחבר את המקדמים שמקבלים לכל {% equation %}k{% endequation %} וגם לקחת בחשבון את סימן המינוס שיש על איברים שבהם {% equation %}k{% endequation %} אי זוגי. כלומר נקבל

{% equation %}\sum_{k=1}^{n}\left(-1\right)^{k}{n-1 \choose k-1}{% endequation %}

במקרה הזה קל לטפל בעזרת <strong>הבינום של ניוטון</strong>. נשנה את משתנה הסכימה באותה דרך שבה עשינו את זה קודם עבור פיבונאצ'י:

{% equation %}\sum_{k=1}^{n}\left(-1\right)^{k}{n-1 \choose k-1}=-\sum_{k=0}^{n-1}\left(-1\right)^{k}{n-1 \choose k}=-\left(1-1\right)^{n-1}=0{% endequation %}

המקרים החריגים היחידים הם {% equation %}n=0,1{% endequation %}. עבור {% equation %}n=0{% endequation %} בכלל אי אפשר להשתמש בנוסחה הזו, אבל אם חושבים רגע רואים שהיא אמורה לתת 0 כאן - וזה נכון, כי {% equation %}x^{0}{% endequation %} בכלל לא מופיע ב-{% equation %}-F\left(x\right)+F\left(x\right)^{2}-F\left(x\right)^{3}+\ldots{% endequation %}, הוא מופיע רק ב-1 בהתחלה. כמו כן עבור {% equation %}n=1{% endequation %} יש לנו סיטואציה חריגה של {% equation %}0^{0}{% endequation %} וזו מהסיטואציות שבהן הדבר הנכון לעשות הוא להגדיר {% equation %}0^{0}=1{% endequation %} (<a href="https://gadial.net/2018/01/01/zero_power_equals_one/">יש לי פוסט על זה</a>), ובואו לא נשכח את המינוס הזה שהשתרבב החוצה, כלומר מקבלים {% equation %}-1{% endequation %} במקרה הזה, ולכן {% equation %}1-F\left(x\right)+F\left(x\right)^{2}-F\left(x\right)^{3}+\ldots=1-x{% endequation %} וזה - הפלא ופלא, זה בדיוק מה שציפינו לקבל, כי אנחנו כבר יודעים ש-{% equation %}1+x+x^{2}+\ldots=\frac{1}{1-x}{% endequation %} אז כמובן ש-{% equation %}\left(1+x+x^{2}+\ldots\right)^{-1}=1-x{% endequation %}.

אוקיי, אז אני מקווה שהשתכנענו שהצלחנו להגדיר את {% equation %}\left(1+F\left(x\right)\right)^{r}{% endequation %} לכל {% equation %}r{% endequation %} <strong>רציונלי</strong>. איך נגדיר אותו לכל ממשי? ובכן, כאן אנחנו בבעיה וחייבים לדבר על מושגים מחדו"א פשוט כי <strong>מספר ממשי</strong> הוא מושג מחדו"א. הייתה לי <a href="https://gadial.net/2024/08/11/real_numbers_decimal_notation/">סדרת פוסטים</a> על זה לא מזמן. בגדול, דרך נוחה לחשוב על מספרים ממשיים הם בתור אובייקטים שלכל אחד מהם, אנחנו יכולים לקחת סדרת רציונליים ששואפת אליו. זה מוביל להגדרה "הרגילה" של חזקה שהיא מספר ממשי כללי: בהינתן {% equation %}r{% endequation %}, לוקחים סדרה {% equation %}q_{n}{% endequation %} של רציונליים כך ש-{% equation %}q_{n}\to r{% endequation %}, ואז מגדירים {% equation %}x^{r}=\lim_{n\to\infty}x^{q_{n}}{% endequation %} וצריך לשבור את הראש כדי להוכיח שזה מוגדר היטב. אבל איך אפשר לעשות משהו דומה עם טורי חזקות פורמליים? אין לנו מושג של התכנסות על טורי חזקות, נכון? נכון...?

<h2>החפירה העמוקה ביותר (שנגיע אליה כאן)</h2>

אז כן, יש לנו מושג של התכנסות על טורי חזקות, הוא לא מסובך במיוחד, והוא כנראה יאפשר את הראייה הצלולה ביותר של מה שעשינו כאן ולאן אפשר להתקדם מפה.

בגדול, הרעיון הוא שאם יש לנו סדרה {% equation %}F^{1}\left(x\right),F^{2}\left(x\right),F^{3}\left(x\right),\ldots{% endequation %} ואנחנו רוצים לדעת אם היא מתכנסת לאנשהו, נסתכל על המקדם של {% equation %}x^{n}{% endequation %} עבור כל הסדרות הללו. אם <strong>החל ממקום מסוים</strong> המקדם הזה קבוע, ואם זה קורה <strong>לכל</strong> {% equation %}n{% endequation %}, אז לסדרה יש גבול שהוא הפונקציה היוצרת שבנויה מהמקדמים הללו. קצת יותר פורמלית: אם לכל {% equation %}n{% endequation %} קיימים {% equation %}a_{n}\in\mathbb{R}{% endequation %} ו-{% equation %}k_{n}{% endequation %} כך שלכל {% equation %}i\ge k_{N}{% endequation %} מתקיים ש-{% equation %}F_{n}^{i}=a_{n}{% endequation %} (כאן {% equation %}F_{n}^{i}{% endequation %} פירושו המקדם של {% equation %}x^{n}{% endequation %} בטור החזקות {% equation %}F^{i}\left(x\right){% endequation %}) אז {% equation %}\lim_{i\to\infty}F^{i}\left(x\right)=F\left(x\right){% endequation %} כך ש-{% equation %}F\left(x\right)=\sum_{n=0}^{\infty}a_{n}x^{n}{% endequation %}.

אבל אפשר לעשות את זה עוד יותר מסודר. מי שמכירות את הבניה האנליטית של המספרים ה-{% equation %}p{% endequation %}-אדיים (<a href="https://gadial.net/2010/01/12/padic_numbers_analytic_constructions/">הצגתי אותה כאן</a>) כנראה ירגישו בבית.

ראשית, לכל טור חזקות פורמלי {% equation %}F\left(x\right){% endequation %} ששונה מאפס, נגדיר {% equation %}\nu\left(F\left(x\right)\right)=\min_{F_{n}\ne0}n{% endequation %}, כלומר האינדקס של המקדם הראשון בטור ששונה מאפס. בנוסף נגדיר {% equation %}\nu\left(0\right)=\infty{% endequation %} כדי שהכל יסתדר יפה. עכשיו אפשר להגדיר <strong>מטריקה</strong> על חוג טורי החזקות הפורמליים: 

{% equation %}d\left(F,G\right)=2^{-\nu\left(F-G\right)}{% endequation %}

במילים אחרות, ככל שהאינדקס הראשון שבו {% equation %}F,G{% endequation %} נבדלים זה מזה הוא גבוה יותר, כך ה"מרחק" שלהם יהיה קטן יותר. אם הם נבדלים כבר באינדקס ה-0 המרחק שלהם יהיה 1, ואם הם נבדלים לראשונה באינדקס ה-3 אז המרחק שלהם יהיה {% equation %}\frac{1}{8}{% endequation %} וכן הלאה.

מה שקורה כאן הוא שראשית כל, אם {% equation %}F=G{% endequation %} אז {% equation %}F-G=0{% endequation %} ולכן {% equation %}d\left(F,G\right)=2^{-\nu\left(F-G\right)}=2^{-\nu\left(0\right)}=2^{-\infty}=0{% endequation %} (מי שמפריע לו השימוש הזה באינסוף - אוקיי, בסדר, פשוט נגדיר {% equation %}d\left(F,G\right)=0{% endequation %} כאשר {% equation %}F=G{% endequation %} וחסל, מרוצים?).

שנית, {% equation %}d\left(F,G\right)=2^{-\nu\left(F-G\right)}=2^{-\nu\left(G-F\right)}=d\left(G,F\right){% endequation %}; זה עובד כי המקדם הראשון ששונה מאפס ב-{% equation %}F-G{% endequation %} הוא אותו מקדם כמו ב-{% equation %}G-F{% endequation %}, פשוט עם סימן הפוך.

לבסוף, אם {% equation %}F,G,H{% endequation %} הם שלושה טורים, אז ראשית בואו נסמן ב-{% equation %}n{% endequation %} את האינדקס הראשון שבו {% equation %}F,H{% endequation %} נבדלים (אם הם זהים התוצאה שאגיע אליה עוד מעט נובעת עוד יותר בקלות), כלומר {% equation %}d\left(F,H\right)=2^{-n}{% endequation %}. בואו נסמן ב-{% equation %}m_{1}{% endequation %} את האינדקס הראשון שבו {% equation %}F,G{% endequation %} נבדלים וב-{% equation %}m_{2}{% endequation %} את האינדקס הראשון שבו {% equation %}G,H{% endequation %} נבדלים (ייתכן ש-{% equation %}m_{1},m_{2}=\infty{% endequation %}). אני טוען ש-{% equation %}n\ge\min\left\{ m_{1},m_{2}\right\} {% endequation %}. למה? ובכן, אם {% equation %}G{% endequation %} נבדל מ-{% equation %}F,H{% endequation %} בשלב שבו הם עדיין זהים, זה אומר ש-{% equation %}m_{1}=m_{2}{% endequation %} (כי הוא ייבדל משניהם בו זמנית שהרי הם זהים עדיין בשלב הזה) ומכיוון שזה לפני שהם נבדלים, האינדקס הזה בא לפני {% equation %}n{% endequation %}, כלומר במקרה הזה {% equation %}m_{1},m_{2}<n{% endequation %}.

עכשיו, באינדקס ה-{% equation %}n{% endequation %} מתקיים {% equation %}F_{n}\ne H_{n}{% endequation %} ולכן <strong>פשוט לא ייתכן</strong> ש-{% equation %}G_{n}=F_{n}{% endequation %} וגם {% equation %}G_{n}=H_{n}{% endequation %}, כי שוויון כזה היה מכריח את {% equation %}F_{n}=H_{n}{% endequation %}. לכן זה השלב שבו <strong>בודאות</strong> {% equation %}G{% endequation %} הולך להיבדל מ-{% equation %}F{% endequation %} או מ-{% equation %}H{% endequation %}. אנחנו לא יודעים מי מהם, לכן אנחנו לוקחים את המינימום על {% equation %}\left\{ m_{1},m_{2}\right\} {% endequation %}.

מה המסקנה? {% equation %}n\ge\min\left\{ m_{1},m_{2}\right\} {% endequation %} גורר ש-

{% equation %}d\left(F,H\right)=2^{-n}\le2^{-\min\left\{ m_{1},m_{2}\right\} }=\max\left\{ 2^{-m_{1}},2^{-m_{2}}\right\} =\max\left(d\left(F,G\right),d\left(G,H\right)\right){% endequation %}

זה נותן לנו את <strong>אי שוויון המשולש</strong>, בגרסה יותר חזקה מהרגיל אפילו: אם אני קטן מהמקסימום של שני מספרים אי שליליים, אני בוודאי קטן יותר מהסכום שלהם (שכולל את המקסימום ועוד איזה מספר)

אז קיבלנו פונקציה {% equation %}d{% endequation %} כך ש-

<ul> <li>{% equation %}d\left(F,G\right)\ge0{% endequation %} ויש שוויון אם ורק אם {% equation %}F=G{% endequation %}</li>


<li>{% equation %}d\left(F,G\right)=d\left(G,F\right){% endequation %}</li>


<li>{% equation %}d\left(F,H\right)\le d\left(F,G\right)+d\left(G,H\right){% endequation %}</li>

</ul>

שלוש התכונות הללו הופכות את {% equation %}d{% endequation %} למה שנקרא <strong>מטריקה</strong>, שהיא פונקציה שמאפשרת לדבר באופן כללי על גבולות והתכנסות (למעשה, התכונה החזקה יותר של אי-שוויון המשולש נותנת משהו שנקרא <strong>אולטרמטריקה</strong> אבל נעזוב את זה). עכשיו אפשר לומר משהו כזה: {% equation %}\lim_{n\to\infty}F^{n}\left(x\right)=F\left(x\right){% endequation %} אם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}d\left(F^{n}\left(x\right),F\left(x\right)\right)<\varepsilon{% endequation %}. זו ההגדרה הסטנדרטית לגבול, ואם חושבים עליה קצת בהקשר של ה-{% equation %}d{% endequation %} הספציפית שלנו רואים שהמשמעות של {% equation %}\lim_{n\to\infty}F^{n}\left(x\right)=F\left(x\right){% endequation %} היא בדיוק מה שהזכרתי קודם: כדי שהסדרה {% equation %}F^{n}\left(x\right){% endequation %} תתכנס לגבול, צריך שהמקדם של {% equation %}x^{k}{% endequation %} יתקבע החל ממקום מסוים בסדרה, ואז הוא יהיה המקדם של אותו איבר ב-{% equation %}F\left(x\right){% endequation %}.

עכשיו אפשר להסתכל על ביטוי כמו {% equation %}\sum_{n=0}^{\infty}F\left(x\right)^{n}{% endequation %}. כבר היינו בסיטואציה דומה קודם, וראינו שכדי שחזקה של {% equation %}F\left(x\right){% endequation %} תתנהג יפה, היה צריך שיתקיים {% equation %}F_{0}=0{% endequation %}, אז נניח שזה קורה. עכשיו אפשר לחשוב על {% equation %}\sum_{n=0}^{\infty}F\left(x\right)^{n}{% endequation %} פשוט כמו טור במובן הרגיל, כזה שמוגדר עם סכומים חלקיים {% equation %}\sum_{n=0}^{\infty}F\left(x\right)^{n}=\lim_{n\to\infty}S_{n}{% endequation %} כאשר {% equation %}S_{n}=\sum_{k=0}^{n}F\left(x\right)^{k}{% endequation %}. בכל פעם שבה מוסיפים חזקה חדשה {% equation %}F\left(x\right)^{n}{% endequation %} לסכום שיש לנו, היא משנה רק את המקדמים של {% equation %}x^{n}{% endequation %} וחזקות גבוהות יותר - כלומר, החזקות הנמוכות יותר <strong>התקבעו</strong> ולכן הטור מתכנס.\textbackslash אפשר לעשות משהו אפילו עוד יותר משעשע כדי לחשב את הסכום שלו: הרי כדי לחשב את הסכום של {% equation %}\sum_{n=0}^{\infty}q^{n}{% endequation %} במספרים ממשיים אנחנו מסתכלים על הסכום החלקי ה-{% equation %}n{% endequation %}-י שיוצא {% equation %}\frac{q^{n+1}-1}{q-1}{% endequation %}, נוכל להסתכל על סכום דומה גם עבור {% equation %}F\left(x\right){% endequation %}. הרי איך מוכיחים את הנוסחה לסכום החלקי? מסתכלים על המכפלה

{% equation %}\left(1+F\left(x\right)+\ldots+F\left(x\right)^{n}\right)\left(F\left(x\right)-1\right)=F\left(x\right)^{n+1}-1{% endequation %}

זו זהות שאפשר להוכיח בכל חוג קומוטטיבי. עכשיו, אם {% equation %}F_{0}=0{% endequation %} אז המקדם החופשי של {% equation %}F\left(x\right)-1{% endequation %} שונה מאפס ולכן הוא הפיך, ולכן אפשר לכפול בהופכי ולקבל

{% equation %}1+F\left(x\right)+\ldots+F\left(x\right)^{n}=\frac{F\left(x\right)^{n+1}-1}{F\left(x\right)-1}{% endequation %}

ועכשיו, מהו {% equation %}\lim_{n\to\infty}\frac{F\left(x\right)^{n+1}-1}{F\left(x\right)-1}{% endequation %}? המכנה נשאר קבוע, ובמונה יש לנו חזקה הולכת וגדלה {% equation %}F\left(x\right)^{n+1}{% endequation %}. בחזקה הזו, המקדם של {% equation %}x^{n}{% endequation %} וכל הקודמים לו הוא 0, ולכן... {% equation %}\lim_{n\to\infty}F\left(x\right)^{n+1}=0{% endequation %} ומכאן נקבל {% equation %}\lim_{n\to\infty}\frac{F\left(x\right)^{n+1}-1}{F\left(x\right)-1}=\frac{0-1}{F\left(x\right)-1}=\frac{1}{1-F\left(x\right)}{% endequation %} והנה קיבלנו את התוצאה שממנה התחיל הפוסט - רק שעכשיו הוכחנו אותה <strong>באותה צורה בדיוק</strong> שבה מוכיחים את הסכום ה"קלאסי". אותה טרמינולוגיה, אותו עולם מושגים של התכנסות, אותה טכניקה - <strong>ובלי לערב רדיוסי התכנסות בכלל</strong>. אין זכר למגבלה {% equation %}\left|q\right|<1{% endequation %}, פשוט כי בחוג שלנו, עם המטריקה שלנו, העניינים הם למעשה <strong>פשוטים יותר</strong>.

עכשיו גם קצת יותר ברורה העניין הזה של להציב את {% equation %}F\left(x\right){% endequation %} בתוך {% equation %}G\left(x\right){% endequation %}. אנחנו מקבלים בסוף טור מהצורה {% equation %}\sum_{n=0}^{\infty}a_{n}F^{n}\left(x\right){% endequation %}, וזה מתכנס אם {% equation %}F_{0}=0{% endequation %}. עכשיו אפשר לקחת את זה ולהשתמש בזה עבור טורים מוכרים. למשל, אם ניזכר איך נראה הפיתוח של פונקציית האקספוננט לטור חזקות: {% equation %}e^{x}=\sum_{n=0}^{\infty}\frac{1}{n!}x^{n}{% endequation %}, אז אפשר להגדיר {% equation %}e^{F\left(x\right)}=\sum_{n=0}^{\infty}\frac{1}{n!}F^{n}\left(x\right){% endequation %}, ואפשר להגדיר {% equation %}\ln\left(1+F\left(x\right)\right)=\sum_{n=0}^{\infty}\frac{\left(-1\right)^{n+1}}{n}F^{n}\left(x\right){% endequation %} ועוד ועוד. אז ביטוי כמו {% equation %}\sqrt{1-4x}{% endequation %} שמופיע בתוך פונקציה יוצרת? נראה לי שאנחנו כבר יודעים איך להסתדר איתו. 
