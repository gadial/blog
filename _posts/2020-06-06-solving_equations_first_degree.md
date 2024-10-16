---
title: "אז איך פותרים משוואות (ממעלה ראשונה בנעלם יחיד)?"
layout: post
categories:
  - כללי
tags:
  - משוואות
social_media_share: true
---

הרי לכם תרחיש בדוי מהראש שאינו מבוסס על חוויה אישית מטופשת שלי בכלל בשום צורה: נניח שנתקלתי בחולצה שנראית לי מגניבה ממש ואני רוצה להזמין אותה מהאתר היחיד באינטרנט שמוכר אותה. החולצה עולה 50 ש"ח. טוב ויפה, אבל האתר דורש קניה של מינימום 200 ש"ח כדי שאוכל לבצע הזמנה. אני מחליט למלא את יתר ההזמנה בחולצות פשוטות יותר, שעולות רק 30 ש"ח כל אחת. כמה חולצות כאלו אני צריך לקנות כדי שאוכל להגיע למחיר המינימום להזמנה?

התשובה היא "חמש", והדרך הפשוטה ביותר להגיע לתשובה הזו היא פשוט <strong>לנסות</strong>. לבחור עוד ועוד חולצות עד שבסוף רואים שהגעתי למינימום ההזמנה. זה גם מה שהייתי עושה, אם לא היה לי איזה אינסטינקט בראש שגורם לי לבצע אוטומטית את החישוב ולהגיע אל "חמש" עוד לפני הניסוי וטעיה. האינסטינקט הזה שם כי בבית הספר התעקשו שאלמד <strong>לפתור משוואות</strong>, וזו דוגמא למשוואה מהסוג הנדיר שאפשר לפתור כמעט ללא מחשבה.

בפוסט הזה אני רוצה לדבר על פתרון של משוואות. כפי שדי ברור מהדוגמא המונפצת שלי, שאלת ה"בשביל מה צריך את זה" היא סיפור נפרד ואני לא הולך לנסות לענות עליה ברצינות כאן. לפעמים זה מועיל; לפעמים זה מגניב; לפעמים זה חשוב; ייתכן שעבורכם זה יהיה נטול חשיבות לחלוטין ואתם לומדים את זה רק כי בבית הספר מכריחים אתכם. אני אישית אוהב מתמטיקה כי זה כיפי ומעניין - אני מקווה שאפילו משהו כמו פתרון משוואות יכול להיות כיפי ומעניין (מה שבטוח הוא שזה אכן צעד ראשון בדרך להיכרות עם דברים כיפיים ומעניינים אחרים במתמטיקה).

אז מה זו משוואה? הכי פשוט להראות דוגמא, והסיפור עם החולצות אכן נותן דוגמא כזו - את המשוואה {% equation %}30x+50=200{% endequation %}. כאן אנחנו רואים מה משוואה כוללת. ראשית כל, היא כוללת את סימן השוויון, "=". מה שנמצא מימין לסימן הזה נקרא <strong>אגף ימין של המשוואה</strong> ומה שנמצא משמאל לסימן הזה נקרא <strong>אגף שמאל של המשוואה</strong>. המשוואה עצמה היא הטענה "מה שבאגף ימין שווה למה שבאגף שמאל". לכתוב {% equation %}3+5=8{% endequation %} זה לכתוב משוואה; גם לכתוב {% equation %}3\times5=7+8{% endequation %} זה לכתוב משוואה. גם לכתוב {% equation %}4=4{% endequation %} זה לכתוב משוואה. אפילו לכתוב {% equation %}3=4{% endequation %} זה לכתוב משוואה, רק שבמקרה של {% equation %}3=4{% endequation %} המשוואה <strong>לא נכונה</strong> (לפחות לא במערכת המספרים הרגילה שלנו) ומה שנכון לכתוב במקרה הזה הוא {% equation %}3\ne4{% endequation %}.

