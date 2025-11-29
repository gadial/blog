---
title: "אז מה זה בעצם המספרים הממשיים? (חלק ה': בונים את המספרים הממשיים עם
חתכי דדקינד)"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - מספרים ממשיים
---


<h2>מבוא</h2>

בפוסט הקודם שלי הצגתי את הבניה של קנטור למספרים הממשיים והוכחתי שהיא מקיימת את האקסיומות של שדה סדור שלם. זה היה בסך הכל בסדר, עם כמה קשיים טכניים לא נוראיים. הפעם אני אעשה את זה עם הבניה של דדקינד, וגם זה יהיה בסך הכל בסדר, עם כמה קשיים טכניים לא נוראיים אבל במקומות שונים לגמרי. למשל, בשיטה של קנטור הסתבכתי עם הוכחת אקסיומת השלמות ולעומת זאת כאן זה יהיה כמעט טריוויאלי, ואילו בחתכי דדקינד הגדרת החיבור תהיה פשוטה אבל הגדרת הכפל תהיה גיהנום, להבדיל ממה שקרה אצל קנטור שבו שתי ההגדרות היו די דומות באופי שלהן. זה לא שיש דרך שהיא "טובה יותר", זו של דדקינד או של קנטור - שתיהן אחלה ושווה להכיר את שתיהן.

אני אחזור על מה שהצגתי בפוסט הקודם בתורה המטרה שלנו, ממש ברמת ההעתק-הדבק:

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

<ul> <li>אם {% equation %}S\subseteq\mathbb{F}{% endequation %} היא קבוצה לא ריקה וחסומה מלעיל, אז {% equation %}\sup S{% endequation %} קיים.</li>

</ul>

אני לא מסביר לעומק מה כל האקסיומות אומרות כי כבר דיברנו על זה בפירוט בפוסטים הקודמים ועוד נעשה את זה בפירוט בהמשך, כחלק מההוכחות עצמן. בואו נעבור לבניה של דדקינד.

<h2>הבניה של דדקינד</h2>

בואו נעשה עוד העתק-הדבק מהפוסט הקודם ואז נחתוך לכיוון דדקינד במקום לכיוון קנטור: 

קנטור ודדקינד לוקחים שניהם בתור נקודת מוצא את הרציונליים, {% equation %}\mathbb{Q}{% endequation %}, ויש לכך סיבות טובות. ראשית, זה שדה סדור, כלומר אנחנו "כמעט שם" ורק נותרה לנו עוד אקסיומה אחת; אפשר להראות ש-{% equation %}\mathbb{Q}{% endequation %} יהיה מוכל בכל שדה סדור כך שהוא בסיס טוב לצאת ממנו; ועם הבניה של {% equation %}\mathbb{Q}{% endequation %} אין לנו שום בעיות והיא די פשוטה.

מה שדדקינד וקנטור עושים, וזה רעיון מקסים שחוזר על עצמו שוב ושוב במתמטיקה, הוא לבנות את האובייקט החדש <strong>בתור</strong> האובייקטים הקיים שכרגע חסר בו משהו. דדקינד אומר - יש לנו קבוצות של רציונליים שנראה שאמור להיות להן חסם עליון אבל אין? יופי, הקבוצות הללו <strong>יהיו</strong> המספר הממשי שהוא החסם העליון הזה. קנטור אומר - יש לנו סדרות קושי שנראה שאמורות להתכנס לאנשהו אבל אין להן גבול? יופי, הסדרות הללו <strong>יהיו</strong> המספר הממשי שהוא הגבול הזה. זה נראה כמו רמאות גמורה, אבל כשפורטים את זה לפרטים ברור שאין כאן שום רמאות והכל תקין מבחינה פורמלית. גם מבחינה רעיונית אפשר להבין את זה: האובייקט שממנו מתחילים, זה שמצביע על החסר, בעצם כולל את <strong>האינפורמציה</strong> שנראית לנו רלוונטית עבור המספר החדש; לכן הוא האובייקט הכי מתאים כדי להגדיר את המספר החדש הזה.

בואו נראה את הדוגמא הקלאסית עם המספר האי-רציונלי {% equation %}\sqrt{2}=1.41421\ldots{% endequation %}. זה מספר אי רציונלי, אבל יש סדרת מספרים רציונליים פשוטה ששואפת אליו: {% equation %}1,1.4,1.41,1.414,1.4142,1.41421,\ldots{% endequation %}. קנטור סוג של הגדיר את {% equation %}\sqrt{2}{% endequation %} בעזרת הסדרה הזו, ואת זה ראינו בפוסט הקודם ולא אכנס לכך שוב.

אצל דדקינד אין סדרה אלא קבוצה, הקבוצה {% equation %}A=\left\{ q\in\mathbb{Q}\ |\ q<\sqrt{2}\right\} {% endequation %}, אבל התיאור של הקבוצה הזו נראה קצת כמו רמאות כי הוא מניח שאנחנו יודעים מה זה {% equation %}\sqrt{2}{% endequation %}. דרך אחת לעקוף את הרמאות הזו היא להסתכל על הקבוצה {% equation %}\left\{ q\in\mathbb{Q}\ |\ q^{2}<2\right\} {% endequation %} אבל גם זו דרך בעייתית כי מה עם מספר כמו {% equation %}\pi{% endequation %} שאי אפשר לתאר בצורה פשוטה דומה את כל המספרים שקטנים ממנו? אבל יש גם דרך אחרת. בהינתן מספר רציונלי {% equation %}x\in\mathbb{Q}{% endequation %} כלשהו אני יכול לכתוב קבוצה {% equation %}A_{x}=\left\{ q\in\mathbb{Q}\ |\ q<x\right\} {% endequation %} של כל המספרים שקטנים ממנו (<strong>ולא שווים אליו</strong>). עכשיו את {% equation %}A{% endequation %} המקורית שלי אפשר לתאר בעזרת סדרת המספרים שראינו קודם: {% equation %}A=A_{1}\cup A_{1.4}\cup A_{1.41}\cup\ldots{% endequation %}.

זה מוביל אותנו לרעיון הכללי מאחורי חתכי דדקינד: קבוצות שנראות באופן כללי כמו משהו מהצורה {% equation %}A_{x}=\left\{ q\in\mathbb{Q}\ |\ q<x\right\} {% endequation %}, אפילו אם {% equation %}x{% endequation %} הוא לא רציונלי. כדי לעשות כזה דבר, מגדירים פורמלית <strong>חתך דדקינד</strong> בתור קבוצה {% equation %}A\subseteq\mathbb{Q}{% endequation %} שמקיימת:

<ol> <li>{% equation %}A\ne\emptyset{% endequation %} ו-{% equation %}A\ne\mathbb{Q}{% endequation %}</li>


<li>אם {% equation %}b<a{% endequation %} וגם {% equation %}a\in A{% endequation %} אז {% equation %}b\in A{% endequation %}</li>


<li>אם {% equation %}a\in A{% endequation %} אז קיים {% equation %}b\in A{% endequation %} כך ש-{% equation %}a<b{% endequation %}</li>

</ol>

תכונה 2 אומרת שהחתך "סגור כלפי מטה": אם מספר כלשהו שייך אליו, אז <strong>כל</strong> המספרים הרציונליים הקטנים ממנו גם כן שייכים אליו. תכונה 3 אומרת שאין בחתך איבר מקסימלי - מה שמתבטא בסימן אי השוויון בתיאור הלא פורמלי {% equation %}A_{x}=\left\{ q\in\mathbb{Q}\ |\ q<x\right\} {% endequation %} שנתתי קודם.

למה בעצם קוראים לדבר כזה "חתך"? כי אפשר לחשוב עליו כאילו לקחנו את כל ציר המספרים הרציונליים {% equation %}\mathbb{Q}{% endequation %} ו"חתכנו" אותו עם סכין בנקודה מסוימת, מה שפירק את {% equation %}\mathbb{Q}{% endequation %} לשתי קבוצות לא ריקות, {% equation %}A,Z{% endequation %} (זו תכונה 1; {% equation %}B{% endequation %} לא ריקה כי {% equation %}A\ne\mathbb{Q}{% endequation %}) כך ש-{% equation %}A{% endequation %} הוא כל מה שמשמאל לנקודת החיתוך (זו תכונה 2) ו-{% equation %}Z{% endequation %} הוא כל מה שמימין (זה נובע מכך ש-{% equation %}Z{% endequation %} היא המשלים של {% equation %}A{% endequation %}), והרעיון הוא שאם החיתוך היה <strong>בדיוק</strong> בנקודה רציונלית כלשהי, היא נכנסת אל {% equation %}Z{% endequation %} ולא אל {% equation %}A{% endequation %} (זו תכונה 3). בפועל אין לנו צורך לדבר על {% equation %}Z{% endequation %} במפורש ולכן אני לא אעשה את זה בכלל.

אם כן, דדקינד מגדיר קבוצה {% equation %}\mathbb{F}{% endequation %} שכוללת את כל חתכי הדדקינד. עדיין אי אפשר לראות שהיא מקיימת אקסיומות כלשהן כי לא הגדרנו עליה פעולות חיבור וכפל או קבוצת חיוביים {% equation %}P{% endequation %}, אבל כן אפשר לשים לב לכך ש-{% equation %}\mathbb{Q}\subseteq\mathbb{F}{% endequation %} במובן האיזומורפיזמי של המילה, כלומר לכל מספר רציונלי {% equation %}x\in\mathbb{Q}{% endequation %} אפשר להתאים את הקבוצה {% equation %}A_{x}=\left\{ q\in\mathbb{Q}\ |\ q<x\right\} {% endequation %} שהראיתי קודם, והקבוצה הזו היא חתך: 1 מתקיים כי {% equation %}x-1\in A_{x}{% endequation %} ואילו 2 מתקיים כי {% equation %}x\notin A_{x}{% endequation %}. עבור 3 אנחנו משתמשים בטרנזיטיביות יחס הסדר על הרציונליים: אם {% equation %}b<a{% endequation %} וגם {% equation %}a\in A_{x}{% endequation %} אז על פי הגדרה {% equation %}a<x{% endequation %} ואז מטרנזיטיביות יחס הסדר נקבל {% equation %}b<x{% endequation %}, כלומר {% equation %}b\in A_{x}{% endequation %}. עבור {% equation %}4{% endequation %}, בהינתן {% equation %}a\in A_{x}{% endequation %}, כלומר {% equation %}a<x{% endequation %}, אז נסמן {% equation %}\varepsilon=x-a{% endequation %} ונגדיר {% equation %}b=a+\frac{\varepsilon}{2}{% endequation %} אז {% equation %}a<b<x{% endequation %} ולכן מצאנו {% equation %}b\in A_{x}{% endequation %} שמקיים את מה שרצינו.

בואו נתחיל להוכיח שהבניה של דדקינד מקיימת את תכונות השדה הסדור השלם. בניגוד לפוסט הקודם, כאן אני לא אלך על פי הסדר, כי אני זקוק לתכונות מאוחרות יותר ברשימה כדי להוכיח תכונות מוקדמות יותר. 

<h2>חיבור של חתכי דדקינד</h2>

עבור השיטה של קנטור עם סדרות קושי, הגדרתי חיבור וכפל ביחד וכמעט באותה צורה. זה לא עובד ככה עבור חתכי דדקינד - כפל הוא פעולה הרבה יותר מורכבת מחיבור, ולכן אני מתחיל מלדבר על חיבור לבד וכפל יצטרף בהמשך. באופן די משמח ההגדרה ה"טבעית" של חיבור עובדת:

<ul> <li>{% equation %}A+B\triangleq\left\{ a+b\ |\ a\in A,b\in B\right\} {% endequation %}</li>

</ul>

כלומר, כדי לבנות את החתך שהוא הסכום של {% equation %}A{% endequation %} ו-{% equation %}B{% endequation %} אנחנו בונים קבוצה חדשה שהאיברים שלה הם הסכומים של איבר מ-{% equation %}A{% endequation %} ואיבר מ-{% equation %}B{% endequation %}; זו הגדרה די נפוצה (למשל, כך גם מגדירים סכומים של מרחבים וקטוריים) אבל עדיין צריך להראות שהיא עובדת - כלומר, ש-{% equation %}A+B{% endequation %} הוא באמת חתך בעצמו, ושפעולת החיבור היא אסוציאצטיבית וקומוטטיבית.

