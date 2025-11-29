---
title: "אז מה זה בעצם המספרים הממשיים? (חלק ד': בונים את המספרים הממשיים עם סדרות קושי)"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - מספרים ממשיים
---


<h2>מבוא</h2>

סדרת הפוסטים שלי על המספרים הממשיים כבר אמרה המון דברים על המספרים הממשיים חוץ מדבר בסיסי אחד: מהם המספרים הממשיים. קיבלנו אינטואיציה וקיבלנו רשימת תכונות שאנחנו <strong>מצפים</strong> שהמספרים הממשיים יקיימו, אבל לא קיבלו בניות קונקרטיות שלהם. בפוסט הזה סוף סוף נגיע להגדרה פורמלית: זו של קנטור שמסתמכת על <strong>סדרות</strong>. בנוסף להגדרה הזו יש גם את ההגדרה של דדקינד שמסתמכת על <strong>חתכים</strong>, אבל אני דוחה אותה לפוסט הבא כי ההוכחה שהיא עובדת היא טכנית להחריד (אפילו יותר מהדברים הטכניים להחריד שיהיו בהמשך הפוסט הזה) וסדר ההצגה של דברים בה הוא שונה, כך שבפוסט הזה אני אתמקד על הבניה של קנטור שהיא קצת יותר קלה לעיכול מבחינת הפרטים הטכניים.

לפני שנתחיל, בואו ניזכר שוב מה היה האפיון שנתתי למספרים הממשיים: המספרים הממשיים הם <strong>השדה הסדור השלם</strong>. כאשר "שדה", "סדור" ו"שלם" כולם מוגדרים על ידי <strong>אקסיומות</strong> (תכונות בסיסיות שאנחנו מצפים מהאובייקט שלנו לקיים אם הוא רוצה להיקרא "שדה", "סדור", "שלם") והשימוש שלי בה' הידיעה הוצדק על ידי הוכחה שיש בדיוק אובייקט אחד (עד כדי איזומורפיזם) שמקיים את כל האקסיומות הללו.

זה אומר מה בעצם אני צריך לעשות בפוסט הזה והבא אחריו: לא סתם להציג בניה, אלא להסביר או אפילו להוכיח עד הסוף למה הבניה מקיימות את כל האקסיומות הללו (בכך זה שונה מאוד מפעמים אחרות שבהן הזכרתי את הבניות בבלוג; אף פעם לא הראיתי שהן מקיימות את האקסיומות, כלומר שהן עושות את מה שהן אמורות לעשות). לכן נתחיל עם להזכיר את רשימת כל האקסיומות:

האובייקט הבסיסי שלנו מסומן ב-{% equation %}\mathbb{F}{% endequation %} והוא פשוט קבוצה. אנחנו אומרים שהוא <strong>שדה</strong> אם בנוסף ל-{% equation %}\mathbb{F}{% endequation %} מוגדרות לנו שתי פונקציות בינאריות על {% equation %}\mathbb{F}{% endequation %} (פונקציות בינאריות: מקבלות שני קלטים ומחזירות פלט אחד) שמסומנות ב-"{% equation %}+{% endequation %}" וב-"{% equation %}\cdot{% endequation %}" כך שמתקיימות התכונות הבאות:

<ul> <li>{% equation %}\left(A+B\right)+C=A+\left(B+C\right){% endequation %}</li>


<li>{% equation %}\left(A\cdot B\right)\cdot C=A\cdot\left(B\cdot C\right){% endequation %}</li>


<li>{% equation %}A+B=B+A{% endequation %}</li>


<li>{% equation %}A\cdot B=B\cdot A{% endequation %} </li>


<li>{% equation %}A\cdot\left(B+C\right)=A\cdot B+A\cdot C{% endequation %}</li>


<li>קיים איבר שמסומן ב-0 כך ש-{% equation %}A+0=A{% endequation %} לכל {% equation %}A{% endequation %}</li>


<li>לכל {% equation %}A{% endequation %} קיים איבר שמסומן ב-{% equation %}-A{% endequation %} ונקרא <strong>הנגדי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A+\left(-A\right)=0{% endequation %}</li>


<li>קיים איבר שמסומן ב-{% equation %}1{% endequation %} כך ש-{% equation %}0\ne1{% endequation %} ו-{% equation %}A\cdot1=A{% endequation %} לכל {% equation %}A{% endequation %}</li>


<li>לכל {% equation %}A\ne0{% endequation %} קיים איבר שמסומן ב-{% equation %}A^{-1}{% endequation %} ונקרא <strong>ההופכי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A\cdot A^{-1}=1{% endequation %}</li>

</ul>

עבור שדה סדור דרשנו בנוסף את הקיום של קבוצה {% equation %}P\subseteq\mathbb{F}{% endequation %} שאינטואיטיבית אנחנו חושבים על אבריה בתור "המספרים החיוביים" שמקיימת:

<ul> <li>לכל {% equation %}A\in\mathbb{F}{% endequation %} בדיוק אחד מהבאים מתקיים: או ש-{% equation %}A\in P{% endequation %}, או ש-{% equation %}-A\in P{% endequation %}, או ש-{% equation %}A=0{% endequation %}.</li>


<li>אם {% equation %}A,B\in P{% endequation %} אז {% equation %}A+B\in P{% endequation %}</li>


<li>אם {% equation %}A,B\in P{% endequation %} אז {% equation %}A\cdot B\in P{% endequation %}</li>

</ul>

לבסוף, <strong>אקסיומת השלמות</strong> הייתה האקסיומה הבאה:

<ul> <li>אם {% equation %}A\subseteq\mathbb{F}{% endequation %} היא קבוצה לא ריקה וחסומה מלעיל, אז {% equation %}\sup A{% endequation %} קיים.</li>

</ul>

בפוסט הקודם ראינו שהאקסיומה הזו <strong>שקולה</strong> לזוג אקסיומות אחר:

<ul> <li>(ארכימדיות) לכל {% equation %}A\in\mathbb{F}{% endequation %} קיים {% equation %}N\in\mathbb{N}{% endequation %} כך ש-{% equation %}A<N{% endequation %}</li>


<li>(שלמות-קנטור) כל סדרת קושי מתכנסת</li>

</ul>

אני לא מסביר לעומק מה כל האקסיומות אומרות כי כבר דיברנו על זה בפירוט בפוסטים הקודמים ועוד נעשה את זה בפירוט בהמשך, כחלק מההוכחות עצמן. בואו נעבור לראות את הבניה עצמה.

<h2>הבניה של קנטור למספרים הממשיים</h2>

קנטור ודדקינד לוקחים שניהם בתור נקודת מוצא את הרציונליים, {% equation %}\mathbb{Q}{% endequation %}, ויש לכך סיבות טובות. ראשית, זה שדה סדור, כלומר אנחנו "כמעט שם" ורק נותרה לנו עוד אקסיומה אחת; אפשר להראות ש-{% equation %}\mathbb{Q}{% endequation %} יהיה מוכל בכל שדה סדור כך שהוא בסיס טוב לצאת ממנו; ועם הבניה של {% equation %}\mathbb{Q}{% endequation %} אין לנו שום בעיות והיא די פשוטה.

מה שדדקינד וקנטור עושים, וזה רעיון מקסים שחוזר על עצמו שוב ושוב במתמטיקה, הוא לבנות את האובייקט החדש <strong>בתור</strong> האובייקטים הקיים שכרגע חסר בו משהו. דדקינד אומר - יש לנו קבוצות של רציונליים שנראה שאמור להיות להן חסם עליון אבל אין? יופי, הקבוצות הללו <strong>יהיו</strong> המספר הממשי שהוא החסם העליון הזה. קנטור אומר - יש לנו סדרות קושי שנראה שאמורות להתכנס לאנשהו אבל אין להן גבול? יופי, הסדרות הללו <strong>יהיו</strong> המספר הממשי שהוא הגבול הזה. זה נראה כמו רמאות גמורה, אבל כשפורטים את זה לפרטים ברור שאין כאן שום רמאות והכל תקין מבחינה פורמלית. גם מבחינה רעיונית אפשר להבין את זה: האובייקט שממנו מתחילים, זה שמצביע על החסר, בעצם כולל את <strong>האינפורמציה</strong> שנראית לנו רלוונטית עבור המספר החדש; לכן הוא האובייקט הכי מתאים כדי להגדיר את המספר החדש הזה.