בדרך כלל מה שאנחנו עושים עם משוואות הוא <strong>לפתור</strong> אותן. במשוואה כמו {% equation %}3\times5=7+8{% endequation %} אין ממש מה לפתור; אולי רק אם אנחנו רוצים לוודא שאגף ימין ושמאל באמת שווים. לרוב הסיטואציה היא כמו ב-{% equation %}30x+50=200{% endequation %}: פרט למספרים, המשוואה כוללת גם <strong>נעלמים</strong>, כלומר סימונים שמייצגים מספרים אבל אנחנו לא לגמרי החלטנו אילו מספרים הם אמורים לייצג. במשוואה {% equation %}30x+50=200{% endequation %} יש נעלם יחיד: {% equation %}x{% endequation %}. "לפתור את המשוואה" פירושו לענות על השאלה - אילו מספרים אפשר להציב במקום {% equation %}x{% endequation %} כך שהמשוואה תהיה נכונה? כלומר, ש-30 כפול המספר שהצבנו באיקס, כל זה ועוד 50, יהיה שווה 200.

למשוואות לא חייב להיות פתרון; למשל, למשוואה {% equation %}0\cdot x=1{% endequation %} אין פתרון (אין מספר שכאשר מכפילים אותו באפס נותן 1 כי כל מספר כפול אפס שווה אפס) ולפעמים יכולים להיות למשוואה כמה פתרונות שונים. זו שאלה כללית ומרתקת במתמטיקה: מהי קבוצת הפתרונות של משוואה? איך היא מתנהגת? איך בודקים שייכות של איבר אליה? וכבר עבור משוואות פשוטות "יחסית" התשובות יכולות להיות מורכבות מאוד (למשל, המשוואה {% equation %}y^{2}=x^{3}+ax+b{% endequation %} שמכונה "עקום אליפטי" היא בעלת מרחב פתרונות מורכב מאוד שהבנה שלו דורשת מתמטיקה עמוקה מאוד). לכן אנחנו מתחילים מלדעת איך פותרים משוואות פשוטות <strong>מאוד</strong>, מתקדמים אל לדעת לפתור משוואות <strong>טיפה</strong> פחות פשוטות, ועוצרים שם; ההמשך הוא במתמטיקה מתקדמת יותר.

אני אדבר פה רק על משוואות פשוטות, למרות שהטכניקות שאני אראה רלוונטיות גם למשוואות מסובכות יותר.

אז איך פותרים את המשוואה {% equation %}30x+50=200{% endequation %}? קודם נראה את הצעדים ואז ננסה להבין מה בעצם עשיתי בהם.

ראשית, אני "מעביר את 50 אגף". זה אומר שאני עובר מהמשוואה {% equation %}30x+50=200{% endequation %} אל המשוואה {% equation %}30x=200-50{% endequation %}. ה-{% equation %}50{% endequation %} שהיה באגף שמאל עבר אל אגף ימין, וה"מחיר" של המעבר הזה הוא שהסימן שלו השתנה מפלוס אל מינוס (למה? עוד רגע אסביר את הנימוקים). עכשיו אני מבצע את פעולת החיסור ומקבל את המשוואה הבאה:

{% equation %}30x=150{% endequation %}

עכשיו אני <strong>מחלק את שני האגפים</strong> במספר 30 ומקבל {% equation %}x=\frac{150}{30}{% endequation %}. אחרי ביצוע החלוקה באגף ימין אני מקבל {% equation %}x=5{% endequation %} וזה הפתרון של המשוואה. פשוט? כן! וזו <strong>רוב</strong> הטכניקה שנדרשת כדי לפתור משוואות.

בואו ננסה להבין מה בעצם עשיתי כאן. התחלתי עם משוואה אחת, ואז יצרתי מין "שרשרת" של משוואות שהאחרונה בהן היא פתרון של המשוואה. בואו נכתוב במפורש את כל השרשרת:

<ul> <li>{% equation %}30x+50=200{% endequation %}</li>


<li>{% equation %}30x=200-50{% endequation %}</li>


<li>{% equation %}30x=150{% endequation %}</li>


<li>{% equation %}x=\frac{150}{30}{% endequation %}</li>


