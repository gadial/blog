---
id: 3534
title: "האם פאי הוא מספר אינסופי?"
date: 2018-01-21 22:08:41
layout: post
categories: 
  - מספרים
tags: 
  - ייצוג עשרוני
  - פאי אינסופי
  - שברים משולבים
---
אני רוצה לכתוב על נושא ש<a href="http://www.gadial.net/2008/12/08/bad_math_pi_undefinable/">כבר כתבתי עליו בבלוג</a> לפני עשור בערך ועוד פעם <a href="http://www.gadial.net/2013/01/30/irrational_infinity/">לפני חמש שנים</a>, אבל הפעם בצורה קצת פחות אגרסיבית מאשר בפעמים ההן (שבהן יצא שהתלוננתי על פופולריזציות בעייתיות של המתמטיקה) ובתקווה שעם הסברים טובים יותר. הנושא הוא לכאורה המספר {% equation %}\pi{% endequation %} ("פאי") אבל כפי שנראה בהמשך, הוא מקיף קצת יותר מזה. השאלה הבסיסית, שלעתים מעניינת גם את מי שאין להם היכרות רחבה במיוחד עם המתמטיקה, היא האם {% equation %}\pi{% endequation %} הוא "אינסופי" או לא. אז התשובה שלי היא "לא, אבל אני מבין למה אנשים חושבים שכן וזה מעניין לדבר על זה".

מה זה פאי? ההגדרה המוכרת היא "היחס בין היקף מעגל לקוטר שלו" (יש הגדרות אחרות במתמטיקה, טובות יותר, אבל זה עניין לפוסט אחר), אבל מוכרת לא פחות היא צורת הכתיבה הזו של פאי:

{% equation %}\pi=3.14159265359\dots{% endequation %}

המספר באגף ימין של המשוואה הוא מה שנקרא <strong>הייצוג העשרוני</strong> של פאי. זו סדרה של ספרות שנמשכת, ונמשכת, ונמשכת, עד... עד לנצח, בעצם. שלוש הנקודות שמופיעות אחרי ה-9 הימני ביותר הן בעלות משמעות מדויקת: הן אומרות "הכתיבה של המספר לא נגמרת פה אלא היא אמורה להימשך עוד ופשוט הפסקנו לכתוב". זו המשמעות של "אינסופי" שאני סבור שמדברים עליה כשאומרים ש-{% equation %}\pi{% endequation %} אינסופי - כשכותבים אותו בצורה הזו, אז הספרות שלו נמשכות עוד ועוד ואינן נגמרות לעולם.

נשמע כמו משהו שמתאים לאינטואיציה של "אינסופי"? בהחלט. אבל בואו נביט לרגע על מספר דומה:

{% equation %}3.142857142857\dots{% endequation %}

המספר הזה מאוד קרוב לפאי, וגם הוא מורכב מסדרת ספרות שנמשכת עוד ועוד עד אינסוף. מה ההבדל? המספר הזה שווה <strong>ממש</strong> ל-{% equation %}\frac{22}{7}{% endequation %}. הכתיב המקובל והנפוץ יותר שלו יהיה בתור {% equation %}\frac{22}{7}{% endequation %}. כשאני מסתכל על {% equation %}\frac{22}{7}{% endequation %} אני לא רואה פה משהו "אינסופי"; אני רואה מנה של שני מספרים שלמים, סופיים. אם כן, מה קרה שבייצוג העשרוני שני המספרים כל כך דומים ושניהם "אינסופיים"?