עיקר העבודה הוא להראות ש-{% equation %}A+B{% endequation %} הוא חתך. ראשית, בגלל ש-{% equation %}A,B{% endequation %} הם חתכים אז הם לא ריקים, כלומר קיימים {% equation %}a\in A{% endequation %} ו-{% equation %}b\in B{% endequation %} ולכן {% equation %}a+b\in A+B{% endequation %} כך ש-{% equation %}A+B\ne\emptyset{% endequation %}. כדי להוכיח ש-{% equation %}A+B\ne\mathbb{Q}{% endequation %} צריך להבין שהתכונה הזו אומרת יותר מ"יש איזה איבר בודד שחסר" אלא שחתכים הם <strong>חסומים</strong>. כלומר, לכל חתך {% equation %}A{% endequation %}, קיים מספר רציונלי {% equation %}q{% endequation %} כך שאם {% equation %}a\in A{% endequation %} אז {% equation %}a<q{% endequation %} (ולכן גם כל מי שגדול מ-{% equation %}q{% endequation %} לא ב-{% equation %}A{% endequation %}). זה לא נובע מ-{% equation %}A\ne\mathbb{Q}{% endequation %} לבד, אלא מהשילוב של זה עם תכונה 2: כי אם {% equation %}A{% endequation %} לא חסום, אז בואו ניקח {% equation %}q\in\mathbb{Q}{% endequation %} <strong>כלשהו</strong>. מכיוון ש-{% equation %}A{% endequation %} לא חסום, גם {% equation %}q{% endequation %} הוא לא חסם שלו, ולכן יש {% equation %}a\in A{% endequation %} כך ש-{% equation %}q<a{% endequation %} ותכונה 2 אומרת ש-{% equation %}q\in A{% endequation %}. זה מוכיח ש-{% equation %}A=\mathbb{Q}{% endequation %}.

עכשיו, עבור חתכים {% equation %}A,B{% endequation %} כלשהם ראינו שיש {% equation %}q_{A},q_{B}{% endequation %} שהם חסמים מלעיל שלהם - אז הקבוצה {% equation %}A+B{% endequation %} חסומה על ידי {% equation %}q_{A}+q_{B}{% endequation %} ובפרט {% equation %}q_{A}+q_{B}{% endequation %} לא שייך אל {% equation %}A+B{% endequation %} כך ש-{% equation %}A+B\ne\mathbb{Q}{% endequation %}. זה מסיים עם תכונה 1.

נעבור לתכונה 2. ניקח איבר {% equation %}a+b{% endequation %} כלשהו של {% equation %}A+B{% endequation %}, ורציונלי {% equation %}c{% endequation %} כלשהו כך ש-{% equation %}c<a+b{% endequation %}. אנחנו רוצים להראות שגם {% equation %}c\in A+B{% endequation %}. אם נחסר את {% equation %}b{% endequation %} משני האגפים, נקבל {% equation %}c-b<a{% endequation %}, ומתכונה 2 נובע ש-{% equation %}c-b\in A{% endequation %} כלומר קיים {% equation %}a^{\prime}{% endequation %} כך ש-{% equation %}c-b=a^{\prime}{% endequation %} ולכן {% equation %}c=a^{\prime}+b\in A+B{% endequation %}. זה מסיים עם תכונה 2.

תכונה 3 היא די ישירה. אם {% equation %}c=a+b{% endequation %}, אז מתכונה 3 עבור {% equation %}A,B{% endequation %} אני יודע שיש {% equation %}a<a^{\prime}\in A{% endequation %} ו-{% equation %}b<b^{\prime}\in B{% endequation %} ולכן {% equation %}c=a+b<a^{\prime}+b^{\prime}\in A+B{% endequation %} (והאמת הייתי מסתדר גם בלי {% equation %}b^{\prime}{% endequation %} אבל אני אוהב סימטריה).

נעבור עכשיו לקומוטטיביות ואסוציאטיביות:

<ul> <li>{% equation %}A+B=B+A{% endequation %}</li>


<li>{% equation %}\left(A+B\right)+C=A+\left(B+C\right){% endequation %}</li>

</ul>

בשני המקרים זה נובע מייד מהתכונות התואמות של מספרים רציונליים. עבור קומוטטיביות זה מובן מאליו:

{% equation %}A+B=\left\{ a+b\ |\ a\in A,b\in B\right\} =\left\{ b+a\ |\ a\in A,b\in B\right\} =B+A{% endequation %}

עבור אסוציאטיביות זה טיפונת יותר טריקי אז אני אעשה את זה בזהירות: נניח ש-{% equation %}x\in\left(A+B\right)+C{% endequation %}. אז זה אומר שקיימים רציונליים {% equation %}c,d{% endequation %} כך ש-{% equation %}c\in C{% endequation %} ו-{% equation %}d\in A+B{% endequation %} ו-{% equation %}x=d+c{% endequation %}. עכשיו, מכיוון ש-{% equation %}d\in A+B{% endequation %} זה אומר שיש רציונליים {% equation %}a\in A,b\in B{% endequation %} כך ש-{% equation %}d=a+b{% endequation %}, כלומר {% equation %}x=\left(a+b\right)+c{% endequation %}. עכשיו נשתמש באסוציאטיביות של החיבור של רציונליים ונקבל {% equation %}x=a+\left(b+c\right){% endequation %}. מכיוון ש-{% equation %}a\in A{% endequation %} וגם {% equation %}b+c\in B+C{% endequation %} קיבלנו {% equation %}x\in A+\left(B+C\right){% endequation %}. זה כיוון אחד, והכיוון השני דומה, אז סיימנו גם עם אסוציאטיביות.

עכשיו צריך להתמודד עם השאלה הפילוסופית הקשה: מה הוא אפס?

<ul> <li>קיים איבר שמסומן ב-0 כך ש-{% equation %}A+0=A{% endequation %} לכל {% equation %}A{% endequation %}</li>

</ul>

איזה חתך יתאים לתכונה הזו? ובכן, לא ממש צריך לשבור את הראש; עבור מספרים רציונליים אנחנו כבר <strong>יודעים</strong> מה החתך שאמור להתאים להם, הראיתי את זה קודם. עבור 0 זה החתך {% equation %}A_{0}=\left\{ q\in\mathbb{Q}\ |\ q<0\right\} {% endequation %}, כלומר כל המספרים השליליים. רק צריך להראות שבאמת מתקיים {% equation %}A+A_{0}=A{% endequation %} לכל {% equation %}A{% endequation %}.

בואו ניקח {% equation %}a\in A{% endequation %} כלשהו. אז לרוע המזל אני <strong>לא יכול</strong> לומר משהו כמו "{% equation %}a+0\in A+A_{0}{% endequation %} כי {% equation %}0\notin A_{0}{% endequation %}. אבל כאן תכונה 3 של חתכים נחלצת לעזרתי: אני יודע שקיים {% equation %}b\in A{% endequation %} כך ש-{% equation %}a<b{% endequation %}, ולכן {% equation %}a-b<0{% endequation %} ולכן {% equation %}a-b\in A_{0}{% endequation %} ולכן קיים {% equation %}c\in A_{0}{% endequation %} כך ש-{% equation %}a-b=c{% endequation %} ולכן {% equation %}a=b+c\in A+A_{0}{% endequation %}. כל זה הראה לי ש-{% equation %}A\subseteq A+A_{0}{% endequation %}.

בכיוון השני, אם {% equation %}x\in A+A_{0}{% endequation %} אז קיימים {% equation %}a\in A,b\in A_{0}{% endequation %} כך ש-{% equation %}x=a+b{% endequation %}. בגלל ש-{% equation %}b\in A_{0}{% endequation %} אז {% equation %}b<0{% endequation %} ולכן {% equation %}x=a+b<a+0=a{% endequation %}, ומתכונה 2 של חתכים נקבל ש-{% equation %}x\in A{% endequation %}, מה שמוכיח ש-{% equation %}A+A_{0}\subseteq A{% endequation %} ומסיים את ההוכחה ש-{% equation %}A+A_{0}=A{% endequation %}.

נשאר רק לטפל באיברים נגדיים:

<ul> <li>לכל {% equation %}A{% endequation %} קיים איבר שמסומן ב-{% equation %}-A{% endequation %} ונקרא <strong>הנגדי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A+\left(-A\right)=0{% endequation %}</li>

</ul>

וכאן לצערי הכיף נגמר - ההגדרה הזו תהיה קצת מעצבנת. איך היינו <strong>רוצים</strong> שההגדרה תלך? מה ההגדרה ה"טבעית"? ובכן, זה קל: {% equation %}-A=\left\{ -a\ |\ a\in A\right\} {% endequation %}. אלא שההגדרה הזו היא <strong>קטסטרופה</strong>. למשל, אם {% equation %}A=\left\{ q\in\mathbb{Q}\ |\ q<2\right\} {% endequation %} אז הקבוצה שקראתי לה {% equation %}-A{% endequation %} תהיה {% equation %}\left\{ q\in\mathbb{Q}\ |\ q>-2\right\} {% endequation %}. אינטואיטיבית החלפתי את הקרן האינסופית-לשמאל {% equation %}\left(-\infty,2\right){% endequation %} בקרן האינסופית-לימין {% equation %}\left(-2,\infty\right){% endequation %}. זה בוודאי לא מה שאני רוצה. מצד שני, הקטע הזה של היפוך קרן מאינסופית-לשמאל אל אינסופית-לימין דווקא יכול לסייע לי: אם אני אסתכל על {% equation %}A{% endequation %} ואקח את {% equation %}\mathbb{Q}\backslash A{% endequation %} אני אקבל את הקרן {% equation %}[2,\infty({% endequation %}, כך שאם אני הופך <strong>אותה</strong> בצורה הזו אני מקבל את {% equation %})-\infty,-2]{% endequation %}. זה <strong>כמעט</strong> מה שאני רוצה, ואם הייתי הולך על זה בצורה הזו, ההגדרה הייתה די פשוטה: {% equation %}-A=\left\{ q\ |\ -q\notin A\right\} {% endequation %}.

אבל זה רק <strong>כמעט</strong> עובד בגלל ש-{% equation %})-\infty,-2]{% endequation %} יש לנו את נקודת הקצה הימנית 2 (זו המשמעות של שימוש בסוגריים מרובעים ולא עגולים) ואנחנו לא רוצים שתהיה נקודת קצה - זה סותר את תכונה 3. לכן צריך ללכלך קצת את ההגדרה היפה של {% equation %}-A{% endequation %} שלי: לא מספיק ש-{% equation %}-q{% endequation %} לא יהיה ב-{% equation %}A{% endequation %}; צריך שהוא לא יהיה <strong>המינימלי</strong> שאינו ב-{% equation %}A{% endequation %}. כלומר, צריך שמישהו קטן יותר מ-{% equation %}-q{% endequation %} גם כן לא יהיה ב-{% equation %}A{% endequation %}, ואת זה אפשר לנסח בתור "קיים {% equation %}r>0{% endequation %} כך ש-{% equation %}-q-r\notin A{% endequation %}". זה נותן לנו את ההגדרה הפורמלית שלנו:

<ul> <li>{% equation %}-A\triangleq\left\{ q\in\mathbb{Q}\ |\ \exists r>0:-q-r\notin A\right\} {% endequation %}</li>

</ul>

וזו... לא הגדרה יפה במיוחד, אין מה לעשות. אבל יש לה יתרון נחמד אחד: היא <strong>עובדת</strong>. בואו נוכיח שהיא עובדת.