<li>{% equation %}x=5{% endequation %}</li>

</ul>

הרעיון המרכזי מאחורי השרשרת הזו, ומאחורי פתרון משוואות בכלל, הוא שכל המשוואות פה הן <strong>שקולות</strong> אחת לשניה. מה זה אומר? שתי משוואות הן שקולות אם בכל פעם שבו אחת מהן היא נכונה, גם השניה היא נכונה. כלומר: אם אני מציב ערך כלשהו ב-{% equation %}x{% endequation %} ויוצא שאחת מהמשוואות היא נכונה, אז מובטח לי שגם השניה תהיה נכונה עם אותו ערך של {% equation %}x{% endequation %}; ואם עבור הצבה כלשהי ב-{% equation %}x{% endequation %} המשוואה הייתה לא נכונה, גם השניה תהיה לא נכונה.

בואו נראה דוגמא פשוטה לסיטואציה שבה זה <strong>לא</strong> המצב; שבה יש לנו שתי משוואות שאינן שקולות. הנה הן:

<ul> <li>{% equation %}5x=4x{% endequation %}</li>


<li>{% equation %}5=4{% endequation %}</li>

</ul>

המשוואה השניה בבירור היא תמיד לא נכונה; המשוואה הראשונה היא לא נכונה אם מציבים באיקס את 1, למשל, אבל אם מציבים באיקס את 0 אז המשוואה דווקא נכונה. כלומר, קיימת סיטואציה שבה המשוואה הראשונה נכונה, ולעומת זאת במשוואה השניה גם אם "נציב באיקס אפס" המשוואה תהיה לא נכונה - איקס בכלל לא מופיע בה, מה זה חשוב מה אנחנו "מציבים" בו?

זוג המשוואות הזה חשוב כי האופן שבו עברתי מהראשונה אל השניה היה על ידי ביצוע חלוקה - חילקתי באיקס. הלקח הוא שצריך להיזהר - לא כל פעולה שאני מבצע על המשוואה מייצרת משוואה ששקולה לה. אבל לא צריך להיזהר <strong>יותר מדי</strong> - רוב הפעולות שבהן נרצה להשתמש מייצרות משוואות שקולות וקל לזהות את המקרים שבהם זה לא קורה.

בואו נסתכל על המעבר הראשון שביצעתי במשוואות למעלה - למה הוא תקין?

<ul> <li>{% equation %}30x+50=200{% endequation %}</li>


<li>{% equation %}30x=200-50{% endequation %}</li>

</ul>

כיניתי את המעבר הזה "העברת אגף" אבל אני בעצם עושה בו משהו קצת יותר פשוט: אני <strong>מחבר לשני האגפים את אותו מספר</strong>. במקרה הנוכחי, אני מחבר לשניהם {% equation %}-50{% endequation %}. הייתי יכול להוסיף פה "שלב ביניים":

<ul> <li>{% equation %}30x+50-50=200-50{% endequation %}</li>

</ul>

אחרי שלב הביניים הזה ה-{% equation %}+50-50{% endequation %} נעלם כי הסכום של שניהם שווה לאפס. גם זה סוג של צעד, שאני גם עושה בהמשך - להחליף את אחד מאגפי המשוואה במשהו ששווה לו נותן לנו משהו שקול למשוואה המקורית. זה גם מה שאני עושה במעבר הבא:

<ul> <li>{% equation %}30x=200-50{% endequation %}</li>


<li>{% equation %}30x=150{% endequation %}</li>

</ul>

כאן החלפתי את {% equation %}200-150{% endequation %} ב-{% equation %}50{% endequation %} ששווה לו וקיבלתי משוואה שקולה.

הסוג הנוסף של מעבר שביצעתי היה <strong>כפל של שני האגפים באותו מספר</strong>:

<ul> <li>{% equation %}30x=150{% endequation %}</li>


<li>{% equation %}x=\frac{150}{30}{% endequation %}</li>

</ul>