נתחיל מההבדל: {% equation %}\frac{22}{7}{% endequation %} אמנם כולל אינסוף ספרות בייצוג העשרוני שלו, אבל הן <strong>מחזוריות</strong>. ה-{% equation %}142857{% endequation %} שאחרי הנקודה חוזר על עצמו שוב ושוב ושוב. זאת להבדיל מפאי שבו אין שום מחזוריות כזו. למה הם דומים? ובכן כי בחרתי אותם ככה בכוונה; {% equation %}\frac{22}{7}{% endequation %} הוא קירוב ידוע מצויין לפאי. עד כמה מצויין? ובכן, ב-14 למרץ חוגגים את "יום פאי" כי בשיטת כתיבה אחת התאריך נכתב כ-{% equation %}3.14{% endequation %} וזה קרוב ל-{% equation %}3.14159\dots{% endequation %} של פאי; אבל בשיטת כתיבה אחרת התאריך של ה-22 ביולי נכתב בתור {% equation %}22/7{% endequation %}, והיום הזה נקרא "יום קירוב פאי" וזה למרות ש-{% equation %}22/7{% endequation %} שווה ל-{% equation %}3.142\dots{% endequation %} שהוא קירוב <strong>יותר טוב</strong> לפאי מאשר {% equation %}3.14{% endequation %} (ההפרש בין הקירוב לפאי קטן יותר). איזה אי צדק משווע. מה שכן, נראה של-{% equation %}3.14{% endequation %} יש "יתרון" אחר - הוא קירוב <strong>סופי</strong>, שלא משתמש באינסוף ספרות גם בבסיס עשרוני.

בואו נסכם את מה שראינו פה. לכאורה יש שלושה סוגים של מספרים:
<ol>
	<li>סופיים כמו {% equation %}3.14{% endequation %}.</li>
	<li>אינסופיים אבל מחזוריים כמו {% equation %}3.142857142857\dots{% endequation %}.</li>
	<li>אינסופיים ולא מחזוריים כמו {% equation %}3.14159265359\dots{% endequation %}.</li>
</ol>
הדבר הראשון שאני רוצה לשכנע אתכם בו הוא שההבדל בין קטגוריות 1 ו-2 הוא <strong>שרירותי לחלוטין</strong> ובעצם שתיהן אינסופיות (או סופיות) באותה מידה. ראשית, כדי לכתוב מספר אינסופי מחזורי אני <strong>לא צריך</strong> לכתוב אינסוף ספרות. יש כתיב סופי ופשוט שמכיל את כל האינפורמציה שרלוונטית למספר: {% equation %}3.\overline{142857}{% endequation %}. הקו העליון מעל {% equation %}142857{% endequation %} אומר שהן החלק המחזורי, ואין צורך לכתוב אותו שוב ושוב - הכתיב הקיים נותן את כל האינפורמציה לגבי המספר ומאפשר לחשב אותו במדויק. איך מחשבים את המספר במדויק? טוב ששאלתם -<a href="http://www.gadial.net/2016/10/13/inverse_of_998001/"> יש לי פוסט</a> שמתעסק בזה. במקרה שלנו השורה התחתונה פשוטה: לוקחים את החלק המחזורי ושמים אותו בשבר כשבמכנה יש את אותו מספר 9-ים כמו מספר הספרות במונה. כלומר, {% equation %}0.\overline{142857}=\frac{142857}{999999}{% endequation %}. חישוב זריז ילמד אתכם ש-{% equation %}142857\times7=999999{% endequation %} ולכן {% equation %}\frac{142857}{999999}=\frac{1}{7}{% endequation %} ולכן כשמוסיפים לזה 3 מקבלים {% equation %}3+\frac{1}{7}=\frac{22}{7}{% endequation %} - חזרנו לייצוג של המספר שלנו בתור מנה של שני מספרים שלמים.

התעלול הזה שביצעתי הוא חשוב, כי האינטואיציה שמתלווה ל"המספר הזה אינסופי" כמו עם פאי היא שכל ייצוג עשרוני של המספר יהיה רק <strong>קירוב</strong> שיאבד חלק מהמספר. אבל {% equation %}3.\overline{142857}{% endequation %} הוא לא קירוב. הוא האינפורמציה המלאה שנדרשת לנו כדי לשחזר את המספר במדויק.

נקודה נוספת היא ש-{% equation %}3.14{% endequation %} הוא "סופי" במובן זה שהפסקתי לכתוב ספרות, אבל זה רק אומר שהמשך המספר הוא כולו אפסים. הכתיב הנכון של המספר הוא {% equation %}3.14000\dots{% endequation %} או, אם תרצו, {% equation %}3.14\overline{0}{% endequation %}. אתם יכולים להגיד, ובצדק גמור, שלכתוב אפסים זה "מיותר" כי זה לא משפר את ההבנה שלנו את המספר. ובכן, אני מסכים איתכם! אבל גם ב-{% equation %}3.\overline{142857}{% endequation %} זה מיותר לכתוב עוד ספרות כי זה לא משפר את ההבנה שלנו את המספר. לכן ההבדל בין שני "סוגי" המספרים הללו נראה לי שרירותי.