ראשית, צריך להראות שגם {% equation %}-A{% endequation %} הוא חתך. כדי להראות ש-{% equation %}-A\ne\emptyset{% endequation %} צריך למצוא {% equation %}q{% endequation %} ו-{% equation %}r{% endequation %} כך ש-{% equation %}-q-r\notin A{% endequation %}. עכשיו, בגלל ש-{% equation %}A{% endequation %} חתך אנחנו יודעים ש-{% equation %}A\ne\mathbb{Q}{% endequation %} אז יש {% equation %}p\notin A{% endequation %} וכזכור, גם כל מי שגדול מ-{% equation %}p{% endequation %} לא שייך ל-{% equation %}A{% endequation %} בגלל תכונה 2. אז נגדיר {% equation %}r=1{% endequation %} ו-{% equation %}q=-p-1{% endequation %} ונקבל ש-{% equation %}-q-r=-q-1=p+1-1=p{% endequation %} ולכן {% equation %}q\in-A{% endequation %}.

כדי להראות ש-{% equation %}-A\ne\mathbb{Q}{% endequation %} נשתמש בזה ש-{% equation %}A\ne\emptyset{% endequation %} ולכן יש {% equation %}a\in A{% endequation %} ופשוט נגדיר {% equation %}q=-a{% endequation %}. אנחנו יודעים שלכל {% equation %}r>0{% endequation %}, {% equation %}-q-r<a{% endequation %} ולכן מתכונה 2, {% equation %}-q-r\in A{% endequation %}, כך שלא ייתכן ש-{% equation %}q\in-A{% endequation %}. זה מסיים עם הוכחת תכונה 1 של חתכים עבור {% equation %}-A{% endequation %}.

עבור תכונה 2, נניח ש-{% equation %}q\in-A{% endequation %} ו-{% equation %}b<q{% endequation %}. עכשיו, אנחנו יודעים שקיים {% equation %}r>0{% endequation %} כך ש-{% equation %}-q-r\notin A{% endequation %} אז בואו נגדיל את {% equation %}r{% endequation %} הזה קצת כדי שיעבוד גם עבור {% equation %}-b{% endequation %}: נגדיר {% equation %}r^{\prime}=r+\left(q-b\right){% endequation %}, אז גם {% equation %}r^{\prime}>0{% endequation %} כי {% equation %}b<q{% endequation %}, וכעת

{% equation %}-b-r^{\prime}=-b-\left(r+\left(q-b\right)\right)=-q-r\notin A{% endequation %}

אז קיבלנו שגם {% equation %}b\in-A{% endequation %}, כפי שצריך.

נשארה רק תכונה 3. נניח ש-{% equation %}q\in-A{% endequation %} ונמצא {% equation %}b\in-A{% endequation %} כך ש-{% equation %}q<b{% endequation %}. זה הולך להיות די קל: בגלל ש-{% equation %}q\in-A{% endequation %} קיים {% equation %}r>0{% endequation %} כך ש-{% equation %}-q-r\notin A{% endequation %}. לפני רגע <strong>הגדלנו</strong> את {% equation %}r{% endequation %}, עכשיו בואו <strong>נקטין</strong> אותו: נגדיר {% equation %}r^{\prime}=\frac{r}{2}{% endequation %} ({% equation %}r^{\prime}{% endequation %} הוא רציונלי כי הוא חלוקה של המספר הרציונלי {% equation %}r{% endequation %} ב-2). עכשיו נסתכל על {% equation %}q^{\prime}=q+r^{\prime}{% endequation %}: מתקיים {% equation %}q<q^{\prime}{% endequation %}, וכמו כן {% equation %}-q^{\prime}-\frac{r}{2}=-q-r\notin A{% endequation %} ולכן {% equation %}q^{\prime}\in-A{% endequation %}, וסיימנו את ההוכחה ש-{% equation %}-A{% endequation %} הוא חתך.

מה שעדיין נותר לנו להראות הוא שמתקיים {% equation %}A+\left(-A\right)=0{% endequation %}. כלומר, שאם ניקח {% equation %}x\in A{% endequation %} ו-{% equation %}y\in-A{% endequation %} ונסתכל על הסכום שלהם {% equation %}x+y{% endequation %} הוא בהכרח יהיה מספר שלילי, {% equation %}x+y<0{% endequation %}. כלומר, אני צריך להראות ש-{% equation %}x<-y{% endequation %}. עכשיו, על {% equation %}-y{% endequation %} אני יודע דברים כי {% equation %}y\in-A{% endequation %}: ספציפית, אני יודע שקיים {% equation %}r>0{% endequation %} כך ש-{% equation %}-y-r\notin A{% endequation %} וכאן כדאי לחשוב על {% equation %}\notin A{% endequation %} בתור "גדול מכל אברי {% equation %}A{% endequation %}" (כי כזכור, זה מה שתכונה 2 אומרת). כלומר, {% equation %}x<-y-r<-y{% endequation %} (אי השוויון הימני נובע מכך ש-{% equation %}r>0{% endequation %}), וזה מה שרציתי.

יפה מאוד, התקדמנו! סיימנו עם כל האקסיומות שנוגעות לפעולת החיבור לבדה (עדיין יש לנו דיסטריביוטיביות שמערבת חיבור וכפל). לאן עכשיו? עכשיו אנחנו יכולים לדבר על <strong>סדר</strong>.

<h2>אקסיומות השדה הסדור ואקסיומת השלמות</h2>

כשעובדים עם חתכי דדקינד, קל להגדיר את יחס הסדר {% equation %}A<B{% endequation %} בצורה מפורשת: {% equation %}A<B{% endequation %} אם ורק אם {% equation %}A\subset B{% endequation %}, כקבוצות. אבל אני לא אנקוט בגישה הזו אלא אשאר נאמן לתיאור אקסיומות השדה דרך הקבוצה {% equation %}P{% endequation %} - קבוצת האיברים החיוביים. אני צריך להגדיר אותה, ואז להוכיח שתי אקסיומות:

<ul> <li>לכל {% equation %}A\in\mathbb{F}{% endequation %} בדיוק אחד מהבאים מתקיים: או ש-{% equation %}A\in P{% endequation %}, או ש-{% equation %}-A\in P{% endequation %}, או ש-{% equation %}A=0{% endequation %}.</li>


<li>אם {% equation %}A,B\in P{% endequation %} אז {% equation %}A+B\in P{% endequation %}</li>

</ul>

אלו האקסיומות שאפשר לנסח עם חיבור בלבד; בשביל האחרונה אנחנו צריכים גם כפל, אז נשמור אותה עד אחרי הגדרת הכפל.

מה {% equation %}P{% endequation %} צריך להיות? אינטואיטיבית, זה כל ה-{% equation %}A{% endequation %}-ים שמקיימים {% equation %}0<A{% endequation %}, כלומר כל ה-{% equation %}A{% endequation %}-ים ש"נקודת הקצה הימנית" שלהם גדולה מ-0. עכשיו, כזכור {% equation %}0{% endequation %} מיוצג אצלנו על ידי החתך {% equation %}A_{0}=\left\{ q\in\mathbb{Q}\ |\ q<0\right\} {% endequation %} אז כל מי שגדול ממנו הולך להכיל את 0; למה לא להגדיר את {% equation %}P{% endequation %} ככה?

<ul> <li>{% equation %}P=\left\{ A\in\mathbb{F}\ |\ 0\in A\right\} {% endequation %}</li>

</ul>

כאשר בהגדרה של {% equation %}P{% endequation %} 0 הוא כמובן המספר הרציונלי 0 ולא החתך {% equation %}A_{0}{% endequation %}.

עכשיו בואו נוכיח את הטריכוטומיה: ניקח {% equation %}A{% endequation %}. נניח ש-{% equation %}A\ne0{% endequation %}, אז יש שתי אפשרויות:

<ul> <li>או שיש {% equation %}a\in A{% endequation %} שמקיים {% equation %}0<a{% endequation %}, ולכן מתכונה 2 של חתכים {% equation %}0\in A{% endequation %} ולכן {% equation %}A\in P{% endequation %}</li>


<li>או שלכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}a<0{% endequation %}. במקרה הזה, בגלל ש-{% equation %}A\ne0{% endequation %} ו<strong>כל</strong> האיברים של 0 הם שליליים, אז קיים {% equation %}q<0{% endequation %} כך ש-{% equation %}q\notin A{% endequation %}. איך זה עוזר לי? אני רוצה להוכיח ש-{% equation %}-A\in P{% endequation %}, כלומר ש-{% equation %}0\in-A{% endequation %}, כלומר שקיים {% equation %}r>0{% endequation %} כך ש-{% equation %}-0-r\notin A{% endequation %}, אז אני פשוט אגדיר {% equation %}r=-q{% endequation %} וסיימתי.</li>

</ul>

זה היה פשוט; מה בדבר חיבור של חיוביים שאמור לצאת גם כן חיובי? זה אפילו עוד יותר קל: אם {% equation %}A,B\in P{% endequation %} אז {% equation %}0\in A,0\in B{% endequation %} ולכן {% equation %}0=0+0\in A+B{% endequation %}.

אם כן, מה עוד נשאר לנו? ראשית, בואו ניזכר במה שאמרתי קודם: הייתי יכול להגדיר את {% equation %}A<B{% endequation %} על ידי {% equation %}A\subset B{% endequation %}. האמנם? ראשית, שימו לב שלכל שני חתכים {% equation %}A,B{% endequation %} או שמתקיים {% equation %}A\subseteq B{% endequation %} או שמתקיים {% equation %}B\subseteq A{% endequation %}. למה? ובכן, אם {% equation %}A\ne B{% endequation %} אז בלי הגבלת הכלליות, יש {% equation %}b\in B{% endequation %} כך ש-{% equation %}b\notin A{% endequation %}. עכשיו, אם היה {% equation %}a\in A{% endequation %} כך ש-{% equation %}b<a{% endequation %} אז מתכונה 2 היינו מקבלים ש-{% equation %}b\in A{% endequation %}; מכאן שלכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}a<b{% endequation %} אבל אז מתכונה 2 נובע ש-{% equation %}a\in B{% endequation %} לכל {% equation %}a\in A{% endequation %}, כלומר {% equation %}A\subseteq B{% endequation %}. אז אנחנו יודעים שתמיד יש יחס של הכלה בין הקבוצות, אבל למה הוא תואם את יחס הסדר? אם {% equation %}A\subset B{% endequation %} אז ניקח {% equation %}b\in B{% endequation %} כך ש-{% equation %}b\notin A{% endequation %}. מתכונה 3 של חתכים, קיים {% equation %}c\in B{% endequation %} כך ש-{% equation %}b<c{% endequation %}. נסמן {% equation %}r=c-b{% endequation %} וקיבלנו ש-{% equation %}c-r=b\notin A{% endequation %}, כלומר {% equation %}-c\in-A{% endequation %}, כך ש-{% equation %}0=c-c\in B-A{% endequation %} ולכן {% equation %}B-A\in P{% endequation %}, כלומר {% equation %}A<B{% endequation %}. הכיוון ההפוך ({% equation %}A<B{% endequation %} גורר {% equation %}A\subset B{% endequation %}) דומה.

יופי. איך זה עוזר לנו? ובכן, בניגוד למה שהלך בבניה של קנטור, כאן אנחנו הולכים להוכיח את אקסיומת השלמות די בקלות בזכות התכונה הזו. כדאי להזכיר גם כאן, כמו שעשיתי אצל קנטור, למה התכונה הזו לא נובעת מאליה - הרי מראש <strong>בניתי</strong> את החתכים בתור קבוצות של של איברים שמגיעים "עד" החסם העליון שלהם; אבל העניין הוא שבניתי קבוצות של <strong>מספרים רציונליים</strong> ואילו אקסיומת השלמות עכשיו אומרת משהו לא על רציונליים, אלא על קבוצות של ממשיים, כלומר על <strong>קבוצות של חתכים</strong>. בנסיון לפתור בעיה עם קבוצות של רציונליים, יצרתי בעיה קשה יותר, שמערבת קבוצות של חתכים ולא סתם של רציונליים; אלא שהבניה שלי חזקה מספיק כדי להתמודד עם זה.

מה שאני צריך להוכיח הוא

<ul> <li>אם {% equation %}S\subseteq\mathbb{F}{% endequation %} היא קבוצה לא ריקה וחסומה מלעיל, אז {% equation %}\sup S{% endequation %} קיים.</li>