בואו נראה את הדוגמא הקלאסית עם המספר האי-רציונלי {% equation %}\sqrt{2}=1.41421\ldots{% endequation %}. זה מספר אי רציונלי, אבל יש סדרת מספרים רציונליים פשוטה ששואפת אליו: {% equation %}1,1.4,1.41,1.414,1.4142,1.41421,\ldots{% endequation %}. לא קשה להראות שהסדרה הזו היא <strong>סדרת קושי</strong> ולכן אם אנחנו רוצים שתתקיים שלמות-קנטור צריך להיות לה גבול ביקום המתמטי שלנו - אז אנחנו <strong>מגדירים</strong> מספר חדש באמצעות הסדרה הזו. לכאורה המספר החדש הזה הולך להיות {% equation %}\sqrt{2}{% endequation %}, אבל אי אפשר סתם להגיד את זה - צריך להשתכנע שהמספר החדש שבנינו, אחרי שכופלים אותו בעצמו, יוצא שווה ל-2. כלומר צריך להבין איך מבצעים פעולות אלגבריות על האובייקטים החדשים שלנו, ומתי שני אובייקטים הם שווים, ואיך בכלל "2" מוגדר בגישה שלנו (ובכן, בעזרת הסדרה {% equation %}2,2,2,2,\ldots{% endequation %}, למשל).

לכאורה ההגדרה שלנו פשוטה: כל איבר של {% equation %}\mathbb{F}{% endequation %} יהיה סדרת קושי של רציונליים. אבל ההגדרה הזו לא מספיק טובה כי יכולות להיות <strong>הרבה</strong> סדרות קושי שונות ש"מתכנסות לאותו איבר". הדוגמא הקלאסית היא הסדרה הקבוצה {% equation %}1,1,1,\ldots{% endequation %} והסדרה {% equation %}0.9,0.99,0.999,\ldots{% endequation %} <a href="https://gadial.net/2008/06/07/almost_1_is_one/">שהקדשתי לה כבר פוסט</a> , אבל הבעיה הרבה יותר עמוקה מזה. למשל, אפילו אם אני אקח את {% equation %}1,1,1\ldots{% endequation %} לבדה ופתאום באיבר ה-54,527,822 אשנה אותו ל-42 וכל יתר הסדרה תהיה 1 - קיבלתי סדרת קושי שמתכנסת אל 1, אבל היא שונה מהסדרה שכולה 1-ים. ואפשר גם להסתכל על סדרה כמו {% equation %}a_{n}=1-\frac{1}{2^{n}}{% endequation %} שמתכנסת גם היא אל 1 אבל בצורה שונה, ועוד ועוד ועוד.

מה שקנטור אומר הוא - אוקיי, אז בואו לא ניקח סדרת קושי אחת ספציפית בתור מספר ממשי; בואו ניקח את <strong>כל</strong> הסדרות שמתכנסות לאותו מספר להיות המספר עצמו. פורמלית אנחנו יכולים לתאר את זה עם המושג של <strong>יחס שקילות</strong> (מושג <a href="https://gadial.net/2020/01/06/equivalence_relations/">שיש לי עליו פוסט בבלוג</a> וכאן אני אניח שהוא מוכר).

איך מגדירים יחס שקילות שאומר "שתי סדרות הקושי הללו מתכנסות לאותו דבר" כשאין "דבר" שהן מתכנסות אליו? פשוט אומרים שהן מתקרבות מספיק אחת לשניה: אם {% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty},\left\{ b_{n}\right\} _{n=0}^{\infty}{% endequation %} הן שתי סדרות קושי, נאמר שהן <strong>שקולות</strong> אם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|a_{n}-b_{n}\right|<\varepsilon{% endequation %}.

קל לראות שזה יחס שקילות: הוא רפלקסיבי כי {% equation %}\left|a_{n}-a_{n}\right|=0{% endequation %} לכל {% equation %}n{% endequation %}; הוא סימטרי כי {% equation %}\left|a_{n}-b_{n}\right|=\left|b_{n}-a_{n}\right|{% endequation %} לכל {% equation %}n{% endequation %}. טרנזיטיביות היא טיפה יותר עבודה טכנית אבל שום דבר חכם במיוחד: אם {% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty},\left\{ b_{n}\right\} _{n=0}^{\infty}{% endequation %} שקולות וגם {% equation %}\left\{ b_{n}\right\} _{n=0}^{\infty},\left\{ c_{n}\right\} _{n=0}^{\infty}{% endequation %} שקולות נראה ש-{% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty},\left\{ c_{n}\right\} _{n=0}^{\infty}{% endequation %} שקולות על פי הגדרה. יהא {% equation %}\varepsilon>0{% endequation %} כלשהו, אז קיים {% equation %}N_{1}{% endequation %} כך ש-{% equation %}\left|a_{n}-b_{n}\right|<\frac{\varepsilon}{2}{% endequation %} לכל {% equation %}n>N_{1}{% endequation %} וקיים {% equation %}N_{2}{% endequation %} כך ש-{% equation %}\left|b_{n}-c_{n}\right|<\frac{\varepsilon}{2}{% endequation %} לכל {% equation %}n>N_{2}{% endequation %} ולכן אם נגדיר {% equation %}N=\max\left\{ N_{1},N_{2}\right\} {% endequation %} אז לכל {% equation %}n>N{% endequation %} מתקיים

{% equation %}\left|a_{n}-c_{n}\right|=\left|a_{n}-b_{n}+b_{n}-c_{n}\right|\le\left|a_{n}-b_{n}\right|+\left|b_{n}-c_{n}\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon{% endequation %}

וזה מה שרצינו. אז יש לנו יחס שקילות, ואם יש לנו יחס שקילות יש לנו מחלקות שקילות, כלומר חלוקה של אוסף <strong>כל</strong> סדרות הקושי הרציונליות לקבוצות כך שכל האיברים של קבוצה שקולים זה לזה ולא שקולים לאיברים של אף קבוצה אחרת. אוסף מחלקות השקילות הזה הוא מה שקנטור מגדיר בתור {% equation %}\mathbb{F}{% endequation %}. ושוב, טרם הגדרנו חיבור או כפל או איברים חיוביים, אז בינתיים אין לנו אקסיומות כלשהן להראות שמתקיימות, אבל כן קל לראות ש-{% equation %}\mathbb{Q}\subseteq\mathbb{F}{% endequation %} כי לכל רציונלי {% equation %}x\in\mathbb{Q}{% endequation %} פשוט ניקח את מחלקת השקילות של הסדרה {% equation %}x,x,x,\ldots{% endequation %}.

<h2>חיבור וכפל של סדרות קושי</h2>

הגישה הסטנדרטית כשבונים אובייקט חדש מתוך אובייקט קיים שבא להרחיב אותו הוא שלא מתחילים מאפס, ומשתמשים במבנה שיש לאובייקט הקיים כדי ליצור את המבנה של האובייקט החדש. אצלנו זה אומר שאת פעולות החיבור והכפל של ממשיים נגדיר באמצעות פעולות החיבור והכפל של רציונליים, שאנחנו כבר מכירים. ברור לנו לגמרי איך לחבר ולכפול כי אנחנו יודעים לחבר ולכפול סדרות: עושים את זה "איבר-איבר". רק מה, יש לנו סיבוך בלתי נמנע שנובע מכך שאנחנו מגדירים את הממשיים לא בתור <strong>סדרות</strong> אלא בתור <strong>מחלקות שקילות</strong> של סדרות. עוד סיבוך נובע מכך שאנחנו לא סתם עובדים עם<strong> </strong>סדרות אלא עם <strong>סדרות קושי</strong> ולכן גם תוצאת החיבור והכפל צריכה להיות סדרת קושי. זה לא יהיה סיבוך נוראי אבל נצטרך טיפה לעבוד.

קודם כל בואו נכניס לתמונה סימונים שיקלו עלינו את החיים. סימנתי סדרה עד כה ב-{% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty}{% endequation %}, אבל בואו נחסוך כתיבה מיותרת ופשוט נסמן אותה ב-{% equation %}a{% endequation %}. עכשיו אפשר להגדיר סכום וכפל של סדרות באופן הבא:

<ul> <li>{% equation %}a+b=c{% endequation %} כאשר {% equation %}c_{n}=a_{n}+b_{n}{% endequation %}</li>