מה גורם להבדל הזה בכלל? הקריטריון שקובע אם שבר יהיה ניתן לכתיבה בצורה "סופית" (כלומר, אינסוף אפסים) או לא הוא זה: האם המכנה הוא מספר שהוא מכפלה של חזקות של 2 וחזקות של 5? אם כן (למשל, {% equation %}\frac{1}{8}=0.125{% endequation %} או {% equation %}\frac{1}{20}=0.05{% endequation %}) אז הוא יהיה סופי, ואחרת (למשל {% equation %}\frac{1}{3}{% endequation %} או {% equation %}\frac{1}{7}{% endequation %}) הוא יהיה אינסופי. למה דווקא 2 ו-5 הן קסומים כל כך? שום סיבה מיוחדת - רק העובדה שאנחנו כותבים מספרים בבסיס 10 ו-{% equation %}10=2\cdot5{% endequation %} הוא הפירוק לגורמים ראשוניים של 10. אם היינו כותבים מספרים בבסיס 6, למשל, אז {% equation %}\frac{1}{3}{% endequation %} היה נכתב בתור {% equation %}0.2{% endequation %} (צריך לקרוא את המספר הזה בתור {% equation %}2\cdot\frac{1}{6}{% endequation %}, כי כאן המספרים שמימין לנקודה הם חזקות של {% equation %}\frac{1}{6}{% endequation %}) ו-{% equation %}\frac{1}{18}{% endequation %} היה נכתב כ-{% equation %}0.02{% endequation %} (שהוא {% equation %}2\cdot\frac{1}{36}{% endequation %}) וכן הלאה. לעומת זאת, {% equation %}\frac{1}{5}{% endequation %} היה נאלץ להיכתב בצורה אינסופית, בתור {% equation %}0.111\dots{% endequation %} (די בדומה לאופן שבו {% equation %}\frac{1}{9}{% endequation %} נכתב כך בבסיס העשרוני הרגיל שלנו).

כלומר, ההבדל בין הייצוג ה"סופי" שסימנתי קודם בתור קטגוריה 1, והייצוג ה"אינסופי" שסימנתי בתור קטגוריה 2 הוא מאוד שרירותי - הוא תלוי בבסיס הספירה שלנו. בבחירה החצי-אקראית שלנו בכמה ספרות להשתמש. <strong>כל</strong> שבר יהיה סופי בבסיס ספירה מסויים, ולכן הסופיות/אינסופיות היא לא חלק מהותי מהשבר: אי אפשר להגיד "השבר הזה הוא אינסופי" כי חייבים לומר ביחס לאיזה בסיס ספירה מדובר.

בואו נעבור לדבר על הקטגוריה השלישית. מספרים שהייצוג שלהם הוא אינסופי ולא מחזורי. במקרה הזה התכונה הזו <strong>אינה</strong> תלויה בבסיס הספירה. הכלל הוא זה: אם למספר יש ייצוג מחזורי (סופי/אינסופי) אז הוא שבר, כלומר ניתן לכתיבה בתור {% equation %}\frac{a}{b}{% endequation %} עם {% equation %}a,b{% endequation %} שלמים (בטרמינולוגיה שלי גם 1 הוא שבר, למשל: הוא {% equation %}\frac{1}{1}{% endequation %}); ואם הוא שבר, אז הייצוג שלו הוא מחזורי. בכל בסיס ספירה. לכן מספרים בקטגוריה 3, של מספרים עם ייצוג לא מחזורי, הם בכלל לא שברים. שברים נקראים לפעמים <strong>מספרים רציונליים</strong> ולכן מספר שאיננו שבר נקרא <strong>מספר אי רציונלי</strong>. הדוגמא הקלאסית למספר אי רציונלי היא שורש 2, {% equation %}\sqrt{2}=1.4142135\dots{% endequation %}. איך בעצם אנחנו יודעים ששורש 2 הוא לא רציונלי? <a href="http://www.gadial.net/2007/06/11/irrational_numbers/">יש לי הוכחה כאן</a>, אבל אם אנחנו כבר מדברים על זה למה לא להציג אותה שוב בזריזות, הרי זו מההוכחות המפורסמות במתמטיקה. אם לא מעניין אתכם אפשר פשוט לדלג על הפסקה הבאה.