</ul>

בהינתן {% equation %}S{% endequation %} כזו, איך אני אבנה פורמלית את החתך שיהיה {% equation %}\sup S{% endequation %}? אצל קנטור הבניה שלי הייתה די מסובכת, אבל כאן הבניה היא טריוויאלית לגמרי, ותהיה מאוד מוכרת לכל מי שלמדו קורס בתורת הקבוצות: נגדיר {% equation %}B=\bigcup S{% endequation %}, כלומר {% equation %}B{% endequation %} היא הקבוצה שאבריה הם האיחוד של כל קבוצות {% equation %}S{% endequation %}; {% equation %}a\in B{% endequation %} אם ורק אם קיים {% equation %}A\in S{% endequation %} כך ש-{% equation %}a\in A{% endequation %}.

כרגיל, השאלה הראשונה אחרי בניה כזו היא למה {% equation %}B{% endequation %} הוא חתך בכלל. הוא לא ריק כי הוא איחוד של קבוצות לא ריקות (זכרו ש-{% equation %}S{% endequation %} לא ריקה אז היא כוללת לפחות חתך אחד, והוא לא ריק כי הוא חתך). למה ש-{% equation %}B{% endequation %} לא יהיה כל {% equation %}\mathbb{Q}{% endequation %}? כאן נכנסת הדרישה ש-{% equation %}S{% endequation %} תהיה חסומה מלעיל. כלומר, קיים חתך {% equation %}C{% endequation %} כך ש-{% equation %}A\le C{% endequation %} לכל {% equation %}A\in S{% endequation %} , ולכן כפי שראינו {% equation %}A\subseteq C{% endequation %} לכל {% equation %}A\in S{% endequation %} כך שגם {% equation %}B\subseteq C{% endequation %}, אבל מכיוון ש-{% equation %}C{% endequation %} הוא חתך אז {% equation %}C\ne\mathbb{Q}{% endequation %} וזה גורר שגם {% equation %}B\ne\mathbb{Q}{% endequation %}.

כדי לראות סגירות כלפי מטה, נניח ש-{% equation %}b\in B{% endequation %} וניקח {% equation %}a<b{% endequation %} כלשהו. מכיוון ש-{% equation %}b\in B{% endequation %} אז קיים {% equation %}A\in S{% endequation %} כך ש-{% equation %}b\in A{% endequation %}, ומכיוון ש-{% equation %}a<b{% endequation %} ו-{% equation %}A{% endequation %} חתך אז {% equation %}a\in A{% endequation %} ומכיוון ש-{% equation %}A\subseteq B{% endequation %} אז {% equation %}a\in B{% endequation %} - טיעון תורת-קבוצתי סטנדרטי ופשוט. אותו הדבר עבור תכונה 3: מכיוון ש-{% equation %}b\in A{% endequation %} אז מתכונה 3 עבור {% equation %}A{% endequation %} קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}b<a{% endequation %}, ומכיוון ש-{% equation %}a\in B{% endequation %} סיימנו. אז {% equation %}B{% endequation %} הוא חתך; רק נשאר להראות שהוא חסם עליון של {% equation %}S{% endequation %}.

זה ש-{% equation %}B{% endequation %} הוא חסם <strong>מלעיל</strong> זה ברור: {% equation %}A\subseteq B{% endequation %} לכל {% equation %}A\in S{% endequation %} ולכן {% equation %}A\le B{% endequation %} לכל {% equation %}A\in S{% endequation %}, וזו בדיוק ההגדרה של חסם מלעיל. רק נותר להראות ש-{% equation %}B{% endequation %} היא החסם מלעיל המינימלי. אז בואו ניקח חתך {% equation %}C{% endequation %} <strong>כלשהו</strong> כך ש-{% equation %}C<B{% endequation %}, כלומר {% equation %}C\subset B{% endequation %}. זה אומר שיש {% equation %}b\in B{% endequation %} כך ש-{% equation %}b\notin C{% endequation %}, כלומר קיים {% equation %}A\in S{% endequation %} כך ש-{% equation %}b\in A{% endequation %} עכשיו, תזכרו מה ראינו קודם: בהכרח מתקיים {% equation %}A\subseteq C{% endequation %} או {% equation %}C\subseteq A{% endequation %}. מכיוון שיש ב-{% equation %}A{% endequation %} איבר שאין ב-{% equation %}C{% endequation %}, מה שחייב לקרות הוא {% equation %}C\subset A{% endequation %}, כלומר {% equation %}C<A{% endequation %} ולכן {% equation %}C{% endequation %} אינו חסם מלעיל של {% equation %}S{% endequation %}. במילים אחרות: אם {% equation %}C{% endequation %} הוא חסם מלעיל של {% equation %}S{% endequation %} הוא לא יכול לקיים {% equation %}C<B{% endequation %} אז בהכרח מתקיים {% equation %}B\le C{% endequation %}, וזה בדיוק מה שמראה ש-{% equation %}B{% endequation %} הוא חסם עליון.

זהו, זה היה ממש קל! אז מה בעצם העוקץ? מה מסובך בבניה הזו של דדקינד? ובכן, הכפל. זה יהיה קצת לא נעים.

<h2>הכפל. זה יהיה קצת לא נעים</h2>

למה שהכפל יהיה לא נעים? שתי סיבות. ראשית, להבדיל מחיבור, כאן ההגדרה הנאיבית לא עובדת. להגדיר {% equation %}A\cdot B\triangleq\left\{ ab\ |\ a\in A,b\in B\right\} {% endequation %} לא הולך לתת לנו אפילו חתך. למשל, אם {% equation %}A,B{% endequation %} שניהם שליליים, אז המכפלה של כל זוג איברים מתוכם תהיה מספר חיובי - ואין כזה דבר, חתך שאין בו שליליים (כי מרגע ש-{% equation %}a{% endequation %} כלשהו בחתך, גם כל מספר שקטן ממנו בחתך). אבל לא נורא, את הבעיה הזו אפשר לתקן על ידי כך שדורשים במפורש סגירות כלפי מטה, כלומר מגדירים {% equation %}A\cdot B\triangleq\left\{ q\in\mathbb{Q}\ |\ \exists a\in A,b\in B:q\le ab\right\} {% endequation %}. כלומר - לוקחים מכפלות, ולכל מכפלה כזו מכניסים אל {% equation %}AB{% endequation %} את מי שברור שצריכים להיות שם - המספרים שקטנים או שווים למכפלה.

זה עדיין לא עובד.

זה לא עובד, כי מספרים שליליים הם יצורים מוזרים למדי. יש את הקטע הזה <a href="https://gadial.net/2017/07/30/minus_minus/">שמכפלה של שני שליליים היא מספר חיובי</a>, וזה יוביל באופן בלתי נמנע לבעיות. בואו נסתכל למשל על החתך {% equation %}A_{1}=\left\{ q\in\mathbb{Q}\ |\ q<1\right\} {% endequation %}. הוא מייצג את 1 והיינו מצפים שיתקיים {% equation %}A_{1}\cdot A_{1}=A_{1}{% endequation %}, אבל הרי {% equation %}-2\in A_{1}{% endequation %}, למשל, אז על פי ההגדרה שנתתי למעלה, {% equation %}4=\left(-2\right)\cdot\left(-2\right)\in A_{1}\cdot A_{1}{% endequation %}. אבל זה לא ייגמר שם - אפשר לקבל כל מספר רציונלי גדול כרצוננו על ידי כפל של המינוס שלו במינוס 1. אז מה שנקבל בסוף יהיה {% equation %}A_{1}\cdot A_{1}=\mathbb{Q}{% endequation %}, כלומר אפילו לא מקבלים חתך. נראה שהדרך ההגיונית היחידה להגדיר כפל היא פשוט לא להרשות למספרים השליליים להשתתף. אבל אם הם לא משתתפים, מה יקרה למשל עם {% equation %}A_{-1}\cdot A_{-1}{% endequation %}? זו מכפלה של שתי קבוצות שהאיברים <strong>היחידים</strong> שלהן הם שליליים. אז המכפלה תהיה קבוצה ריקה? גם זה לא חתך. בקיצור, עסק ביש.

נקודת האור בכל הסיפור הזה היא שכל עוד אנחנו מסתכלים רק על מספרים <strong>חיוביים</strong>, הכל עובד כמו שצריך. זה מאפשר לי להתחיל את הגדרת הכפל עבור חתכים חיוביים, ולהתקדם משם. אז הנה ההגדרה הראשונית:

<ul> <li>אם {% equation %}A,B>0{% endequation %} אז {% equation %}A\cdot B\triangleq\left\{ q\in\mathbb{Q}\ |\ \exists a>0\in A,b>0\in B:q\le ab\right\} {% endequation %}</li>

</ul>

כלומר, עבור {% equation %}A,B{% endequation %} חיוביים אנחנו כופלים את כל האיברים <strong>החיוביים</strong> שלהם, ואז לוקחים את כל מה שקטן או שווה לזה. למה זה יוצא חתך? זה לא ריק כי אם {% equation %}A,B{% endequation %} חיוביים אז יש בהם {% equation %}a,b>0{% endequation %} ולכן {% equation %}ab\in AB{% endequation %}. זה לא {% equation %}\mathbb{Q}{% endequation %} כי {% equation %}A,B{% endequation %} חתכים ולכן קיימים {% equation %}q,p{% endequation %} שלא שייכים אליהם וזה כזכור אומר ש-{% equation %}a<q,b<p{% endequation %} <strong>לכל</strong> {% equation %}a\in A,b\in B{% endequation %} ולכן {% equation %}ab<qp{% endequation %} <strong>לכל</strong> האיברים {% equation %}a,b{% endequation %} הללו כך שכל אברי {% equation %}AB{% endequation %} קטנים מ-{% equation %}qp{% endequation %}.

תכונה 2, של הסגירות כלפי מטה, נובעת מיידית מההגדרה של {% equation %}AB{% endequation %}. נותרה רק תכונה 3: אם {% equation %}q\in AB{% endequation %} אז יש {% equation %}a\in A,b\in B{% endequation %} כך ש-{% equation %}q\le ab{% endequation %}. מכיוון ש-{% equation %}A,B{% endequation %} חתכים אז יש {% equation %}a^{\prime}\in A,b^{\prime}\in B{% endequation %} כך ש-{% equation %}a<a^{\prime},b<b^{\prime}{% endequation %} ולכן {% equation %}q\le ab<a^{\prime}b^{\prime}{% endequation %} וקיבלנו את תכונה 3. אז אמנם לא היה קל למצוא הגדרה שנותנת חתך, אבל עכשיו שהצטמצמנו קצת היה קל להוכיח שבהגדרה המצומצמת מקבלים אחד כזה.

עכשיו אפשר לעבור לקומוטטיביות ואסוציאטיביות:

<ul> <li>{% equation %}A\cdot B=B\cdot A{% endequation %} </li>


<li>{% equation %}\left(A\cdot B\right)\cdot C=A\cdot\left(B\cdot C\right){% endequation %}</li>

</ul>

ההוכחות מאוד דומות למה שראינו על חיבור. קומוטטיביות נובעת מייד מזה ש-{% equation %}q\le ab{% endequation %} אם ורק אם {% equation %}q\le ba{% endequation %} (וזה בזכות הקומוטטיביות של הרציונליים). אסוציאטיביות, כרגיל, מרגישה קצת יותר טריקית אז אני אעשה אותה בצורה יותר מפורשת:

נניח ש-{% equation %}q\in\left(A\cdot B\right)\cdot C{% endequation %}, אז קיימים {% equation %}x\in A\cdot B{% endequation %} ו-{% equation %}c\in C{% endequation %}, חיוביים שניהם, כך ש-{% equation %}q\le xc{% endequation %}. זה אומר שעבור {% equation %}x{% endequation %} קיימים {% equation %}a\in A,b\in B{% endequation %} חיוביים כך ש-{% equation %}x\le ab{% endequation %}. לכן {% equation %}q\le\left(ab\right)c=a\left(bc\right){% endequation %} כשהשוויון נובע מהאסוציאטיביות של מספרים רציונליים. מכיוון ש-{% equation %}b,c{% endequation %} שניהם חיוביים אז {% equation %}bc\in B\cdot C{% endequation %} (כי עבור {% equation %}b,c{% endequation %} עצמם מתקיים ש-{% equation %}bc\le bc{% endequation %}) ולכן {% equation %}q\le a\left(bc\right){% endequation %} תואם את ההגדרה של {% equation %}q\in A\cdot\left(B\cdot C\right){% endequation %}, והכיוון השני דומה.

עכשיו אפשר סוף סוף לערבב את החיבור והכפל:

<ul> <li>{% equation %}A\cdot\left(B+C\right)=A\cdot B+A\cdot C{% endequation %}</li>

</ul>

אבל שימו לב: רק בהנחה ש-{% equation %}A,B,C>0{% endequation %} אחרת המכפלות {% equation %}AB,AC{% endequation %} לא יהיו מוגדרות היטב. מרגע ש-{% equation %}B,C>0{% endequation %} אנחנו מקבלים ש-{% equation %}B+C>0{% endequation %} (את זה הוכחנו כבר) ולכן גם המכפלה {% equation %}A\left(B+C\right){% endequation %} מוגדרת היטב. עכשיו אני אוכיח את הדיסטריביוטיביות בשיטה הסטנדרטית של הכלה דו-כיוונית:

ראשית, אם {% equation %}x\in A\left(B+C\right){% endequation %} זה אומר שקיימים {% equation %}a\in A{% endequation %} חיובי ו-{% equation %}y\in B+C{% endequation %} חיובי כך ש-{% equation %}x\le ay{% endequation %}. עכשיו הקטע הטריקי: אם אני סתם אומר שמ-{% equation %}y\in B+C{% endequation %} נובע שקיימים {% equation %}b\in B,c\in C{% endequation %} כך ש-{% equation %}y\in b+c{% endequation %} זה <strong>לא מספיק טוב</strong> כי ייתכן למשל ש-{% equation %}b{% endequation %} הוא שלילי (למשל, אם {% equation %}B=C=\left(-\infty,5\right){% endequation %} ואני לוקח {% equation %}y=3{% endequation %} ו-{% equation %}b=-1,c=4{% endequation %}). לא, אני צריך שיתקיים {% equation %}b,c>0{% endequation %} כדי להמשיך, אז אני אעשה "תיקון" קטן. בואו נניח בלי הגבלת הכלליות ש-{% equation %}b<0{% endequation %} ו-{% equation %}c>0{% endequation %}. אני רוצה להגדיל קצת את הערך של {% equation %}b{% endequation %} עד שיהפוך לחיובי. כל מה שאני אוסיף ל-{% equation %}b{% endequation %} יצטרך לרדת מ-{% equation %}c{% endequation %} - האם אני בטוח שזה לא יהפוך את {% equation %}c{% endequation %} לשלילי? ובכן, מכיוון שאני יודע ש-{% equation %}b+c>0{% endequation %} זה אומר ש-{% equation %}c>-b{% endequation %}, כלומר אני יכול לחסר את כל הערך המוחלט של {% equation %}b{% endequation %} מ-{% equation %}c{% endequation %} ועדיין ישאר לי עודף - וזה חשוב, כי אני אצטרך את העודף הזה, כי אני לא רוצה להגדיל את {% equation %}b{% endequation %} עד שיהפוך ל-0 אלא עד שיהפוך ל"משהו חיובי קטן". כמה קטן? קטן ככה ש:

<ol> <li>הוא עדיין שייך אל {% equation %}B{% endequation %}.</li>


<li>אם אני מחסר מ-{% equation %}c{% endequation %} <strong>גם</strong> את הערך המוחלט של {% equation %}b{% endequation %} וגם אותו אני עדיין מקבל משהו חיובי.</li>

</ol>

כלומר, זה טיעון טיפה מורכב יחסית לכמה שזה אמור להיות פשוט. מה שאני עושה הוא זה: ראשית, בגלל ש-{% equation %}B>0{% endequation %} אז {% equation %}0\in B{% endequation %} ולכן מתכונה 3 קיים {% equation %}\varepsilon_{1}>0{% endequation %} כך ש-{% equation %}\varepsilon_{1}\in B{% endequation %}. שנית, בגלל ש-{% equation %}c>-b{% endequation %} קיים {% equation %}\varepsilon_{2}>0{% endequation %} כך ש-{% equation %}c>-b+\varepsilon_{2}{% endequation %}. עכשיו אני אבחר {% equation %}\varepsilon=\min\left\{ \varepsilon_{1},\varepsilon_{2}\right\} {% endequation %}. בגלל ש-{% equation %}\varepsilon\le\varepsilon_{1}\in B{% endequation %} קיבלנו שגם {% equation %}\varepsilon\in B{% endequation %}, ובגלל ש-{% equation %}\varepsilon\le\varepsilon_{2}{% endequation %} קיבלנו ש-{% equation %}c>-b+\varepsilon{% endequation %} ולכן {% equation %}0<c+b-\varepsilon<c{% endequation %} כך ש-{% equation %}c+b-\varepsilon\in C{% endequation %}, וקיבלנו

{% equation %}y=b+c=\varepsilon+\left(c+b-\varepsilon\right){% endequation %}

וזו הצגה של {% equation %}y{% endequation %} בתור סכום של שני חיוביים מ-{% equation %}B,C{% endequation %}. זה מאפשר לי לחזור להוכחה של הדיסטריביוטיביות: ראיתי שקיימים {% equation %}a\in A,b\in B,c\in C{% endequation %} חיוביים כולם כך ש-{% equation %}x\le a\left(b+c\right)=ab+ac{% endequation %} כשהמעבר האחרון נובע מדיסטריביוטיביות הרציונליים. החיוביות של {% equation %}a,b,c{% endequation %} פירושה ש-{% equation %}ab\in AB{% endequation %} ו-{% equation %}ac\in AC{% endequation %} ולכן קיבלתי ש-{% equation %}x\le z{% endequation %} כאשר {% equation %}z=ab+ac\in AB+AC{% endequation %} ומכך ש-{% equation %}AB+AC{% endequation %} הוא חתך ומתכונה 2 אני אקבל ש-{% equation %}x\in AC+AC{% endequation %}. זה משלים את הכיוון הזה של ההוכחה.

בכיוון השני, נניח ש-{% equation %}x\in AB+AC{% endequation %}, כלומר יש {% equation %}a_{1},a_{2}\in A{% endequation %} ו-{% equation %}b,c{% endequation %}, חיוביים כולם, כך ש-{% equation %}x=y+z{% endequation %} עבור {% equation %}y\le a_{1}b{% endequation %} ו-{% equation %}z\le a_{2}c{% endequation %}. נניח בלי הגבלת הכלליות ש-{% equation %}a_{1}\le a_{2}{% endequation %}, כלומר {% equation %}a_{1}=a_{2}-\varepsilon{% endequation %}, אז

{% equation %}x\le a_{1}b+a_{2}c=a_{2}b+a_{2}c-\varepsilon b=a_{2}\left(b+c\right)-\varepsilon b\le a_{2}\left(b+c\right){% endequation %}

מכיוון ש-{% equation %}b,c{% endequation %} שניהם חיוביים כך גם {% equation %}b+c{% endequation %} ולכן {% equation %}a_{2}\left(b+c\right)\in A\left(B+C\right){% endequation %}, וקיבלנו ש-{% equation %}x\in A\left(B+C\right){% endequation %}. זה מסיים את הכיוון הזה של ההוכחה ומסיים עם דיסטריביוטיביות.

נשארנו עם שלושה דברים שצריך להוכיח על כפל:

<ul> <li>אם {% equation %}A,B\in P{% endequation %} אז {% equation %}A\cdot B\in P{% endequation %}</li>


<li>קיים איבר שמסומן ב-{% equation %}1{% endequation %} כך ש-{% equation %}0\ne1{% endequation %} ו-{% equation %}A\cdot1=A{% endequation %} לכל {% equation %}A{% endequation %}</li>


<li>לכל {% equation %}A\ne0{% endequation %} קיים איבר שמסומן ב-{% equation %}A^{-1}{% endequation %} ונקרא <strong>ההופכי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A\cdot A^{-1}=1{% endequation %}</li>

</ul>

את התכונה הראשונה טריוויאלי להוכיח: אם {% equation %}A>0,B>0{% endequation %} אז כפי שראינו קיימים {% equation %}a\in A,b\in B{% endequation %} ששניהם גדולים מ-0, ובגלל ש-{% equation %}0<ab{% endequation %} אז {% equation %}0\in AB{% endequation %} וזה מסיים את ההוכחה. למרבה השמחה, זה מסיים לגמרי עם יחס הסדר {% equation %}P{% endequation %}; לא נצטרך לחזור לשם אחרי שנגדיר כפל בצורה מלאה על כל החתכים, כי בכל מקרה את התכונה הזו היה צריך להוכיח רק עבור חתכים חיוביים.

עכשיו נעבור להגדרת 1. כמו עם 0, אנחנו כבר יודעים מי בעצם אמור להיות החתך המתאים ל-1: {% equation %}A_{1}=\left\{ q\in\mathbb{Q}\ |\ q<1\right\} {% endequation %}. ברור ש-{% equation %}A_{1}\ne A_{0}{% endequation %} כי {% equation %}0\in A_{1}{% endequation %} אבל {% equation %}0\notin A_{0}{% endequation %}, אבל למה {% equation %}A\cdot A_{1}=A{% endequation %} לכל {% equation %}A{% endequation %} חיובי? כיוון אחד הוא קל: אם {% equation %}a\in A\cdot A_{1}{% endequation %} אז {% equation %}a\le a^{\prime}\cdot q{% endequation %} כך ש-{% equation %}a^{\prime}\in A{% endequation %} וגם {% equation %}q<1{% endequation %}; אבל בגלל ש-{% equation %}q<1{% endequation %} נקבל {% equation %}a\le a^{\prime}\cdot q<a^{\prime}{% endequation %} והסגירות כלפי מטה של {% equation %}A{% endequation %} נותנת לנו {% equation %}a\in A{% endequation %}.

הכיוון השני טריקי יותר. ראשית, אם {% equation %}a\in A{% endequation %} מקיים {% equation %}a\le0{% endequation %} אז ברור ש-{% equation %}a\in A\cdot A_{1}{% endequation %} כי {% equation %}0\in A,A_{1}{% endequation %}. לכן אפשר להניח מראש ש-{% equation %}a>0{% endequation %}. במקרה הזה, מנין לנו ש-{% equation %}a\in A\cdot A_{1}{% endequation %}? הרי אין {% equation %}q\in A_{1}{% endequation %} שעבורו {% equation %}a\cdot q=a{% endequation %}, בשביל זה נצטרך {% equation %}q{% endequation %} גדול מדי (כי ה-{% equation %}q{% endequation %} הזה הוא פשוט 1...). אבל אפשר להתחכם - במקום להתחיל עם {% equation %}a{% endequation %} ולכפול אותו במשהו, להתחיל עם מישהו קצת יותר גדול מ-{% equation %}a{% endequation %}; תכונה 3 של חתכים נותנת לנו קיום של {% equation %}x\in A{% endequation %} כך ש-{% equation %}a<x{% endequation %}. אני רוצה למצוא {% equation %}q{% endequation %} כך ש-{% equation %}qx=a{% endequation %}, כלומר {% equation %}q=\frac{a}{x}{% endequation %} (אין בעיה לחלק ב-{% equation %}x{% endequation %} כי {% equation %}0<a<x{% endequation %}). מכיוון ש-{% equation %}0<a<x{% endequation %} אז {% equation %}0<q<1{% endequation %} ולכן {% equation %}q\in A_{1}{% endequation %} וקיבלנו {% equation %}a=x\cdot q\in A\cdot A_{1}{% endequation %}. זה מסיים את ההוכחה: {% equation %}A=A\cdot A_{1}{% endequation %}.