<li>{% equation %}a\cdot b=c{% endequation %} כאשר {% equation %}c_{n}=a_{n}\cdot b_{n}{% endequation %}</li>

</ul>

כלומר, החיבור והכפל הם "נקודתיים", איבר-איבר.

עכשיו נעבור לדבר על מחלקות שקילות: דרך סטנדרטית לסמן מחלקת שקילות היא באמצעות <strong>נציג</strong>: ניקח סדרה {% equation %}a{% endequation %} ונסמן

{% equation %}A=\left[a\right]\triangleq\left\{ a^{\prime}\ |\ a\sim a^{\prime}\right\} {% endequation %}

כאשר אצלנו כזכור {% equation %}a\sim a^{\prime}{% endequation %} פירושו שלכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|a_{n}-a_{n}^{\prime}\right|<\varepsilon{% endequation %}. כלומר, אנחנו מתארים את המחלקה בתור "כל האיברים ששקולים אל {% equation %}a{% endequation %}" - במקרה הזה {% equation %}a{% endequation %} הוא <strong>הנציג</strong> של המחלקה.

בואו ניסגר על הסימונים שלנו. כשאני כותב {% equation %}a_{n}{% endequation %} אני כותב מספר רציונלי - איבר של הסדרה {% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty}{% endequation %}. כשאני כותב {% equation %}a{% endequation %}, זה קיצור במקום לכתוב {% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty}{% endequation %}, וכשאני כותב {% equation %}A{% endequation %} אני מתכוון למספר ממשי: מחלקת שקילות של סדרות קושי. כשאני כותב {% equation %}A=\left[a\right]{% endequation %} אני בוחר לייצג את {% equation %}A{% endequation %} באמצעות הנציג הקונקרטי {% equation %}a{% endequation %}, ולעתים קרובות אני לא אטרח לכתוב את {% equation %}A{% endequation %} במפורש אלא אכתוב פשוט {% equation %}\left[a\right]{% endequation %} מלכתחילה, שזו דרך לומר "המספר הממשי שאני מייצג כרגע עם {% equation %}a{% endequation %}".

עכשיו אפשר להגדיר חיבור וכפל של ממשיים, כלומר של מחלקות השקילות, על ידי נציגים:

<ul> <li>{% equation %}\left[a\right]+\left[b\right]=\left[a+b\right]{% endequation %}</li>


<li>{% equation %}\left[a\right]\cdot\left[b\right]=\left[a\cdot b\right]{% endequation %}</li>

</ul>

כלומר: רוצים לחבר/לכפול שני ממשיים? קחו סדרת קירובים כלשהי לכל אחד מהם, חברו/כפלו את סדרת הקירובים והופס, קיבלתם סדרת קירובים למספר שהוא החיבור/כפל של הממשיים שהתחלתם איתם.

עד כאן הכל טוב, אבל בכל פעם שבה מגדירים פונקציה על מחלקות שקילות שמתבססת על הנציגים שלהן, יש את הסכנה שעבור נציגים <strong>שונים</strong> נקבל תוצאות <strong>שונות</strong>, וזה יאמר שהפונקציה שאנחנו מגדירים היא <strong>לא מוגדרת היטב</strong> כי על אותו הקלט (זוג ממשיים) היא יכולה להחזיר יותר מפלט אחד (כלומר, כמה ממשיים שונים) בהתאם לנציגים שאנחנו לוקחים.

אז בואו נראה שזה לא יכול לקרות, בצורה הסטנדרטית. לכל מחלקה ניקח <strong>שני</strong> נציגים, ונראה שהתוצאה זהה גם עבור זוג הנציגים הראשון וגם עבור זוג הנציגים השני.

פורמלית, ניקח {% equation %}a,a^{\prime}{% endequation %} כך ש-{% equation %}\left[a\right]=\left[a^{\prime}\right]{% endequation %}, ניקח {% equation %}b,b^{\prime}{% endequation %} כך ש-{% equation %}\left[b\right]=\left[b^{\prime}\right]{% endequation %} ונוכיח ש:

<ul> <li>{% equation %}\left[a+b\right]=\left[a^{\prime}+b^{\prime}\right]{% endequation %}</li>


<li>{% equation %}\left[a\cdot b\right]=\left[a^{\prime}\cdot b^{\prime}\right]{% endequation %}</li>

</ul>