ושוב, קפצתי על צעד. אני כופל את שני האגפים במספר {% equation %}\frac{1}{30}{% endequation %} ("מחלק ב-30") ולכן שלב הביניים היה {% equation %}\frac{1}{30}\cdot30x=\frac{1}{30}\cdot150{% endequation %}. את הצמצום {% equation %}\frac{30}{30}=1{% endequation %} ביצעתי בלי לכתוב אותו במפורש.

אז אילו פעולות היו לנו שמייצרות משוואה שקולה מתוך משוואה קיימת?

<ul> <li>להחליף אגף אחד של המשוואה באגף אחר ששווה לו.</li>


<li>לחבר את אותו מספר לשני אגפי המשוואה.</li>


<li>להכפיל באותו מספר את שני אגפי המשוואה.</li>

</ul>

את הפעולה השלישית צריך לסייג. זה <strong>לא עובד</strong> אם המספר שבו כופלים הוא אפס. אם יש לי את המשוואה {% equation %}x=x+1{% endequation %}, לא קשה לראות על ידי חיסור {% equation %}x{% endequation %} משני האגפים שמקבלים {% equation %}0=1{% endequation %} וזו משוואה נטולת פתרון. עם זאת, אם נכפול ב-0 את שני אגפי המשוואה נקבל {% equation %}0=0{% endequation %} שהיא משוואה נכונה ("כל איקס הוא פתרון"). זה היוצא מן הכלל היחיד - אם לא כופלים באפס (או מנסים לחלק באפס) תמיד מקבלים משוואה שקולה.

למה בעצם?

הסוד כאן טמון בשאלה אם הפעולה שאנחנו מבצעים על אגפי המשוואה היא <strong>פעולה הפיכה</strong> או לא. אני אתנסח פורמלית: נניח שיש לי את המשוואה {% equation %}a=b{% endequation %} כש-{% equation %}a{% endequation %} ו-{% equation %}b{% endequation %} הם מספרים כלשהם. אז אני מבצע <strong>פעולה</strong> כלשהי על שני האגפים ומקבל משוואה חדשה, {% equation %}f\left(a\right)=f\left(b\right){% endequation %} כש-{% equation %}f{% endequation %} מייצגת את הפעולה שביצעתי. בלשון מתמטית אומרים ש-{% equation %}f{% endequation %} היא <strong>פונקציה</strong> שהפעלתי על שני האגפים. הרעיון הוא שאם {% equation %}a{% endequation %} אכן היה שווה ל-{% equation %}b{% endequation %} (אותו ערך מספרי בדיוק) אז הפעלת {% equation %}f{% endequation %} על שני האגפים תחזיר את אותו ערך מספרי. כלומר, אם המשוואה {% equation %}a=b{% endequation %} מתקיימת <strong>אז</strong> גם המשוואה {% equation %}f\left(a\right)=f\left(b\right){% endequation %} מתקיימת. שימו לב שזה משהו שקורה גם עם פעולה "בעייתית" כמו הכפל ב-{% equation %}0{% endequation %}: אם התחלתי מ-{% equation %}3=1+2{% endequation %} וכפלתי את שני האגפים ב-0 אקבל את {% equation %}0=0{% endequation %} שגם היא מתקיימת, פשוט "משהו הלך לאיבוד" בדרך.

עכשיו, {% equation %}f{% endequation %} יכולה להיות בעלת התכונה הבאה: לכל {% equation %}a,b{% endequation %}, אם {% equation %}a\ne b{% endequation %} אז {% equation %}f\left(a\right)\ne f\left(b\right){% endequation %}. או בניסוח אחר: אם {% equation %}f\left(a\right)=f\left(b\right){% endequation %} אז {% equation %}a=b{% endequation %} (התכונה הזו נקראת "חד-חד-ערכיות"). אם {% equation %}f{% endequation %} היא בעלת התכונה הזו, אז בהינתן המשוואה {% equation %}f\left(a\right)=f\left(b\right){% endequation %} אפשר "לשחזר" מתוכה את המשוואה המקורית {% equation %}a=b{% endequation %}.