נשאר לטפל בהופכי, ושוב יש לנו שאלה של הגדרה: בהינתן {% equation %}A>0{% endequation %}, איך נכון להגדיר את {% equation %}A^{-1}{% endequation %}? הגדרת נגדי בחיבור הייתה טריקית ומעצבנת; האם בכפל אפשר סתם להגדיר בצורה "הטבעית" {% equation %}A^{-1}\triangleq\left\{ a^{-1}\ |\ a\in A,a>0\right\} {% endequation %}? ובכן, ממש לא! תחשבו למשל ש-{% equation %}A=\left(-\infty,3\right){% endequation %} אז היינו מצפים שיתקיים {% equation %}A^{-1}=\left(-\infty,\frac{1}{3}\right){% endequation %} אבל מכיוון ש-{% equation %}1\in A{% endequation %}, אם נהפוך אותו נקבל ש-{% equation %}1\in A^{-1}{% endequation %} וזה ממש לא אמור לקרות. יותר גרוע מזה, ככל שניקח איברים קרובים יותר ויותר ל-0 ב-{% equation %}A{% endequation %}, ההופכי שלהם ישאף לאינסוף - יוצא שנקבל את כל {% equation %}\mathbb{Q}{% endequation %}. לא, מה שאנחנו צריכים לעשות הוא כמו עם הנגדי - להסתכל לא על {% equation %}A{% endequation %} אלא על <strong>כל מי שלא </strong>ב-{% equation %}A{% endequation %}. אז אולי נגדיר {% equation %}A^{-1}\triangleq\left\{ b^{-1}\ |\ b\notin A\right\} {% endequation %}? זה כמעט יעבוד, אבל שוב יש לנו את הבעיה הזו עם נקודת הקצה שאנחנו לא רוצים שתהיה שייכת לחתך. זה מוביל אותנו להגדרה

<ul> <li>{% equation %}A^{-1}\triangleq\left\{ q\in\mathbb{Q}\ |\ \exists b\notin A:q<b^{-1}\right\} {% endequation %}</li>

</ul>

ראשית, למה {% equation %}A^{-1}{% endequation %} הוא חתך? בגלל ש-{% equation %}A\ne\mathbb{Q}{% endequation %} ו-{% equation %}0<A{% endequation %} קיים {% equation %}b>0{% endequation %} כך ש-{% equation %}b\notin A{% endequation %} ולכן ב-{% equation %}A^{-1}{% endequation %} יש את כל מי שקטן יותר מ-{% equation %}b^{-1}{% endequation %}, כך ש-{% equation %}A^{-1}\ne\emptyset{% endequation %}. מצד שני, קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}a>0{% endequation %} ולכן <strong>לכל</strong> {% equation %}x\notin A{% endequation %} מתקיים {% equation %}a<x{% endequation %}, כלומר {% equation %}a^{-1}>x^{-1}{% endequation %}, ולכן {% equation %}a^{-1}\notin A^{-1}{% endequation %} כך ש-{% equation %}A^{-1}\ne\mathbb{Q}{% endequation %}.

תכונת הסגירות כלפי מטה נובעת מההגדרה (אם {% equation %}p<q{% endequation %} ו-{% equation %}q\in A^{-1}{% endequation %} אז קיים {% equation %}b{% endequation %} מתאים כך ש-{% equation %}q<b^{-1}{% endequation %} ומטרנזיטיביות {% equation %}p<b^{-1}{% endequation %}). עבור תכונה 3, נניח ש-{% equation %}q\in A^{-1}{% endequation %}, אז קיים {% equation %}b\notin A{% endequation %} מתאים כך ש-{% equation %}q<b^{-1}{% endequation %} אבל מצפיפות הרציונליים נובע שקיים {% equation %}p{% endequation %} כך ש-{% equation %}q<p<b^{-1}{% endequation %} ולכן גם {% equation %}p\in A^{-1}{% endequation %}, וסיימנו.

שנית, האם {% equation %}A^{-1}>0{% endequation %}? בלי זה הכפל {% equation %}A\cdot A^{-1}{% endequation %} לא יהיה מוגדר בשלב הזה. אבל גם זה ברור - מכיוון ש-{% equation %}A>0{% endequation %} אז {% equation %}0\in A{% endequation %} ולכן אם {% equation %}b\notin A{% endequation %} אז {% equation %}0<b{% endequation %} ולכן {% equation %}0<b^{-1}{% endequation %}, כך ש-{% equation %}0\in A^{-1}{% endequation %}, מה שמראה ש-{% equation %}A^{-1}>0{% endequation %}.

נשאר רק להראות ש-{% equation %}A\cdot A^{-1}=1{% endequation %} וכרגיל נשתמש בהכלה דו כיוונית. בכיוון אחד, אם {% equation %}x\in A\cdot A^{-1}{% endequation %} אז יש {% equation %}a\in A{% endequation %} ו-{% equation %}q\in A^{-1}{% endequation %} כך ש-{% equation %}x\le aq{% endequation %}. על {% equation %}q{% endequation %} אנחנו יודעים ש-{% equation %}q<b^{-1}{% endequation %} עבור {% equation %}b\notin A{% endequation %}, ובגלל ש-{% equation %}b\notin A{% endequation %} זה אומר ש-{% equation %}a<b{% endequation %}, ולכן {% equation %}ab^{-1}<1{% endequation %} וזה מסיים את הכיוון הזה כי {% equation %}x\le aq<ab^{-1}<1{% endequation %}.

בכיוון השני, נניח ש-{% equation %}x<1{% endequation %} ונראה ש-{% equation %}x\in AA^{-1}{% endequation %}. כאן ההוכחה תסתבך ותהפוך לטכנית למדי ואני לא מכיר דרך אלגנטית להתחמק מזה. כדי להבין מה בעצם הבעיה, בואו נראה דוגמא: למשל, {% equation %}A=\left(-\infty,3\right){% endequation %} ואז{% equation %}A^{-1}=\left(-\infty,\frac{1}{3}\right){% endequation %} ונניח ש-{% equation %}x=\frac{1}{2}{% endequation %}. מה אני צריך לעשות? אני צריך למצוא שני איברים ב-{% equation %}A{% endequation %} וב-{% equation %}A^{-1}{% endequation %} שהמכפלה שלהם יוצאת {% equation %}\frac{1}{2}{% endequation %}. האם יש דרך "טבעית" לקבל אותם מתוך {% equation %}\frac{1}{2}{% endequation %} עצמו? אני לא רואה כזו; למשל, {% equation %}\frac{1}{2}\notin A^{-1}{% endequation %} אז אי אפשר סתם לבחור את {% equation %}\frac{1}{2}{% endequation %} ולכפול ב-1 שב-{% equation %}A{% endequation %}. מה שכן אפשר לעשות הוא לומר "אוקיי, בואו נבחר מ-{% equation %}A{% endequation %} איבר שממש קרוב ל-3 ומ-{% equation %}A^{-1}{% endequation %} איבר שממש קרוב אל {% equation %}\frac{1}{3}{% endequation %} ואז המכפלה שלהם תהיה ממש קרובה אל {% equation %}1{% endequation %} ומן הסתם גדולה מ-{% equation %}\frac{1}{2}{% endequation %}" וזה בדיוק מה שאני רוצה לעשות - אבל איך מפרמלים את ה"ממש קרוב ל-3" אם עבור חתך המספר שהוא מייצג לא נתון לנו באופן מפורש? האם יש דרך "נקייה" לעשות את זה? ובכן, כן, בערך.

הרעיון הוא זה: {% equation %}x<1{% endequation %} ולכן ראשית נמצא {% equation %}n{% endequation %} כך ש-{% equation %}x<1-\frac{1}{n+1}{% endequation %}. אנחנו יודעים שקיים {% equation %}n{% endequation %} כזה בזכות הארכימדיות של הרציונליים: אם נסתכל על {% equation %}\frac{1}{1-x}{% endequation %}, זה מספר רציונלי גדול מ-1 (כי המכנה שלו קטן מ-1 וגדול מ-0) ולכן קיים טבעי {% equation %}n{% endequation %} כך ש-{% equation %}\frac{1}{1-x}-1<n{% endequation %}, ועל ידי העברת אגפים נקבל {% equation %}x<1-\frac{1}{n+1}{% endequation %}.

עכשיו נשים לב שלכל {% equation %}m\ge n{% endequation %} מתקיים {% equation %}m+1\ge n+1{% endequation %} ולכן {% equation %}\frac{1}{m+1}\le\frac{1}{n+1}{% endequation %} ולכן {% equation %}-\frac{1}{m+1}\ge-\frac{1}{n+1}{% endequation %} ולכן

{% equation %}x<1-\frac{1}{n+1}\le1-\frac{1}{m+1}=\frac{m}{m+1}{% endequation %}

זה נותן לנו הערכה קצת יותר קונקרטית של הגודל של {% equation %}x{% endequation %} שאנחנו צריכים לעבור. עכשיו אפשר לבנות איבר של {% equation %}A{% endequation %} שיתקרב אל הקצה של {% equation %}A{% endequation %} "ממש קרוב". הדרך לבנות איבר כזה היא לקחת איבר "ממש קטן" של {% equation %}A{% endequation %} ולהתחיל לחבר אותו לעצמו עד שנגיע ממש אל הנקודה שבה האיבר עדיין ב-{% equation %}A{% endequation %} אבל אם נחבר אותו לעצמו עוד פעם אחת כבר נצא מגבולות {% equation %}A{% endequation %} (ואז, אחרי שניקח את ההופכי שלנו, נגיע לתוך {% equation %}A^{-1}{% endequation %}). 

את האיבר הממש קטן שלנו נבנה כך: ראשית, בגלל ש-{% equation %}A>0{% endequation %} קיים {% equation %}a>0{% endequation %} כך ש-{% equation %}a\in A{% endequation %}. מכיוון ש-{% equation %}a{% endequation %} היה איבר שרירותי הוא לא הכי עוזר לנו, אבל אם נחלק אותו לפרוסות מספיק קטנות זה יהיה טוב: נסתכל על {% equation %}0<\frac{a}{n}{% endequation %} ועכשיו ניקח מספר חיובי שקטן יותר מזה: {% equation %}q<\frac{a}{n}{% endequation %}. על פי תכונה 2 של חתכים, {% equation %}q\in A{% endequation %}.

עכשיו נתחיל לחבר את {% equation %}q{% endequation %} לעצמו, כלומר להסתכל על מכפלות מהצורה {% equation %}mq{% endequation %} כך ש-{% equation %}m{% endequation %} הוא מספר טבעי. אנחנו יודעים שעבור {% equation %}m=1{% endequation %}, {% equation %}mq\in A{% endequation %}; אנחנו גם יודעים שקיים {% equation %}m{% endequation %} כך ש-{% equation %}mq\notin A{% endequation %} אחרת היינו מקבלים ש-{% equation %}A=\mathbb{Q}{% endequation %} (לכל מספר רציונלי קיים {% equation %}m{% endequation %} כך ש-{% equation %}mq{% endequation %} גדול ממנו). אז בואו ניקח את {% equation %}m{% endequation %} להיות האיבר שמקיים ש-{% equation %}mq\in A{% endequation %} אבל {% equation %}\left(m+1\right)q\notin A{% endequation %}. שימו לב שבפרט צריך להתקיים {% equation %}m\ge n{% endequation %} כי אם היה מתקיים {% equation %}m<n{% endequation %} אז {% equation %}m+1\le n{% endequation %}, ולכן

{% equation %}\left(m+1\right)q<\frac{\left(m+1\right)a}{n}\le\frac{na}{n}=a\in A{% endequation %}

בסתירה לכך ש-{% equation %}\left(m+1\right)q\notin A{% endequation %}.

מכיוון ש-{% equation %}m\ge n{% endequation %} מתקיים, יש לנו את אי השוויון שהוכחנו קודם:

{% equation %}x<\frac{m}{m+1}{% endequation %}

בואו נחלק את הכל באיבר הגדול ביותר שמצאנו ב-{% equation %}A{% endequation %}, כלומר ב-{% equation %}mq{% endequation %}, ונקבל:

{% equation %}\frac{x}{mq}<\frac{m}{m+1}\frac{1}{mq}=\frac{1}{\left(m+1\right)q}{% endequation %}

ועכשיו, בגלל ש-{% equation %}\left(m+1\right)q\notin A{% endequation %} אז ב-{% equation %}A^{-1}{% endequation %} יש כל איבר ש<strong>קטן יותר</strong> מההופכי שלו, כלומר שקטן יותר מ-{% equation %}\frac{1}{\left(m+1\right)q}{% endequation %}. זה עתה הראינו ש-{% equation %}\frac{x}{mq}{% endequation %} הוא איבר כזה, כלומר {% equation %}\frac{x}{mq}\in A^{-1}{% endequation %}, ויחד עם זה ש-{% equation %}mq\in A{% endequation %} קיבלנו ש-{% equation %}x=\left(mq\right)\cdot\frac{x}{mq}\in A\cdot A^{-1}{% endequation %}, מה שמסיים את ההוכחה.

<h2>כפל עם חתכים שליליים</h2>

הגענו אל הישורת האחרונה. הנה מה שאנחנו צריכים להוכיח:

<ul> <li>{% equation %}A\cdot B=B\cdot A{% endequation %} </li>


<li>{% equation %}\left(A\cdot B\right)\cdot C=A\cdot\left(B\cdot C\right){% endequation %}</li>


<li>{% equation %}A\cdot\left(B+C\right)=A\cdot B+A\cdot C{% endequation %}</li>


<li>{% equation %}A\cdot1=A{% endequation %} לכל {% equation %}A{% endequation %}</li>


<li>לכל {% equation %}A\ne0{% endequation %} קיים איבר שמסומן ב-{% equation %}A^{-1}{% endequation %} ונקרא <strong>ההופכי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A\cdot A^{-1}=1{% endequation %}</li>

</ul>

את כל אלו הוכחנו כבר בהנחה ש-{% equation %}A,B,C>0{% endequation %}, אבל עכשיו אנחנו רוצים לטפל בכל {% equation %}A,B,C{% endequation %}, כולל שליליים. הצעד הראשון הוא <strong>להגדיר</strong> כפל שמעורבים בו חתכים שליליים, וכדי לעשות את זה אני רוצה להזכיר תכונה מהותית שמתקיימת בכל שדה: {% equation %}-\left(-A\right)=A{% endequation %}. התכונה הזו נובעת רק מאקסיומות החיבור של השדה, אז נוכל כבר עכשיו להוכיח שהיא מתקיימת עבור חתכים. ראשית נוכיח שמתקיים <strong>כלל הצמצום</strong>, כלומר שאם {% equation %}A+B=A+C{% endequation %} אז {% equation %}B=C{% endequation %}. אינטואיטיבית, אנחנו "מחברים את {% equation %}-A{% endequation %} לשני האגפים" אבל בפועל צריך להיות זהירים ולהשתמש רק במה שאנחנו יודעים:

{% equation %}B=0+B=\left(-A+A\right)+B=-A+\left(A+B\right){% endequation %}

עד כאן השתמשנו בכך ש-0 הוא אדיש, בכך שלכל {% equation %}A{% endequation %}, מתקיים {% equation %}A+\left(-A\right)=0{% endequation %} (וגם בקומוטטיביות כי הפכתי את הסדר ביניהם) ובאסוציאטיביות (המעבר האחרון). עכשיו אני אשתמש בנתון ואקבל

{% equation %}-A+\left(A+B\right)=-A+\left(A+C\right)=\left(-A+A\right)+C=0+C=C{% endequation %}

אז קיבלתי שרשרת שוויונים שמראה ש-{% equation %}B=C{% endequation %}.

עכשיו, אפשר להשתמש בכלל הצמצום כדי להראות שהנגדי הוא יחיד: שאם {% equation %}A+B=0{% endequation %} אז {% equation %}B=-A{% endequation %}: הרי עבור {% equation %}-A{% endequation %} מתקיים {% equation %}A+\left(-A\right)=0=A+B{% endequation %} אז מצמצום ה-{% equation %}A{% endequation %} משני האגפים נישאר עם {% equation %}-A=B{% endequation %}. עכשיו, מכיוון ש-{% equation %}\left(-A\right)+A=0{% endequation %} המסקנה היא ש-{% equation %}A=-\left(-A\right){% endequation %}.

את זה כאמור הוכחנו פורמלית עבור חתכים, אבל אחרי שמגדירים כפל אפשר לקחת את הכללים הללו הלאה. באופן כללי, אם יש לי שדה ואיברים {% equation %}x,y{% endequation %} בתוכו, אז מתקיים:

<ul> <li>{% equation %}\left(-x\right)y=-\left(xy\right)=x\left(-y\right){% endequation %}</li>


<li>{% equation %}\left(-x\right)\left(-y\right)=xy{% endequation %}</li>

</ul>

אני הולך <strong>להגדיר</strong> את הכפל עבור חתכים שליליים בצורה שתבטיח שהדברים הללו יתקיימו (כי אם ההגדרה לא נותנת את הדברים הללו, מה שאני מגדיר לא יכול להיות שדה). איך מוכיחים אותם? אז למשל, כדי להוכיח את {% equation %}\left(-x\right)y=-\left(xy\right){% endequation %} ראיתי עכשיו שאני צריך להוכיח {% equation %}\left(-x\right)y+xy=0{% endequation %} ואת זה עושים עם דיסטריביוטיביות:

{% equation %}\left(-x\right)y+xy=\left(-x+x\right)y=0\cdot y=0{% endequation %}

כשאני משתמש בכך שכפל ב-0 מחזיר 0 (כי {% equation %}0\cdot y=\left(0+0\right)\cdot y=0\cdot y+0\cdot y{% endequation %} ועכשיו משתמשים בכלל הצמצום).

גם ההוכחה של {% equation %}-\left(xy\right)=x\left(-y\right){% endequation %} דומה, ולכן נשאר רק להוכיח את {% equation %}\left(-x\right)\left(-y\right)=xy{% endequation %}. בשביל להוכיח את זה, ראשית נשתמש ב-{% equation %}\left(-x\right)y=-\left(xy\right){% endequation %} רק כשאנחנו מחליפים את {% equation %}y{% endequation %} ב-{% equation %}-y{% endequation %} ונקבל

{% equation %}\left(-x\right)\left(-y\right)=-\left(x\left(-y\right)\right){% endequation %}

עכשיו נשתמש ב-{% equation %}x\left(-y\right)=-\left(xy\right){% endequation %} ונקבל

{% equation %}-\left(x\left(-y\right)\right)=-\left(-\left(xy\right)\right){% endequation %}

ולסיום נשתמש בתכונה המהותית שבה התחלתי, כלומר ש-{% equation %}-\left(-\left(xy\right)\right)=xy{% endequation %}, וקיבלתי {% equation %}\left(-x\right)\left(-y\right)=xy{% endequation %}, כמו שרציתי.

בשביל מה כל זה היה טוב? כי כזכור, עבור חתך {% equation %}A{% endequation %} יש שלוש אפשרויות: או ש-{% equation %}A>0{% endequation %} (ואז כבר הגדרנו עליו כפל), או ש-{% equation %}A=0{% endequation %} (ואז כפל בו פשוט יהיה 0) או ש-{% equation %}-A>0{% endequation %} ואז כדי להגדיר כפל על {% equation %}A{% endequation %} אפשר להיעזר בכפל על {% equation %}-A{% endequation %} ולהגדיר בהתאם לכללים שזה עתה ראינו.

בואו נכתוב במפורש את ההגדרה המלאה לכפל של {% equation %}A,B{% endequation %}. היא מתבססת בדיוק על החלוקה הזו למקרים אפשריים:

<ol> <li>אם {% equation %}A=0{% endequation %} או {% equation %}B=0{% endequation %} אז {% equation %}AB\triangleq0{% endequation %}</li>


<li>אם {% equation %}A,B>0{% endequation %} אז {% equation %}AB\triangleq\left\{ q\in\mathbb{Q}\ |\ \exists a>0\in A,b>0\in B:q\le ab\right\} {% endequation %}</li>


<li>אם {% equation %}A<0,B>0{% endequation %} אז {% equation %}AB\triangleq-\left(\left(-A\right)B\right){% endequation %}</li>


<li>אם {% equation %}A>0,B<0{% endequation %} אז {% equation %}AB\triangleq-\left(A\left(-B\right)\right){% endequation %}</li>


<li>אם {% equation %}A<0,B<0{% endequation %} אז {% equation %}AB\triangleq\left(-A\right)\left(-B\right){% endequation %}</li>

</ol>

בכל שלוש ההגדרות האחרונות ברשימה אני משתמש בהגדרה הקודמת, עבור כפל של חיוביים: מה שמוכפל בתוך הסוגריים הוא תמיד שני חתכים חיוביים, ואני בסך הכל לוקח את הנגדי של התוצאה במקרה שבו אחד מהחתכים חיובי והשני שלילי.

זו ההגדרה, רק נותר להראות שהיא עובדת. זה כמובן מערב בדיקה של המון מקרים אז אני לא אוכיח את הכל, אבל בואו נראה את המהות של כל דבר.

ראשית, קומוטטיביות.

<ul> <li>{% equation %}AB=BA{% endequation %}</li>

</ul>

נסתכל למשל על המקרה {% equation %}A<0,B>0{% endequation %}, אז

{% equation %}AB=-\left(\left(-A\right)B\right)=-\left(B\left(-A\right)\right)=BA{% endequation %}

בואו נבין מה קרה פה: המעבר הראשון הוא פשוט ההגדרה. המעבר השני הוא שימוש בקומוטטיביות עבור מכפלה של שני חיוביים, שכבר הוכחתי. המעבר השלישי הוא שוב הההגדרה, אבל לא אותה הגדרה; ההגדרה הראשונה הייתה שורה 3 (כשהאיבר השמאלי במכפלה שלילי) וכאן אני משתמש בהגדרה שבשורה 4 (כשהאיבר הימני במכפלה שלילי).

עכשיו לאסוציאטיביות: 

<ul> <li>{% equation %}\left(AB\right)C=A\left(BC\right){% endequation %}</li>

</ul>

למשל, אם {% equation %}A<0,B>0,C<0{% endequation %}. אז

{% equation %}\left(AB\right)C=\left[-\left(\left(-A\right)B\right)\right]C{% endequation %}

כאן אני משתמש בהגדרה של שורה 3. עכשיו יש לי את הכפל של שני החיוביים {% equation %}\left(-A\right)B{% endequation %}, וכפל של שני חיוביים נותן חיובי (את זה כבר הוכחנו קודם) ולכן המינוס שלהם הוא שלילי, ולכן קיבלתי ביטוי מהצורה {% equation %}XY{% endequation %} כאשר {% equation %}X<0{% endequation %} וגם {% equation %}Y<0{% endequation %} (במקרה הזה {% equation %}X=-\left[\left(-A\right)B\right]{% endequation %} ואילו {% equation %}Y=C{% endequation %}) ולכן אותו אפשר לפתוח על פי שורה 5:

{% equation %}\left[-\left(\left(-A\right)B\right)\right]C=\left(-\left[-\left(\left(-A\right)B\right)\right]\right)\left(-C\right){% endequation %}

זה נראה די מזעזע אבל יש אור בקצה המנהרה - את הביטוי {% equation %}-\left[-\left(\left(-A\right)B\right)\right]{% endequation %} אנחנו יודעים לפשט עם הזהות {% equation %}-\left(-A\right)=A{% endequation %} שהראיתי בהתחלה: {% equation %}-\left[-\left(\left(-A\right)B\right)\right]=\left(-A\right)B{% endequation %} ולכן נקבל

{% equation %}\left(-\left[-\left(\left(-A\right)B\right)\right]\right)\left(-C\right)=\left(\left(-A\right)B\right)\left(-C\right){% endequation %}