ובכן, נניח ש-{% equation %}\sqrt{2}{% endequation %} הוא <strong>כן</strong> שבר - מה שנקרא הנחה בשלילה. אז אפשר לסמן {% equation %}\sqrt{2}=\frac{a}{b}{% endequation %} כאשר {% equation %}\frac{a}{b}{% endequation %} הוא <strong>שבר מצומצם</strong> - אין ל-{% equation %}a,b{% endequation %} גורם משותף. אם נעלה את שני אגפי המשוואה בריבוע נקבל {% equation %}2=\frac{a^{2}}{b^{2}}{% endequation %}, כלומר {% equation %}a^{2}=2b^{2}{% endequation %} ובפרט {% equation %}a^{2}{% endequation %} הוא <strong>זוגי</strong>. מכיוון שאי-זוגי כפול אי-זוגי הוא אי-זוגי, לא ייתכן ש-{% equation %}a{% endequation %} הוא אי זוגי - הוא חייב להיות זוגי בעצמו, כלומר {% equation %}a=2d{% endequation %}. נציב במשוואה {% equation %}a^{2}=2b^{2}{% endequation %} ונקבל {% equation %}4d^{2}=2b^{2}{% endequation %}, כלומר {% equation %}b^{2}=2d^{2}{% endequation %} ומכך נקבל שגם {% equation %}b{% endequation %} זוגי, בסתירה לכך שאין ל-{% equation %}a,b{% endequation %} גורם משותף (והנה מצאנו ש-2 הוא גורם משותף). מסקנה: הנחת השלילה שלנו שגויה ולכן {% equation %}\sqrt{2}{% endequation %} איננו שבר.

גם פאי הוא מספר אי רציונלי, ומכאן הייצוג הלא מחזורי שלו, אבל ההוכחה מסובכת יותר ולכן לא אביא אותה כאן. לכאורה זה מסיים את העניין - אין ייצוג מחזורי למספרים אי רציונליים ובוודאי שאין להם ייצוג פשוט בתור מנה של שני מספרים, אז הם בבירור אינסופיים, לא?

ובכן, לא בדיוק. הסיבה שהכנסתי את {% equation %}\sqrt{2}{% endequation %} לתמונה היא כדי להפיל אתכם בפח. כי ל-{% equation %}\sqrt{2}{% endequation %} בהחלט <strong>יש</strong> ייצוג סופי, פשוט בשיטת ייצוג אחרת של מספרים, שאותה לא רואים בבתי הספר ובאופן כללי עלולה להיראות מאוד מפחידה למרות שיש מאחוריה לא מעט הגיון - ייצוג של מספר בתור <strong>שבר משולב</strong>. <a href="http://www.gadial.net/2010/05/29/continued_fractions_1/">כאן יש לי פוסט</a> על מה זה שבר משולב, אבל בואו פשוט נראה דוגמא:

{% equation %}1+\frac{1}{2+\frac{1}{2+\frac{1}{2+\dots}}}{% endequation %}

ישמרנו לגראנז', מה הולך פה? שבר משולב הוא יצור מוזר שנראה כמו שבר שבו המכנה בעצמו מורכב משבר, שבו המכנה בעצמו מורכב משבר, וכן הלאה עד אינסוף. כמו במקרה של ייצוג עשרוני, שבו אינסוף הספרות מייצגות סכום אינסופי ועם זאת עדיין אפשר לקבל ממנו מספר סופי, כך קורה גם עם שבר משולב. כדי להקל קצת על הכתיב המסורבל שלו, אפשר לכתוב אותו גם בצורה הבאה:

{% equation %}1+\frac{1}{2+}\frac{1}{2+}\frac{1}{2+\dots}{% endequation %}

השבר המשולב הזה הוא בבירור <strong>מחזורי</strong> - הוא מתחיל עם 1 ומשם והלאה מופיע רק 2 כל הזמן. כלומר, יש לנו סיטואציה דומה לזו של קטגוריה 2 מקודם - אם יש לנו מחזוריות, אז מספיק מספר סופי של ספרות כדי לייצג את המספר בשלמותו. אפשר לכתוב {% equation %}\left[1,\overline{2}\right]{% endequation %} בתור הייצוג של המספר במקום להסתבך עם הכתיב השברי המפחיד. אם כן, לדעתי המספר הזה הוא "סופי" באותו מובן של המספרים מקטגוריות 1 ו-2 שראינו קודם. אבל מהו המספר הזה? זה פשוט {% equation %}\sqrt{2}{% endequation %} מיודענו. יש משפט שמאפיין את כל המספרים הממשיים שיש להם ייצוג כשבר משולב מחזורי - אלו כל המספרים שהם פתרונות של משוואה ממעלה שנייה במספרים רציונליים. {% equation %}\sqrt{2}{% endequation %} הוא פתרון המשוואה {% equation %}x^{2}-2=0{% endequation %}, למשל.

עבורי אישית הפעם הראשונה שבה נתקלתי בתוצאה הזו הייתה נקודת שבר (אוי ואבוי איזה משחק מילים נוראי) גדולה עבורי. עד אז הייתי <strong>בטוח</strong> שכל המספרים האי-רציונליים הם "בעלי ייצוג אינסופי". אבל זה לא המצב. הנה יש לנו מספר אי רציונלי עם ייצוג סופי בעליל, בשיטת ייצוג <strong>לא שרירותית</strong>. קצת קשה להרגיש את זה בפוסט כמו זה, כמובן, שבו שלפתי את השפן של השברים המשולבים מהכובע ולא טרחתי להצדיק <strong>עד כמה</strong> הם שיטת ייצוג סבירה - אבל זה מה שהם. לי זה גרם לפקפק למדי בכל העניין הזה של "ייצוג אינסופי". אני לא אומר ש<strong>אין</strong> מספרים שאפשר לייצג רק באמצעות כמות אינסופית של אינפורמציה (יש) אלא שצריך להיות יותר גמישים מחשבתית ולא להניח שאינסופיות בשיטת ייצוג אחת אומרת יותר מדי.

מה עם פאי? האם לפאי יש ייצוג מחזורי באמצעות שבר משולב? ובכן, לא. פאי הוא <strong>טרנסנדנטי</strong> - זה מספר שהוא לא הפתרון של <strong>אף</strong> משוואה במקדמים רציונליים. בפרט לא משוואה ממעלה שניה, ולכן המשפט שהזכרתי לפני רגע לא עובד עבורו והייצוג שלו כשבר משולב הוא לא מחזורי. אבל זה לא אומר שאין לו ייצוגים שיש בהם <strong>תבנית פשוטה</strong> אחרת. אם אנחנו מדברים על שבר משולב מוכלל - כזה שבו המונים לא חייבים להיות 1 כמו בדוגמא שנתתי, אז יש לפאי את הייצוג המופלא הבא:

{% equation %}\pi=\frac{4}{1+}\frac{1^{2}}{2+}\frac{3^{2}}{2+}\frac{5^{2}}{2+}\frac{7^{2}}{2+\dots}{% endequation %}

הייצוג הזה אינו מחזורי, אבל התבנית שלו מאוד ברורה - אחרי האיבר הראשון המכנה הוא תמיד 2 והמונה הוא חזקות של המספרים האי-זוגיים. את התבנית הזו אפשר לתאר בעזרת נוסחה קומפקטית וסופית. והנה עוד ייצוג, הפעם פשוט בתור סכום אינסופי:

{% equation %}\pi=4\left(1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\frac{1}{9}-\frac{1}{11}+\dots\right){% endequation %}