למשל, אם {% equation %}f\left(a\right)=a+3{% endequation %}, אז נקבל מ-{% equation %}a=b{% endequation %} את המשוואה {% equation %}a+3=b+3{% endequation %}. כדי "לשחזר" את המשוואה המקורית, נפעיל על המשוואה החדשה את הפעולה {% equation %}g\left(a\right)=a-3{% endequation %} ש"הופכת" את {% equation %}f{% endequation %}. דבר דומה קורה גם עבור כפל: אם {% equation %}f\left(a\right)=3a{% endequation %} אז ה"היפוך" של הפונקציה הזו הוא {% equation %}g\left(a\right)=\frac{a}{3}{% endequation %}. רק עבור כפל באפס אין פעולה הופכית שכזו, כי אי אפשר לחלק באפס, וכפל באפס הוא בבירור לא פעולה חד-חד-ערכית (כי למשל עבור {% equation %}1\ne2{% endequation %} אחרי כפל באפס נקבל {% equation %}0=0{% endequation %}).

אז חיבור וכפל במשהו שאינו אפס הן פעולות הפיכות ולכן הן משמרות שקילות של משוואות. מה עם הפעולה השלישית, של "להחליף אגף אחד של המשוואה באגף אחר ששווה לו"? הפעולה הזו לא משנה את <strong>הערך המספרי</strong> של האגף, רק את איך שהערך המספרי הזה כתוב בו; פורמלית, זה כאילו הפעלנו על האגף את הפונקציה {% equation %}f\left(a\right)=a{% endequation %} שהיא בבירור חד-חד-ערכית. לכן גם הפעולה הזו משמרת שקילות של משוואות.

מצוידים בכל הידע הזה, אפשר ללכת ולפתור משוואות "אמיתיות"! כלומר... כאלו שמופיעות בספרי לימוד. למשל, {% equation %}4x+7=19{% endequation %}. כדי לפתור את המשוואה הזו, נעביר את 7 אגף ונקבל {% equation %}4x=12{% endequation %} ואז נחלק ב-4 ונקבל {% equation %}x=3{% endequation %}. מה שהלך כאן היה בעצם זהה לגמרי לפתרון המשוואה {% equation %}30x+50=200{% endequation %} שממנה התחלתי; רק המספרים היו שונים. שיטת הפתרון הייתה זהה. אז אולי אפשר לנסח את השיטה הזו בצורה כללית?

נניח שיש לי משוואה מהצורה הבאה: {% equation %}ax+b=c{% endequation %} כאשר {% equation %}a,b,c{% endequation %} הם מספרים ואני מניח ש-{% equation %}a\ne0{% endequation %} (אחרת איקס לא באמת משתתף במשוואה). אז כדי לפתור אותה אני מעביר את {% equation %}b{% endequation %} אגף ומחלק ב-{% equation %}a{% endequation %} ומקבל את הפתרון {% equation %}x=\frac{c-b}{a}{% endequation %}. לרוב מעדיפים לנסח את הסיטואציה בצורה טיפה <strong>פחות</strong> כללית: אומרים - נניח שיש לנו משוואה מהצורה {% equation %}ax+b=0{% endequation %}, הבה ונפתור אותה. הפתרון במקרה הזה הוא פשוט {% equation %}x=-\frac{b}{a}{% endequation %} (תציבו {% equation %}c=0{% endequation %} בפתרון הקודם ותקבלו את זה). זה מתווה לנו דרך פעולה לפתרון משוואות כאלו באופן כללי: קודם כל לסדר אותן כך שיהיו מהצורה {% equation %}ax+b=0{% endequation %}, ואז להשתמש בנוסחה הזו, שעכשיו אנחנו מבינים מאיפה הגיעה.