נתחיל מהמקרה הראשון. אם "נקלף" את הרמה של מחלקות השקילות, נראה שמה שצריך להוכיח פה הוא בעצם שאם {% equation %}a\sim a^{\prime}{% endequation %} וגם {% equation %}b\sim b^{\prime}{% endequation %} אז {% equation %}a+b\sim a^{\prime}+b^{\prime}{% endequation %}. כלומר, נתחיל עם "יהי {% equation %}\varepsilon>0{% endequation %}" כרגיל ונמצא {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|\left(a_{n}+b_{n}\right)-\left(a_{n}^{\prime}+b_{n}^{\prime}\right)\right|<\varepsilon{% endequation %}. בשלב הזה אני מקווה שאנחנו ממש מתורגלים כבר בשטיק הזה. עושים:

{% equation %}\left|\left(a_{n}+b_{n}\right)-\left(a_{n}^{\prime}+b_{n}^{\prime}\right)\right|=\left|\left(a_{n}-a_{n}^{\prime}\right)+\left(b_{n}-b_{n}^{\prime}\right)\right|\le\left|a_{n}-a_{n}^{\prime}\right|+\left|b_{n}-b_{n}^{\prime}\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon{% endequation %}

כשהמעברים הללו עובדים עבור {% equation %}N=\max\left\{ N_{1},N_{2}\right\} {% endequation %} כש-{% equation %}N_{1}{% endequation %} הוא מה שמבטיח {% equation %}\left|a_{n}-a_{n}^{\prime}\right|<\frac{\varepsilon}{2}{% endequation %} ו-{% equation %}N_{2}{% endequation %} מבטיח את זה עבור ה-{% equation %}b{% endequation %}-ים.

כפל מצריך טריק אלגברי קטן:

{% equation %}\left|a_{n}b_{n}-a_{n}^{\prime}b_{n}^{\prime}\right|=\left|\left(a_{n}-a_{n}^{\prime}\right)b_{n}+a_{n}^{\prime}\left(b_{n}-b_{n}^{\prime}\right)\right|\le\left|b_{n}\right|\left|a_{n}-a_{n}^{\prime}\right|+\left|a_{n}^{\prime}\right|\left|b_{n}-b_{n}^{\prime}\right|{% endequation %}

זה טיפה מסבך לנו את החיים כי לא מספיק לחסום את {% equation %}\left|a_{n}-a_{n}^{\prime}\right|{% endequation %} ואת {% equation %}\left|b_{n}-b_{n}^{\prime}\right|{% endequation %} כמו קודם: צריך לחסום גם את {% equation %}\left|b_{n}\right|{% endequation %} ואת {% equation %}\left|a_{n}^{\prime}\right|{% endequation %}. זו לא בעיה אמיתית כי סדרות קושי הן חסומות: אם {% equation %}a{% endequation %} היא סדרת קושי, אז קיים {% equation %}N{% endequation %} כל שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|a_{n}-a_{N}\right|<1{% endequation %}, כלומר 

{% equation %}\left|a_{n}\right|=\left|a_{n}-a_{N}+a_{N}\right|\le\left|a_{n}-a_{N}\right|+\left|a_{N}\right|<\left|a_{N}\right|+1{% endequation %}

לכן בכללי אפשר להניח שעבור {% equation %}N{% endequation %} גדול מספיק נקבל לכל {% equation %}n>N{% endequation %} ש-{% equation %}\left|b_{n}\right|<M{% endequation %} וגם {% equation %}\left|a_{n}^{\prime}\right|<M{% endequation %} עבור {% equation %}M{% endequation %} כלשהו. עכשיו נמצא {% equation %}N{% endequation %} גדול דיו כך שהאפקט הזה מתקיים <strong>וגם</strong> {% equation %}\left|a_{n}-a_{n}^{\prime}\right|<\frac{\varepsilon}{2M}{% endequation %} <strong>וגם {% equation %}</strong>\left|b_{n}-b_{n}^{\prime}\right|<\frac{\varepsilon}{2M}{% endequation %}, ולכן נקבל

{% equation %}\left|a_{n}b_{n}-a_{n}^{\prime}b_{n}^{\prime}\right|=\le\left|b_{n}\right|\left|a_{n}-a_{n}^{\prime}\right|+\left|a_{n}^{\prime}\right|\left|b_{n}-b_{n}^{\prime}\right|<M\cdot\frac{\varepsilon}{2M}+M\cdot\frac{\varepsilon}{2M}=\varepsilon{% endequation %}

מה שמסיים את ההוכחה שהחיבור והכפל מוגדרים היטב. למרבה השמחה, כדי להוכיח שהסכום והכפל של סדרות קושי הוא סדרת קושי אנחנו בעצם עושים <strong>את אותו דבר בדיוק</strong> כך שטיפלנו בשתי הבעיות שלנו במחיר אחת. כדי לראות את זה, בואו נחשוב מה בעצם אנחנו רוצים להוכיח: שלכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n,m>N{% endequation %} אז

<ul> <li>{% equation %}\left|\left(a_{n}+b_{n}\right)-\left(a_{m}+b_{m}\right)\right|<\varepsilon{% endequation %}</li>


<li>{% equation %}\left|\left(a_{n}b_{n}\right)-\left(a_{m}b_{m}\right)\right|<\varepsilon{% endequation %}</li>

</ul>

תחליפו את {% equation %}a_{m},b_{m}{% endequation %} ב-{% equation %}a_{n}^{\prime},b_{n}^{\prime}{% endequation %} וחזרנו להוכחה שכבר ראינו. אותן טכניקות עובדות בדיוק; לב העניין הוא בכך שכמו ש-{% equation %}a_{n},a_{n}^{\prime}{% endequation %} קרובים מספיק עבור {% equation %}n{% endequation %}-ים גדולים מספיק, כך גם {% equation %}a_{n},a_{m}{% endequation %} קרובים מספיק עבור {% equation %}n,m{% endequation %}-ים גדולים מספיק. זה מסיים עבורנו את ההגדרה של חיבור וכפל של מספרים ממשיים בגישה של קנטור (אבל הפעם לא הגדרנו על הדרך מתי איבר הוא חיובי או מה המינוס של איבר, עוד נצטרך להגיע אל זה).

<h2>אסוציאטיביות, קומוטטיביות, דיסטריביוטיביות</h2>

הגדרנו את פעולות החיבור והכפל ועכשיו אפשר להוכיח שהן מקיימות את התכונות הבסיסיות שנדרשות מהן בשדה:

<ul> <li>{% equation %}\left(A+B\right)+C=A+\left(B+C\right){% endequation %}</li>


<li>{% equation %}\left(A\cdot B\right)\cdot C=A\cdot\left(B\cdot C\right){% endequation %}</li>


<li>{% equation %}A+B=B+A{% endequation %}</li>


<li>{% equation %}A\cdot B=B\cdot A{% endequation %} </li>


<li>{% equation %}A\cdot\left(B+C\right)=A\cdot B+A\cdot C{% endequation %}</li>


<li>קיים איבר שמסומן ב-0 כך ש-{% equation %}A+0=A{% endequation %} לכל {% equation %}A{% endequation %}</li>

</ul>

מה שאנחנו יכולים להסתמך עליו הוא שכל התכונות הללו <strong>כבר נכונות</strong> עבור הממשיים, {% equation %}\mathbb{Q}{% endequation %}, וזה הולך מאוד להקל עלינו.

נוכיח למשל קומוטטיביות של חיבור. אני צריך להראות ש:

<ul> <li>{% equation %}\left[a\right]+\left[b\right]=\left[b\right]+\left[a\right]{% endequation %}</li>

</ul>

אבל זה קל: עבור שתי סדרות, {% equation %}a+b{% endequation %} היא הסדרה שהאיבר הכללי שלה הוא {% equation %}a_{n}+b_{n}{% endequation %}, אבל מקומוטטיביות הרציונליים, האיבר הכללי הזה שווה אל {% equation %}b_{n}+a_{n}{% endequation %} ולכן {% equation %}a+b=b+a{% endequation %} ולכן {% equation %}\left[a+b\right]=\left[b+a\right]{% endequation %}. כפל מתקבל באותו אופן בדיוק וגם דיסטריביוטיביות, אבל בואו נראה דיסטריביוטיביות במפורש כדי לא לדאוג שאנחנו מדלגים על משהו קריטי:

{% equation %}\left[a\right]\cdot\left(\left[b\right]+\left[c\right]\right)=\left[a\right]\cdot\left[b+c\right]=\left[a\left(b+c\right)\right]{% endequation %}

והאיבר הכללי של {% equation %}a\left(b+c\right){% endequation %}, על פי הגדרת חיבור וכפל סדרות, הוא {% equation %}a_{n}\left(b_{n}+c_{n}\right){% endequation %} ולכן, על פי דיסטריביוטיביות של רציונליים, שווה אל {% equation %}a_{n}b_{n}+a_{n}c_{n}{% endequation %} כלומר אל האיבר הכללי של {% equation %}ab+ac{% endequation %}, כמו שרצינו.

גם עבור אסוציאטיביות זה בעצם אותו דבר אבל כדאי לראות את זה בזהירות. מה זה {% equation %}\left(\left[a\right]+\left[b\right]\right)+\left[c\right]{% endequation %}, על פי הגדרה? זה {% equation %}\left[a+b\right]+\left[c\right]{% endequation %}, כלומר זה {% equation %}\left[\left(a+b\right)+c\right]{% endequation %} ושוב אנחנו מתדרדרים לאסוציאטיביות ברמת האיבר הכללי: {% equation %}\left(a_{n}+b_{n}\right)+c_{n}=a_{n}+\left(b_{n}+c_{n}\right){% endequation %} ומכאן מתקדמים כרגיל. אז עבור סדרות קושי הכל פשוט (עבור חתכי דדקינד השלב הזה יהיה גיהנום).

<h2>אדיש חיבורי וכפלי, נגדי, הופכי</h2>

עכשיו אנחנו רוצים להראות שמתקיימות האקסיומות הבאות:

<ul> <li>קיים איבר שמסומן ב-0 כך ש-{% equation %}A+0=A{% endequation %} לכל {% equation %}A{% endequation %}</li>


<li>לכל {% equation %}A{% endequation %} קיים איבר שמסומן ב-{% equation %}-A{% endequation %} ונקרא <strong>הנגדי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A+\left(-A\right)=0{% endequation %}</li>


<li>קיים איבר שמסומן ב-{% equation %}1{% endequation %} כך ש-{% equation %}0\ne1{% endequation %} ו-{% equation %}A\cdot1=A{% endequation %} לכל {% equation %}A{% endequation %}</li>


<li>לכל {% equation %}A\ne0{% endequation %} קיים איבר שמסומן ב-{% equation %}A^{-1}{% endequation %} ונקרא <strong>ההופכי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A\cdot A^{-1}=1{% endequation %}</li>

</ul>

מכיוון שאנחנו מרחיבים את השדה {% equation %}\mathbb{Q}{% endequation %} מתבקש שה-0 וה-1 שלנו יהיו גם אלו של {% equation %}\mathbb{Q}{% endequation %}, כלומר ניקח את 0 להיות מחלקת השקילות של סדרת הקושי {% equation %}0,0,0,\ldots{% endequation %} ואת {% equation %}1{% endequation %} להיות המחלקה של {% equation %}1,1,1,\ldots{% endequation %}. אלו בבירור סדרות קושי; הן בבירור לא שקולות זו לזו מכיוון שההפרש ביניהן הוא 1 באופן קבוע; ולכל סדרה אחרת מתקיים {% equation %}a+0=a{% endequation %} ו-{% equation %}a\cdot1=a{% endequation %} פשוט כי ברציונליים, {% equation %}a_{n}+0=a_{n}{% endequation %} ו-{% equation %}a_{1}\cdot1=a_{n}{% endequation %}. אז יש לנו את האדישים שלנו.

נגדי חיבורי יהיה קל גם כן: אם {% equation %}A=\left[a\right]{% endequation %} הוא מספר ממשי כלשהו, אני אגדיר {% equation %}-A=\left[-a\right]{% endequation %}. כרגיל, צריך להבהיר שזה מוגדר היטב, כלומר שאם {% equation %}a\sim a^{\prime}{% endequation %} אז {% equation %}-a\sim-a^{\prime}{% endequation %}; זה טריוויאלי כי המינוס הזה "נבלע" בתוך הערך המוחלט שמופיע בהגדרת השקילות. עכשיו נותר להראות ש-{% equation %}A+\left(-A\right)=0{% endequation %} וזה למרבה השמחה קל מאוד כי אנחנו יכולים לבחור איזה נציג שאנחנו רוצים ל-{% equation %}A{% endequation %} ול-{% equation %}-A{% endequation %} בגלל שהוכחנו בעמל רב שהגדרת החיבור לא תלויה בנציג: אז נבחר {% equation %}A=\left[a\right],-A=\left[-a\right]{% endequation %} ולכן

{% equation %}A+\left(-A\right)=\left[a\right]+\left[-a\right]=\left[a-a\right]=\left[0\right]=0{% endequation %}

ומה עם הופכי? הדבר המתבקש הוא לעשות את אותו קונץ, כלומר להגדיר {% equation %}A^{-1}=\left[a^{-1}\right]{% endequation %} כש-{% equation %}a^{-1}{% endequation %} מתקבל מהסדרה {% equation %}a{% endequation %} על ידי היפוך של כל איבר ב-{% equation %}a{% endequation %}, ואז יתקיים {% equation %}A\cdot A^{-1}=\left[a\right]\cdot\left[a^{-1}\right]=\left[aa^{-1}\right]=\left[1\right]=1{% endequation %}. אלא שכאן יש לנו בעיה: ראשית, כי הסדרה {% equation %}a{% endequation %} עלולה לכלול את 0, ואין לנו דרך להפוך אותו. אבל אפילו אם הסדרה לא כוללת את 0 בכלל עדיין יש לנו בעיה כי אנחנו צריכים ש-{% equation %}a^{-1}{% endequation %} תהיה <strong>סדרת קושי</strong>. אם הסדרה {% equation %}a{% endequation %} "מצטופפת" סביב 0, אפילו אם היא לא נוגעת בו בכלל, הערכים של {% equation %}a^{-1}{% endequation %} "מתפוצצים" - הם נהיים כל כך גדולים שהסדרה כבר לא תהיה סדרת קושי.

מה שאני רוצה להראות הוא שכל המקרים הבעייתיים הללו צצים רק במקרה שבו {% equation %}a\sim0{% endequation %}. מה שאנחנו הולכים אוטוטו להראות כשנדבר על יחס הסדר על הממשיים הוא שלכל ממשי {% equation %}A{% endequation %} קיים נציג {% equation %}a{% endequation %} שמקיים אחד משלושת הדברים הבאים:

<ol> <li>{% equation %}a\sim0{% endequation %}</li>


<li>קיים {% equation %}M>0{% endequation %} כך ש-{% equation %}a_{n}\ge M{% endequation %} לכל {% equation %}n>N{% endequation %} ("הסדרה חסומה חיובית הרחק מאפס")</li>


<li>קיים {% equation %}M>0{% endequation %} כך ש-{% equation %}a_{n}\le-M{% endequation %} לכל {% equation %}n>N{% endequation %} ("הסדרה חסומה שלילית הרחק מאפס")</li>

</ol>

זה משפט מועיל למדי כי הוא יאפשר לנו להגדיר את החיוביים בחלק הבא - אלו יהיו מן הסתם הממשיים שמיוצגים על ידי סדרה חסומה חיובית הרחק מאפס.

עכשיו, אם סדרה מקיימת את קריטריון 2 או 3 {% equation %}\left|a_{n}\right|\ge M>0{% endequation %} לכל אבריה ובפרט כל אבריה שונים מאפס, ולכן אפשר להגדיר סדרה חדשה, שנסמן {% equation %}a^{-1}{% endequation %}, שאבריה הם {% equation %}a_{n}^{-1}{% endequation %}. אבל למה זו סדרת קושי?

ובכן, בואו ניקח שני איברים כלליים של הסדרה וננסה להבין מה ההפרש ביניהם: 

{% equation %}\left|a_{n}^{-1}-a_{m}^{-1}\right|=\left|\frac{1}{a_{n}}-\frac{1}{a_{m}}\right|=\left|\frac{a_{m}-a_{n}}{a_{n}a_{m}}\right|=\frac{\left|a_{m}-a_{n}\right|}{\left|a_{n}\right|\left|a_{m}\right|}\le\frac{\left|a_{m}-a_{n}\right|}{M^{2}}{% endequation %}

זה פותר לנו את הבעיה: עבור {% equation %}\varepsilon>0{% endequation %} כלשהו, נפעיל את קריטריון קושי של הסדרה המקורית כדי למצוא {% equation %}N{% endequation %} עבורו לכל {% equation %}n,m>N{% endequation %} מתקיים {% equation %}\left|a_{n}-a_{m}\right|\le M^{2}\cdot\varepsilon{% endequation %}

התקדמנו יפה! סיימנו את כל מה שצריך כדי להראות שהקבוצה שבנינו היא שדה, ועכשיו אפשר לדבר על סדר.

<h2>שדה סדור</h2>

עכשיו אנחנו רוצים להגדיר תת-קבוצה {% equation %}P{% endequation %} של השדה שלנו, ולהראות שמתקיים:

<ul> <li>לכל {% equation %}A\in\mathbb{F}{% endequation %} בדיוק אחד מהבאים מתקיים: או ש-{% equation %}A\in P{% endequation %}, או ש-{% equation %}-A\in P{% endequation %}, או ש-{% equation %}A=0{% endequation %}.</li>


<li>אם {% equation %}A,B\in P{% endequation %} אז {% equation %}A+B\in P{% endequation %}</li>


<li>אם {% equation %}A,B\in P{% endequation %} אז {% equation %}A\cdot B\in P{% endequation %}</li>

</ul>

ההגדרה לזה טמונה במשפט שציטטתי קודם: לכל ממשי {% equation %}A{% endequation %} קיים נציג {% equation %}a{% endequation %} שמקיים בדיוק אחד משלושת הדברים הבאים:

<ol> <li>{% equation %}a\sim0{% endequation %}</li>


<li>קיים {% equation %}M>0{% endequation %} כך ש-{% equation %}a_{n}\ge M{% endequation %} לכל {% equation %}n>N{% endequation %} ("הסדרה חסומה חיובית הרחק מאפס")</li>


<li>קיים {% equation %}M>0{% endequation %} כך ש-{% equation %}a_{n}\le-M{% endequation %} לכל {% equation %}n>N{% endequation %} ("הסדרה חסומה שלילית הרחק מאפס")</li>

</ol>

כדי לראות את זה, בואו ניקח נציג כלשהו של {% equation %}A{% endequation %} ומכיוון ש-{% equation %}a{% endequation %} תפוס לתיאור הנציג המוצלח שאנחנו מחפשים, נקרא לו {% equation %}a^{\prime}{% endequation %}: {% equation %}A=\left[a^{\prime}\right]{% endequation %}. אם {% equation %}a^{\prime}\sim0{% endequation %} אז סיימנו; נגדיר {% equation %}a=a^{\prime}{% endequation %} וחסל. אחרת, מה אני יודע על {% equation %}a^{\prime}{% endequation %}? ראשית, הוא סדרת קושי. שנית, הוא לא מקיים {% equation %}a^{\prime}\sim0{% endequation %}. מה זה אומר? {% equation %}a^{\prime}\sim0{% endequation %} אומר שלכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N>0{% endequation %} כך שלכל {% equation %}m>N{% endequation %} מתקיים {% equation %}\left|a_{m}^{\prime}-0\right|<\varepsilon{% endequation %}. אם אני אומר שזה לא מתקיים, אני לוקח את השלילה הלוגית של הטענה הזו: זה אומר ש<strong>קיים</strong> {% equation %}\varepsilon>0{% endequation %} כך ש<strong>לכל</strong> {% equation %}N>0{% endequation %} <strong>קיים</strong> {% equation %}m>N{% endequation %} שעבורו מתקיים {% equation %}\left|a_{m}^{\prime}\right|\ge\varepsilon{% endequation %}. זה טוב, אבל לא מספיק למצוא איבר אחד - אני רוצה שכל האיברים של הסדרה החל ממקום מסוים יהיו מרוחקים מאפס. בשביל זה אני אשתמש בכך שזו סדרת קושי, ולכן עבור {% equation %}\frac{\varepsilon}{2}{% endequation %} קיים {% equation %}N{% endequation %} כך שלכל {% equation %}n,m>N{% endequation %} מתקיים {% equation %}\left|a_{n}^{\prime}-a_{m}^{\prime}\right|<\frac{\varepsilon}{2}{% endequation %}, ובמילים אחרות: {% equation %}a_{m}^{\prime}-\frac{\varepsilon}{2}<a_{n}^{\prime}<a_{m}^{\prime}+\frac{\varepsilon}{2}{% endequation %}.

עכשיו, אם {% equation %}a_{m}^{\prime}{% endequation %} הוא חיובי אז מ-{% equation %}\left|a_{m}^{\prime}\right|\ge\varepsilon{% endequation %} נקבל {% equation %}a_{m}^{\prime}\ge\varepsilon{% endequation %}, כלומר {% equation %}a_{n}^{\prime}>a_{m}^{\prime}-\frac{\varepsilon}{2}\ge\frac{\varepsilon}{2}{% endequation %}. אם לעומת זאת {% equation %}a_{m}^{\prime}{% endequation %} שלילי אז {% equation %}a_{m}^{\prime}\le-\varepsilon{% endequation %} ולכן {% equation %}a_{n}^{\prime}<a_{m}^{\prime}+\frac{\varepsilon}{2}\le-\frac{\varepsilon}{2}{% endequation %}. בכל מקרה קיבלנו ש-{% equation %}\left|a_{n}^{\prime}\right|\ge\frac{\varepsilon}{2}{% endequation %} לכל {% equation %}n>N{% endequation %}, ונשאר רק לסמן {% equation %}M=\frac{\varepsilon}{2}{% endequation %}.

עדיין לא סיימתי; מצאתי מקום {% equation %}N{% endequation %} שהחל ממנו, {% equation %}a^{\prime}{% endequation %} עונה לקריטריונים, אבל אני לא רוצה שזה יהיה <strong>החל ממקום מסויים</strong> אלא לכל אברי הסדרה - אז אני אגדיר סדרה חדשה שפשוט מתחילה מאותו המקום המסוים. פורמלית, אני מגדיר {% equation %}a_{n}=a_{N+n}^{\prime}{% endequation %}, ואז מובטח לי שאכן {% equation %}a_{n}\ge M{% endequation %} או לכל {% equation %}n{% endequation %} (או {% equation %}a_{n}\le-M{% endequation %} לכל {% equation %}n{% endequation %}), וברור ש-{% equation %}a_{n}{% endequation %} היא עדיין סדרת קושי כי היא הסיפא של סדרת קושי.

עכשיו ברור איך להגדיר את {% equation %}P{% endequation %} שלנו: היא תכלול את כל הממשיים {% equation %}A{% endequation %} שקיים להם נציג שמקיים את קריטריון 2.

נשאר להוכיח את שלוש האקסיומות. בשביל הראשונה, בואו ניקח {% equation %}A{% endequation %} כלשהו ונציג {% equation %}A=\left[a\right]{% endequation %} כלשהו. אם {% equation %}a\sim0{% endequation %} אז {% equation %}A=0{% endequation %}; אם {% equation %}a{% endequation %} מקיים את קריטריון 2 אז {% equation %}A\in P{% endequation %}; נשאר להראות שאם {% equation %}a{% endequation %} מקיים את קריטריון 3 אז {% equation %}-A\in P{% endequation %}, אבל זה מובן מאליו: {% equation %}-A=\left[-a\right]{% endequation %} ואם {% equation %}a_{n}\ge M{% endequation %} לכל {% equation %}n{% endequation %} אז {% equation %}-a_{n}\le-M{% endequation %} לכל {% equation %}n{% endequation %}.

בשביל שתי האקסיומות האחרות צריך להראות בעצם שאם {% equation %}a,b{% endequation %} סדרות שמקיימות את קריטריון 2, אז גם {% equation %}a+b{% endequation %} וגם {% equation %}ab{% endequation %} מקיימות את קריטריון 2. בשני המקרים נשתמש בקריטריון 2 כדי לקבל קיום של {% equation %}M_{a},M_{b}>0{% endequation %}כך ש-{% equation %}a_{n}\ge M_{a}{% endequation %} ו-{% equation %}b_{n}\ge M_{b}{% endequation %} לכל {% equation %}n{% endequation %}. עכשיו נחבר/נכפול את אי השוויונים ונקבל שלכל {% equation %}n{% endequation %} מתקיים {% equation %}a_{n}+b_{n}\ge M_{a}+M_{b}{% endequation %} ו-{% equation %}a_{n}b_{n}\ge M_{a}M_{b}{% endequation %} וסיימנו בזכות העובדה ש-{% equation %}M_{a}+M_{b}>0{% endequation %} וגם {% equation %}M_{a}M_{b}>0{% endequation %} - כלומר, תכונות 2,3 עבור הממשיים שאנחנו בונים נובעות בסופו של דבר מכך שהן מתקיימות עבור הרציונליים {% equation %}M_{a},M_{b}{% endequation %}.

עכשיו אפשר לשאול את עצמנו מתי, עבור שני ממשיים {% equation %}A,B{% endequation %}, מתקיים {% equation %}A<B{% endequation %}. כזכור, מרגע שהגדרנו את {% equation %}P{% endequation %} אנחנו מקבלים את {% equation %}<{% endequation %} "בחינם": {% equation %}A<B{% endequation %} על פי הגדרה אם {% equation %}B-A\in P{% endequation %}.

אז הגדרה יש לנות אבל לא יזיק אם יהיה לנו גם משפט שמקל עלינו להוכיח בפועל שמתקיים {% equation %}A<B{% endequation %} וכאן המצב יהיה טיפה טריקי. מה <strong>שהייתי רוצה</strong> להוכיח הוא שאם מצאתי נציגים {% equation %}a,b{% endequation %} ל-{% equation %}A,B{% endequation %} כך ש-{% equation %}a_{n}<b_{n}{% endequation %} לכל {% equation %}n{% endequation %} החל ממקום מסוים, אז {% equation %}A<B{% endequation %}, אלא שזה פשוט <strong>לא נכון</strong>: תסתכלו על הסדרות {% equation %}a_{n}=0{% endequation %} ו-{% equation %}b_{n}=\frac{1}{n}{% endequation %} למשל שמייצגות שתיהן את 0. מה <strong>שכן נכון</strong> הוא שאם {% equation %}a_{n}\le b_{n}{% endequation %} החל ממקום מסוים, אז {% equation %}A\le B{% endequation %}.

בואו נוכיח את זה. כלומר, יש לנו שתי סדרות {% equation %}a,b{% endequation %} ואני מניח ש-{% equation %}a_{n}\le b_{n}{% endequation %} החל ממקום מסוים. אז הסדרה {% equation %}b_{n}-a_{n}{% endequation %} היא נציג של {% equation %}B-A{% endequation %}. אם נסתכל על ההוכחה של הטענה הקודמת, הראינו שכל נציג של מספר ממשי הוא או שקול לאפס, או חסום הרחק מאפס החל ממקום מסוים. אם {% equation %}b_{n}-a_{n}\sim0{% endequation %} אז {% equation %}B-A=0{% endequation %}, כלומר {% equation %}B=A{% endequation %}; אחרת, {% equation %}b_{n}-a_{n}{% endequation %} חסום הרחק מאפס החל ממקום מסוים, וכמו כן {% equation %}a_{n}\le b_{n}{% endequation %} החל ממקום מסוים, כלומר {% equation %}b_{n}-a_{n}\ge0{% endequation %} החל ממקום מסוים, ולכן {% equation %}b_{n}-a_{n}{% endequation %} חסום <strong>חיובית</strong> הרחק מאפס החל ממקום מסוים, כלומר {% equation %}B-A>0{% endequation %} וקיבלנו {% equation %}A<B{% endequation %}. זה מסיים את ההוכחה הזו.

עוד דבר שאנחנו יכולים לדבר עליו עכשיו הוא ערך מוחלט. כזכור, הגדרנו

{% equation %}\left|A\right|=\begin{cases} A & A\ge0\\ -A & A<0 \end{cases}{% endequation %}

מושג הערך המוחלט מתקבל "בחינם" מרגע שיש לנו את {% equation %}P{% endequation %}, ובזכות אקסיומות השדה הסדור אנחנו גם מקבלים את התכונות המועילות שלו, למשל אי שוויון המשולש {% equation %}\left|A+B\right|\le\left|A\right|+\left|B\right|{% endequation %}.

סיימנו עם השדה הסדור! עכשיו אנחנו מגיעים סוף סוף למטרה שלשמה התכנסנו.

<h2>אקסיומת השלמות</h2>

בפוסט הקודם ראינו שעבור אקסיומת השלמות אנחנו יכולים להסתפק בלהוכיח שני דברים:

<ul> <li>(ארכימדיות) לכל {% equation %}A\in\mathbb{F}{% endequation %} קיים {% equation %}N\in\mathbb{N}{% endequation %} כך ש-{% equation %}A\le N{% endequation %}</li>


<li>(שלמות-קנטור) כל סדרת קושי מתכנסת</li>

</ul>

שלמות-קנטור נראית כמו משהו שטבעי יותר להוכיח מאשר את אקסיומת השלמות, כי כל הבנייה של קנטור את המספרים הממשיים מכוונת אליה: אנחנו לוקחים את האובייקט הבסיסי של סדרת קושי ו"מכריחים" את הגבול שלו להתקיים על ידי כך שאנחנו בונים אותו. בפועל העניינים לא כל כך פשוטים ותכף אסביר גם למה, אבל לפני זה בואו נטפל בארכימדיות.

בואו ניקח {% equation %}A=\left[a\right]{% endequation %} ממשי כלשהו עם נציג שרירותי {% equation %}a{% endequation %}. כל סדרת קושי של רציונליים היא חסומה, כלומר קיים {% equation %}q{% endequation %} רציונלי כך ש-{% equation %}a_{k}\le q{% endequation %} לכל {% equation %}k{% endequation %}. עכשיו אני אשתמש בארכימדיות של הרציונליים ואקבל שקיים {% equation %}n{% endequation %} טבעי כך ש-{% equation %}q\le n{% endequation %}. אני אגדיר את הממשי {% equation %}N{% endequation %} על ידי הסדרה הקבועה {% equation %}n,n,n,\ldots{% endequation %} - לא קשה להראות ש-{% equation %}N{% endequation %} הוא טבעי, כלומר הוא איבר של השדה {% equation %}\mathbb{F}{% endequation %} שלנו שאפשר לכתוב בתור {% equation %}1+1+\ldots+1{% endequation %}. עכשיו, מכיוון ש-{% equation %}a_{k}\le n{% endequation %} לכל {% equation %}k{% endequation %}, מהמשפט שהראיתי קודם נובע ש-{% equation %}A\le N{% endequation %}. אז ארכמדיות היה קל.

למה ששלמות-קנטור תהיה בעייתית? ניקח סדרת קושי {% equation %}a{% endequation %}, אז {% equation %}A=\left[a\right]{% endequation %} הוא הגבול שלה, לא? ככה בנינו את הממשיים. אבל הנה העניין: {% equation %}a{% endequation %} היא סדרת קושי של <strong>מספרים רציונליים</strong> ושלמות-קנטור שאנחנו רוצים להוכיח מדברת על התכנסות של סדרות קושי של <strong>מספרים ממשיים</strong>, כלומר על סדרות קושי של מחלקות שקילות של סדרות קושי של מספרים רציונליים. זה הולך להיות טיפה יותר טריקי.

הסיטואציה הזו צצה די הרבה במתמטיקה: יש לנו אובייקט מתמטי ש"חסר בו" משהו, אז אנחנו מרחיבים אותו בצורה שבאופן מובהק מטפלת במה שהיה חסר קודם - אלא שאחרי ההרחבה, האובייקט שלנו יותר גדול ומסובך, ויש סיכוי שעכשיו חסרים בו דברים <strong>חדשים</strong>, שלא היו במסגרת ההתייחסות שלנו קודם ולכן לא יכלו להיות חסרים. בניה חכמה היא בניה שמצליחה למנוע מהבעיה הזו להיווצר. <a href="https://gadial.net/2023/07/27/continuum_hypothesis_forcing_intro/">ראינו לא מזמן בבלוג</a> סוג מרשים במיוחד של בניה חכמה שכזו - <strong>כפייה</strong> בתורת הקבוצות האקסיומטית. יש עוד דוגמאות קלילות יותר, למשל <strong>המשפט היסודי של האלגברה</strong>: הרעיון שם הוא שגם במספרים ממשיים עדיין "חסרים דברים" - למשל, פתרון למשוואה הפולינומית {% equation %}x^{2}+1=0{% endequation %}. אז מרחיבים את הממשיים אל <strong>המספרים המרוכבים</strong> ואז קורה הקסם ש<strong>כל</strong> משוואה פולינומית היא פתירה; לא רק המשוואות שקודם לא היו פתירות, אלו שהמקדמים שלהן הם מספרים ממשיים, אלא גם כל המשוואות הפולינומיות החדשות שקיבלנו, עכשיו כשהמקדמים יכולים להיות גם מרוכבים.

פורמלית, מה שאנחנו צריכים לעשות הוא זה: לקחת סדרה {% equation %}A_{1},A_{2},A_{3},\ldots{% endequation %} כש-{% equation %}A_{n}\in\mathbb{F}{% endequation %} ולהוכיח שאם הסדרה הזו היא סדרת קושי, אז קיים {% equation %}B{% endequation %} כך ש-{% equation %}\lim_{n\to\infty}A_{n}=B{% endequation %}. איך נבנה את {% equation %}B{% endequation %}? אנחנו צריכים לבנות סדרה של רציונליים, {% equation %}\left\{ b_{n}\right\} _{n=1}^{\infty}{% endequation %} ואנחנו צריכים שהסדרה הזו תהיה סדרת קושי, ובנוסף שהיא "תתקרב" אל סדרת ה-{% equation %}A_{n}{% endequation %}-ים כרצוננו. זה מייד מזכיר תכונה שנקראת <strong>צפיפות</strong> הרציונליים: שעבור כל מספר ממשי, קיים מספר רציונלי שקרוב אליו כרצוננו. ראינו כבר תכונה <strong>אחרת</strong> שנקראה צפיפות - שבין כל שני ממשיים קיים רציונלי - אבל אני לא אכנס כאן לשאלה עד כמה התכונות הללו קשורות, אלא פשוט אוכיח פורמלית את תכונת הצפיפות שאני רוצה עכשיו.

אני רוצה להראות שאם {% equation %}A{% endequation %} הוא מספר ממשי, אז קיים רציונלי {% equation %}q{% endequation %} שקרוב אליו כרצוננו. פורמלית, אם {% equation %}\varepsilon>0{% endequation %} אז קיים {% equation %}Q\in\mathbb{Q}{% endequation %} כך ש-{% equation %}\left|Q-A\right|\le\varepsilon{% endequation %}. שימו לב שכל המעורבים פה הם מספרים ממשיים: גם {% equation %}A{% endequation %}, גם {% equation %}Q{% endequation %} (שהולך להיות מיוצג על ידי סדרה קבועה של מספר רציונלי ספציפי) וגם {% equation %}\varepsilon{% endequation %}. אבל שזה ש-{% equation %}\varepsilon{% endequation %} הוא ממשי ולא בהכרח רציונלי זה מעצבן, כי זה אומר שאני צריך לתאר אותו עם סדרה במקום פשוט עם קבוע, אז נתבסס על זה שכבר הוכחתי ארכימדיות: זה אומר שקיים {% equation %}N{% endequation %} טבעי כך ש-{% equation %}\frac{1}{\varepsilon}\le N{% endequation %}, כלומר {% equation %}\frac{1}{N}\le\varepsilon{% endequation %}, ואם נראה שמשהו קטן מ-{% equation %}\frac{1}{N}{% endequation %} (הרציונלי) אז הוא בוודאי קטן גם מ-{% equation %}\varepsilon{% endequation %}, אז אני יכול פשוט להניח מכאן והלאה ש-{% equation %}\varepsilon{% endequation %} רציונלי.

איפה כדאי לחפש את {% equation %}q{% endequation %}? ובכן, זה קל: מכיוון ש-{% equation %}A{% endequation %} הוא מספר ממשי, הוא בנוי <strong>מתוך</strong> הרציונליים, כלומר כדאי לחפש את {% equation %}q{% endequation %} בתוך נציג {% equation %}A=\left[a\right]{% endequation %} של {% equation %}A{% endequation %}. הנציג הזה הוא סדרת קושי של רציונליים, אז עבור {% equation %}\varepsilon>0{% endequation %} רציונלי קיים {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|a_{N}-a_{n}\right|<\varepsilon{% endequation %}. עכשיו אני אגדיר את {% equation %}Q{% endequation %} בתור המספר הממשי שמיוצג על ידי הסדרה הקבועה {% equation %}q_{n}=a_{N}{% endequation %}, ובואו נראה מה קיבלנו. אמרתי קודם שכדי להוכיח {% equation %}A\le B{% endequation %} עבור ממשיים, מספיק להראות שעבור נציגים שלהם מתקיים {% equation %}a_{n}\le b_{n}{% endequation %} החל ממקום מסוים. אצלנו הסיטואציה טיפה יותר מורכבת: אגף שמאל של {% equation %}\left|Q-A\right|\le\varepsilon{% endequation %} כולל את הביטוי {% equation %}\left|Q-A\right|{% endequation %} בזמן שאגף ימין הוא עדיין פשוט וכולל רק את {% equation %}\varepsilon{% endequation %}, שמיוצג על ידי הסדרה הקבועה {% equation %}\varepsilon_{n}=\varepsilon{% endequation %}. כשאני יורד לרמת הנציגים אני מקבל {% equation %}\left|q_{n}-a_{n}\right|<\varepsilon_{n}{% endequation %}, וזה הולך לתת לי את {% equation %}\left|Q-A\right|\le\varepsilon{% endequation %} אם אני רק אשתכנע שהסדרה {% equation %}\left|q_{n}-a_{n}\right|{% endequation %} היא נציג של המספר הממשי {% equation %}\left|Q-A\right|{% endequation %}.

את זה יחסית קל להראות: אם {% equation %}Q\ge A{% endequation %} אז {% equation %}\left|Q-A\right|=Q-A{% endequation %} וכמו כן בגלל ש-{% equation %}Q-A\ge0{% endequation %} אז החל ממקום מסוים, {% equation %}q_{n}-a_{n}\ge0{% endequation %}, כלומר {% equation %}\left|q_{n}-a_{n}\right|=q_{n}-a_{n}{% endequation %} וזו אכן סדרה שמייצגת את {% equation %}Q-A{% endequation %}. אם {% equation %}Q<A{% endequation %} אז {% equation %}\left|Q-A\right|=A-Q{% endequation %} ומכיוון ש-{% equation %}Q-A<0{% endequation %} החל ממקום מסוים {% equation %}q_{n}-a_{n}\le0{% endequation %}, כלומר {% equation %}\left|q_{n}-a_{n}\right|=a_{n}-q_{n}{% endequation %} וגם את הכיוון הזה סיימנו. זה מסיים את הוכחת תכונת הצפיפות.

עכשיו, אם נסתכל על מה שהוכחנו, בעצם ראינו משהו חזק יותר מאשר "סתם" צפיפות: ראינו שלכל מספר ממשי {% equation %}A{% endequation %} ונציג שלו {% equation %}a{% endequation %}, אברי הנציג קרובים אל {% equation %}A{% endequation %} כרצוננו. זה נשמע כמעט מובן מאליו, אז הנה המשמעות הפורמלית: לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}\left|a_{n}-A\right|\le\varepsilon{% endequation %}. גם בתכונה המחוזקת הזו תכף אשתמש.

חזרה אל הטענה המקורית שאני רוצה להוכיח: {% equation %}\left\{ A_{n}\right\} _{n=1}^{\infty}{% endequation %} היא סדרת קושי של ממשיים שאני מחפש לה גבול. אני אבנה מספר ממשי {% equation %}B=\left[b\right]{% endequation %} באופן הבא: לכל {% equation %}n{% endequation %}, מתכונת הצפיפות של הרציונליים קיים רציונלי {% equation %}b_{n}{% endequation %} כך ש-{% equation %}\left|b_{n}-A_{n}\right|\le\frac{1}{n}{% endequation %}. זהו, זו כל ההגדרה.

עכשיו קל להוכיח ש-{% equation %}\lim_{n\to\infty}A_{n}=B{% endequation %}. יהא {% equation %}\varepsilon>0{% endequation %} כלשהו, אז אני יודע שקיימים:

<ul> <li>{% equation %}N_{1}{% endequation %} כך שלכל {% equation %}n>N_{1}{% endequation %} מתקיים {% equation %}\left|b_{n}-B\right|\le\frac{\varepsilon}{2}{% endequation %} (זו תכונת הצפיפות ה"מחוזקת")</li>


<li>{% equation %}N_{2}{% endequation %} כך ש-{% equation %}\frac{1}{N_{2}}<\frac{\varepsilon}{2}{% endequation %}, ולכן לכל {% equation %}n>N_{2}{% endequation %} מתקיים {% equation %}\left|b_{n}-A_{n}\right|\le\frac{1}{n}\le\frac{1}{N_{2}}<\frac{\varepsilon}{2}{% endequation %} (כי כך בנינו את ה-{% equation %}b_{n}{% endequation %}-ים).</li>

</ul>

נגדיר {% equation %}N=\max\left\{ N_{1},N_{2}\right\} {% endequation %} וקיבלנו שלכל {% equation %}n>N{% endequation %} מתקיים:

{% equation %}\left|A_{n}-B\right|=\left|A_{n}-b_{n}+b_{n}-B\right|\le\left|A_{n}-b_{n}\right|+\left|b_{n}-B\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon{% endequation %}

האם סיימנו? ובכן, עוד לא! כי קפצתי באלגנטיות על שלב קריטי בדרך: הגדרתי את {% equation %}B{% endequation %} באמצעות הסדרה {% equation %}b_{1},b_{2},b_{3},\ldots{% endequation %} אבל בשום מקום לא הוכחתי שזו <strong>סדרת קושי</strong>. ודי ברור שטרם סיימתי את ההוכחה, כי בעצם לא השתמשתי בשום שלב בכך שסדרת הממשיים, {% equation %}A_{1},A_{2},A_{3},\ldots{% endequation %} היא סדרת קושי. אבל בואו נחשוב שניה בהגיון - אם היא לא הייתה סדרת קושי, אז סדרת ה-{% equation %}b_{n}{% endequation %}--ים הזו הייתה סדרה אקראית של מספרים שקרובים ל-{% equation %}A_{1},A_{2},A_{3}{% endequation %} וכן הלאה אבל אין שום סיבה שיהיו קרובים זה לזה, כי ה-{% equation %}A_{n}{% endequation %}-ים הללו לא קרובים זה לזה.

הנה מה שנעשה: בהינתן {% equation %}\varepsilon>0{% endequation %}, אני יודע שקיימים:

<ul> <li>{% equation %}N_{1}{% endequation %} כך שאם {% equation %}n,m>N_{1}{% endequation %} אז {% equation %}\left|A_{n}-A_{m}\right|<\frac{\varepsilon}{3}{% endequation %} (כי ה-{% equation %}A_{n}{% endequation %}-ים הם סדרת קושי).</li>


<li>{% equation %}N_{2}{% endequation %} כך ש-{% equation %}\frac{1}{N_{2}}<\frac{\varepsilon}{3}{% endequation %} ולכן עבור {% equation %}n,m>N_{2}{% endequation %} מתקיים {% equation %}\left|b_{n}-A_{n}\right|<\frac{\varepsilon}{3}{% endequation %} וגם {% equation %}\left|b_{m}-A_{m}\right|<\frac{\varepsilon}{3}{% endequation %} (כי כך בנינו את ה-{% equation %}b_{n}{% endequation %}-ים).</li>

</ul>

ניקח {% equation %}N=\max\left\{ N_{1},N_{2}\right\} {% endequation %} ואז לכל {% equation %}n,m>N{% endequation %}:

{% equation %}\left|b_{n}-b_{m}\right|=\left|b_{n}-A_{n}+A_{n}-A_{m}+A_{m}-b_{m}\right|\le{% endequation %}

{% equation %}\le\left|b_{n}-A_{n}\right|+\left|A_{n}-A_{m}\right|+\left|A_{m}-b_{m}\right|<{% endequation %}

{% equation %}\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon{% endequation %}

וזה.. מסיים את הכל... אני חושב? אין לי אף מקור שמציג את הדברים ברמות הפירוט שאליה נכנסתי כאן (כדי לשכנע את עצמי אחת ולתמיד שהכל עובד) אז בטח יש לי שלל טעויות - אבל היי, נראה לי שבגדול ככה זה הולך! עוד פינה שסגרתי לעצמי אחרי עשרים שנים בערך! 