את הסכום הזה אפשר לכתוב בצורה "סופית" כך: {% equation %}\pi=4\sum_{k=1}^{\infty}\frac{\left(-1\right)^{k+1}}{2k-1}{% endequation %}. אתם יכולים להתרעם, ובצדק, על כך שאני אומר שכתבתי את הסכום בצורה "סופית" - הרי הסכום הוא אינסופי ואני משתמש בסימן {% equation %}\infty{% endequation %} בתוך הנוסחה והכל. אבל צריך להבין שזה גם <strong>בדיוק</strong> מה שקורה בייצוג "רגיל" של מספר בבסיס עשרוני. מה בעצם אומר {% equation %}0.333\dots{% endequation %}? הוא אומר את הדבר הבא:

{% equation %}0.333\dots=\frac{3}{10^{1}}+\frac{3}{10^{2}}+\frac{3}{10^{3}}+\dots=\sum_{k=1}^{\infty}\frac{3}{10^{k}}{% endequation %}

כלומר, זה שהייצוג של מספר כלשהו מתאר "תהליך אינסופי" (סכום אינסופי, שבר משולב אינסופי, מה שתרצו) לא אומר שהייצוג עצמו הוא אינסופי, או שהמספר עצמו הוא אינסופי. נוסחאות כמו זו של פאי למעלה מאפשרות לנו לחשב אותו באיזו רמת קירוב שנרצה - כלומר, למצוא כמה ספרות מימין לנקודה העשרונית שנרצה - אז באיזה מובן פאי הוא אינסופי או בלתי מושג?

טיעון מאוד נפוץ הוא ש"אי אפשר לתפוס את פאי בשלמותו", אבל לדעתי {% equation %}4\sum_{k=1}^{\infty}\frac{\left(-1\right)^{k+1}}{2k-1}{% endequation %} בדיוק תופס אותו בשלמותו. אז אפשר לומר "אבל לא כתבת את כל הספרות של פאי על נייר", ולזה יש לי שתי תשובות. ראשית, ופחות חשוב, מה זה בכלל אומר שהכל כתוב על נייר? אם כתובות לנו מיליון ספרות על נייר, אז אנחנו בני האדם עדיין לא נהיה מסוגלים לתפוס את כולן בו זמנית. מה התועלת בכך שכל הספרות כבר כתובות על נייר? שאם ישאלו אותנו מה הספרה במקום ה-352,263 נוכל פשוט לשוטט בזהירות על הנייר עד שנגיע לספרה המתאימה ולהגיד מהי? אותו דבר אפשר לעשות עם פאי - אם יבקשו מאיתנו את הספרה במקום ה-352,263 של פאי נוכל לחשב אותה וזה אולי ידרוש אפילו פחות מאמץ מאשר לספור שהגענו בדיוק למקום ה-352,263 של מספר שכתוב כולו על נייר.

אבל יותר מכך, כל ה"דרישה" הזו לכתוב את <strong>הספרות</strong> של פאי על נייר היא שגויה. לפאי <strong>אין ספרות</strong>. כשאומרים "ספרות" מתכוונים לספרות שמייצגות את פאי בשיטת ייצוג מסויימת, השיטה העשרונית שבה מייצגים מספרים בתור סכומים של חזקות של 10 כפול מקדמים בין 0 ל-9. אני לא רואה את הסיבה שבגללה נהיה מחוייבים להשתמש דווקא בשיטת הסימון הזו כדי "לתפוס את פאי".

לסיכום, אני מבין למה אנשים מתכוונים כשהם אומרים "פאי אינסופי". הם מתכוונים לכך שבייצוג עשרוני אין מחזוריות לאינסוף הספרות שלו. הטענה הזו נכונה לגמרי מבחינה מתמטית ויש בה עניין מסויים, אבל אני לא כל כך מסכים שכדאי להשתמש במילה "אינסופי" בצורה כזו. כשאני מדבר על מספרים אינסופיים אני בדרך כלל מתכוון למספרים שגדולים מכל מספר טבעי (למשל <a href="http://www.gadial.net/2011/05/25/ordinals_overview/">הסודר</a> {% equation %}\omega{% endequation %}) בזמן שפאי תקוע לו היטב בין 3 ו-4.