כמובן, לא צריך ללכת למחוזות אבסורדיים. אם למשל נותנים לנו את המשוואה {% equation %}2x=10{% endequation %} אנחנו פשוט נחלק ב-{% equation %}2{% endequation %} ונקבל {% equation %}x=5{% endequation %}; לא קודם כל נעביר את 10 אגף כדי לקבל {% equation %}2x-10=0{% endequation %} ונגיד "אה-הא! הנה משוואה עם {% equation %}a=2{% endequation %} ו-{% equation %}b=-10{% endequation %} ולכן על פי הנוסחה הפתרון הוא {% equation %}x=-\frac{b}{a}=-\frac{-10}{2}=5{% endequation %}". הגיון פשוט הוא תמיד משהו שעדיף להסתמך עליו כשפותרים משוואות; פשוט לא חייבים.

הנה דוגמא קצת יותר מסובכת: המשוואה {% equation %}\frac{1}{1-x}=2{% endequation %}. כדי לפשט את המשוואה הזו, צריך לכפול ב-{% equation %}1-x{% endequation %} שבמכנה של אגף שמאל. אבל בניגוד למה שעשינו עד כה, לכפול ב-{% equation %}1-x{% endequation %} זה לא בדיוק לכפול במספר - זה לכפול <strong>במספר שתלוי</strong> ב-{% equation %}x{% endequation %}. אנחנו יודעים שאסור לכפול ב-0, ולכן אסור לכפול ב-{% equation %}1-x{% endequation %} במקרה שבו {% equation %}1-x=0{% endequation %}, כלומר במקרה שבו {% equation %}x=1{% endequation %}. אז מה עושים? מטפלים במקרה הזה בנפרד. ראשית כל שמים לב לכך שאם {% equation %}x=1{% endequation %} אז {% equation %}\frac{1}{1-x}{% endequation %} הוא ביטוי לא מוגדר כי אסור לחלק באפס, ולכן בוודאי שאינו שווה 2, ולכן {% equation %}x=1{% endequation %} לא יכול להיות פתרון של המשוואה. כעת אנחנו אומרים במפורש "נניח ש-{% equation %}x\ne1{% endequation %}" ואז נכפול ב-{% equation %}1-x{% endequation %} ונקבל {% equation %}1=2\left(1-x\right){% endequation %}, כלומר {% equation %}1=2-2x{% endequation %}. נעביר את {% equation %}2x{% endequation %} ואת {% equation %}1{% endequation %} אגפים ונקבל {% equation %}2x=1{% endequation %}, כלומר {% equation %}x=\frac{1}{2}{% endequation %}, וזה פתרון המשוואה.

האם זה סוף הסיפור? לא, זה סוף השלב הראשון בלבד. למשוואה מהצורה {% equation %}ax+b=0{% endequation %} (ומשוואות דומות ששקולות לה בקלות כמו {% equation %}ax+b=c{% endequation %}) קוראים <strong>משוואה ממעלה ראשונה</strong>. למה? כי הנה למשל דוגמא למשוואה ממעלה <strong>שניה</strong>: {% equation %}x^{2}+2x+1=0{% endequation %}. כאן {% equation %}x{% endequation %} מופיע גם בחזקה שניה, ומכאן מגיעה ה"מעלה שניה". לפתור משוואות כאלו זה כבר יותר מסובך ולכן צריך לדבר על זה בפוסט נפרד. משוואות ממעלה יותר גבוהה כמו {% equation %}x^{3}+3x+3+1=0{% endequation %} זה כבר סיפור <strong>הרבה</strong> יותר מסובך ואין פתרון כללי נחמד שאותו אפשר ללמד, אבל יש טריקים שעוזרים מאוד במקרים מסויימים. וחוץ מכל זה, אפשר לדבר גם על משוואות עם <strong>יותר מנעלם אחד</strong>, למשל {% equation %}x+y=5{% endequation %}, ואז יכולים להיות למשוואה הרבה פתרונות שונים, ולעתים קרובות מדברים על <strong>מערכת של משוואות</strong> שבה יש יותר ממשוואה אחת שצריך לפתור בו זמנית.

במילים אחרות, העולם של פתרון המשוואות הוא גדול ועשינו בו רק את הצעד הראשון, אבל זה צעד חשוב; הטכניקה הזו של "לבצע את אותה פעולה על שני האגפים" ממשיכה לעזור לנו גם בסיטואציות המורכבות יותר. 