עכשיו יש לנו מכפלה מהצורה {% equation %}\left(XY\right)Z{% endequation %} רק שהפעם כל המוכפלים הם חיוביים, כי {% equation %}A,C{% endequation %} השליליים הוחלפו ב-{% equation %}-A,-C{% endequation %} החיוביים, אז אנחנו יכלום להשתמש באסוציאטיביות שכבר הוכחנו עבור חיוביים ולקבל

{% equation %}\left(\left(-A\right)B\right)\left(-C\right)=\left(-A\right)\left(B\left(-C\right)\right){% endequation %}

הביטוי {% equation %}B\left(-C\right){% endequation %} תואם את שורה 4 במובן הבא: אנחנו יודעים <strong>שהנגדי שלו</strong> הוא {% equation %}BC{% endequation %}, אז בגלל היחידות של הנגדי שהוכחנו קודם אפשר לכתוב {% equation %}B\left(-C\right)=-\left(BC\right){% endequation %} ולכן

{% equation %}\left(-A\right)\left(B\left(-C\right)\right)=\left(-A\right)\left(-\left(BC\right)\right){% endequation %}

עכשיו שימו לב מה קורה פה: אנחנו יודעים ש-{% equation %}A<0{% endequation %} כי מזה התחלנו, ובנוסף אנחנו יודעים ש-{% equation %}BC<0{% endequation %} כי ראינו ש-{% equation %}B\left(-C\right)=-\left(BC\right){% endequation %} ואגף שמאל הוא מכפלת שני חיוביים ולכן חיובי, ולכן <strong>הנגדי</strong> של {% equation %}BC{% endequation %} הוא חיובי, ולכן {% equation %}BC{% endequation %} שלילי (באופן כללי שורות 3-4 בהגדרה מראות לנו שמכפלה של חיובי בשלילי היא שלילית). זה אומר ש-{% equation %}\left(-A\right)\left(-\left(BC\right)\right){% endequation %} הוא ביטוי שהוא מכפלה של שני <strong>נגדיים</strong> של שליליים - בדיוק מה שקורה באגף ימין של שורה 5, ולכן שווה לאגף שמאל:

{% equation %}\left(-A\right)\left(-\left(BC\right)\right)=A\left(BC\right){% endequation %}

וסיימנו סוף סוף - {% equation %}\left(AB\right)C=A\left(BC\right){% endequation %}.

זו הייתה הוכחה של מקרה אחד של האסוציאטיביות.

מתוך 27 אפשרויות.

כמובן, אני עושה כאן הגזמה קומית, 27 אפשרויות זה רק אם מביאים בחשבון כל אחת משלוש הסיטואציות האפשריות לכל אחד מהחתכים: {% equation %}A>0{% endequation %} או {% equation %}A=0{% endequation %} או {% equation %}A<0{% endequation %}. אבל אם ולו אחד מהחתכים מקיים {% equation %}A=0{% endequation %} אז המכפלה הסופית תצא 0 בשני האגפים והשוויון טריוויאלי, אז אין מה להוכיח פה, ואנחנו מצטמצמים אל "רק" 8 אפשרויות. מתוכן אחת היא האפשרות שכולם חיוביים שבה טיפלנו במפורש קודם, ועוד אחת ראינו כרגע, וכל היתר הן אותו דבר כמו מה שעשינו כרגע - שימוש זהיר בחוקי הצמצומים של מינוס ובהגדרות של הכפל במקרים שונים ומשונים. אני אוותר על יתר 6 המקרים אבל זה "תרגיל טוב" לנסות עצמאית אחד מהם.

מה עכשיו? דיסטריביוטיביות.

<ul> <li>{% equation %}A\left(B+C\right)=AB+AC{% endequation %}</li>

</ul>

דיסטריביוטיביות היא מקרה מעניין במיוחד כי {% equation %}B+C{% endequation %} הוא ביטוי שיכול לצאת גם חיובי וגם שלילי, תלוי בערכים הספציפיים של {% equation %}B,C{% endequation %}. אם {% equation %}B,C>0{% endequation %} שניהם אז {% equation %}B+C>0{% endequation %} באופן טריוויאלי ואם {% equation %}B,C<0{% endequation %} אז {% equation %}B+C<0{% endequation %} גם באופן טריוויאלי - בשני המקרים זה נובע ישירות מההגדרה של הסכום בתור קבוצת כל הסכומים. אבל אם למשל {% equation %}B>0{% endequation %} ו-{% equation %}C<0{% endequation %} הסכום יכול לצאת חיובי או שלילי. למשל אם {% equation %}B=\left(-\infty,2\right){% endequation %} ו-{% equation %}C=\left(-\infty,-3\right){% endequation %} הסכום יצא שלילי, {% equation %}\left(-\infty,-1\right){% endequation %} ואילו אם {% equation %}C=\left(-\infty,-1\right){% endequation %} הסכום יצא חיובי, {% equation %}\left(-\infty,1\right){% endequation %}. איכשהו ההוכחה צריכה לעבוד בכל אחד משני המקרים הללו למרות שהם לכאורה "הפוכים".

נתחיל מהסיטואציה הקלה יותר - {% equation %}A>0,B<0,C<0{% endequation %}. במקרה זה {% equation %}B<0,C<0{% endequation %} ולכן {% equation %}B+C<0{% endequation %} ולכן כל המכפלות {% equation %}A\left(B+C\right),AB,AC{% endequation %} מוגדרות לפי שורה 4:

{% equation %}A\left(B+C\right)=-\left[A\left(-\left(B+C\right)\right)\right]=\left[A\left(-\left(B+C\right)\right)\right]=-\left[A\left(\left(-B\right)+\left(-C\right)\right)\right]{% endequation %}

את המעבר האחרון צריך להצדיק; זה בעצם עוד חוק חיבור, {% equation %}-\left(x+y\right)=\left(-x\right)+\left(-y\right){% endequation %}. בשביל להצדיק אותו אפשר להסתכל על הסכום

{% equation %}\left[\left(-x\right)+\left(-y\right)\right]+\left(x+y\right)=\left(-x\right)+\left[\left(-y\right)+\left(y+x\right)\right]={% endequation %}

{% equation %}=\left(-x\right)+\left[\left(-y+y\right)+x\right]=-x+x=0{% endequation %}

ולהסיק ש-{% equation %}\left(-x\right)+\left(-y\right){% endequation %} הוא הנגדי של {% equation %}\left(x+y\right){% endequation %} - הכל פה הוא שימוש סטנדרטי באסוציאטיביות, קומוטטיביות והתכונות שראינו בהתחלה של החיבור. אז אפשר לחזור לדיסטריביוטיביות שלנו. הגענו לכך שבסוגריים יש לנו {% equation %}A\left(\left(-B\right)+\left(-C\right)\right){% endequation %}, ומכיוון ש-{% equation %}B,C<0{% endequation %} קיבלנו כאן ביטוי שתואם את הדיסטריביוטיביות במקרה שבו כל המעורבים הם חיוביים ואפשר להשתמש בכך שהוכחנו את המקרה הזה קודם:

{% equation %}-\left[A\left(\left(-B\right)+\left(-C\right)\right)\right]=-\left[A\left(-B\right)+A\left(-C\right)\right]=-\left(A\left(-B\right)\right)+\left(-\left(A\left(-C\right)\right)\right){% endequation %}

וביטוי כמו {% equation %}-\left(A\left(-B\right)\right){% endequation %} הוא אגף ימין של כלל 4 ולכן מקבלים

{% equation %}-\left(A\left(-B\right)\right)+\left(-\left(A\left(-C\right)\right)\right)=AB+AC{% endequation %}. אז זה היה קל, ואם {% equation %}A<0{% endequation %} זה יעבוד בערך אותו הדבר.

אם כן, בואו נעבור לסיטואציה הבעייתית: {% equation %}B<0,C>0{% endequation %} (ונניח ש-{% equation %}A>0{% endequation %} אבל {% equation %}A<0{% endequation %} יהיה דומה). כאן יש שלוש אפשרויות: או ש-{% equation %}B+C>0{% endequation %}, או ש-{% equation %}B+C=0{% endequation %}, או ש-{% equation %}B+C<0{% endequation %}. נתחיל מ-{% equation %}B+C=0{% endequation %}; במקרה הזה {% equation %}C=-B{% endequation %} ואז {% equation %}A\left(B+C\right)=0{% endequation %} וכמו כן 

{% equation %}AB+AC=AB+A\left(-B\right)=AB-AB=0{% endequation %}

כשהמעבר הלפני אחרון נובע משורה 3 בהגדרה: {% equation %}-\left(A\left(-B\right)\right)=AB{% endequation %}, כלומר {% equation %}A\left(-B\right)=-AB{% endequation %}.

עכשיו נניח ש-{% equation %}B+C>0{% endequation %} ונשתמש בטריק כדי להעביר את הסיטואציה לדיסטריביוטיביות שמערבת רק חיוביים. הטריק הוא לכתוב {% equation %}C=\left(B+C\right)+\left(-B\right){% endequation %}: ככה כתבנו את {% equation %}C{% endequation %} בתור סכום של שני חיוביים, ועכשיו נסתכל על

{% equation %}AC=A\left(\left(B+C\right)+\left(-B\right)\right)=A\left(B+C\right)+A\left(-B\right){% endequation %}

כשהמעבר השני הוא שימוש בדיסטריביוטיביות על חיוביים. עכשיו , מכיוון ש-{% equation %}B<0{% endequation %} אנחנו מקבלים מכלל 4 ש-{% equation %}A\left(-B\right)=-AB{% endequation %} ולכן קיבלנו

{% equation %}AC=A\left(B+C\right)-AB{% endequation %}

ועל ידי העברת אגפים מקבלים

{% equation %}A\left(B+C\right)=AB+AC{% endequation %}

ושוב - יש שלל מקרים אחרים לטפל בהם אבל שום טכניקה חדשה, אז אני אברח מזה באלגנטיות.

עכשיו צריך לטפל באיבר היחידה:

<ul> <li>{% equation %}A\cdot1=A{% endequation %} לכל {% equation %}A{% endequation %}</li>

</ul>

כבר הוכחנו את זה למקרה ש-{% equation %}A>0{% endequation %} וזה ברור במקרה ש-{% equation %}A=0{% endequation %}. אם {% equation %}A<0{% endequation %} אז בגלל ש-{% equation %}1>0{% endequation %} נקבל {% equation %}A\cdot1=-\left(\left(-A\right)\cdot1\right){% endequation %}. עבור {% equation %}-A>0{% endequation %} כבר ראינו ש-{% equation %}\left(-A\right)\cdot1=-A{% endequation %} ולכן 

{% equation %}A\cdot1=-\left(\left(-A\right)\cdot1\right)=-\left(-A\right)=A{% endequation %}

כפי שרצינו.

נותר רק דבר אחד - הופכי:

<ul> <li>לכל {% equation %}A\ne0{% endequation %} קיים איבר שמסומן ב-{% equation %}A^{-1}{% endequation %} ונקרא <strong>ההופכי</strong> של {% equation %}A{% endequation %} כך ש-{% equation %}A\cdot A^{-1}=1{% endequation %}</li>

</ul>

הראינו את זה עבור {% equation %}A>0{% endequation %} ולא צריך לטפל במקרה {% equation %}A=0{% endequation %}, אז נותר רק {% equation %}A<0{% endequation %}. במקרה הזה נסמן {% equation %}B=-A{% endequation %}, אז {% equation %}B>0{% endequation %} ולכן קיים {% equation %}B^{-1}{% endequation %} כך ש-{% equation %}B\cdot B^{-1}=1{% endequation %}. עכשיו אני אגדיר {% equation %}A^{-1}=-B^{-1}{% endequation %}. שימו לב שבגלל ש-{% equation %}B>0{% endequation %} גם {% equation %}B^{-1}>0{% endequation %} כך ש-{% equation %}A^{-1}<0{% endequation %} ולכן המכפלה {% equation %}A\cdot A^{-1}{% endequation %} תואמת את כלל מס' 5: {% equation %}AA^{-1}=\left(-A\right)\left(-A^{-1}\right)=BB^{-1}=1{% endequation %}, וסיימנו את כל מה שצריך להוכיח על חתכי דדקינד! 
