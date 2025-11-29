---
title: "חישוב קוונטי בגישה מתמטית, חלק ה': אלגוריתם דויטש-ג'וזה"
layout: post
categories:
  - חישוב קוונטי
tags:
  - חישוב קוונטי
description: "אלגוריתם דויטש-ג'וזה הוא הזדמנות ראשונה לראות בפעולה את אחד מהמרכיבים המרכזיים בחישוב קוונטי: התאבכות"
image: "2022/deutsch_jozsa_3_qubits.png"
---


<h2>מה אנחנו רוצים לפתור?</h2>

עד עכשיו בסדרת הפוסטים על חישוב קוונטי ראינו את הבסיס המתמטית שאפשר לצמצם לכמה משפטי מחץ:

<ul> <li>בחישוב קוונטי האובייקט שמשתנה עם הזמן הוא <strong>המצב הקוונטי</strong> של המערכת, שמיוצג בתור וקטור {% equation %}\left|\psi\right\rangle \in\mathbb{C}^{2^{n}}{% endequation %}.</li>


<li>סוג אחד של שינוי הוא כפל המצב {% equation %}v{% endequation %} במטריצה אוניטרית {% equation %}U\in\mathbb{C}^{2^{n}\times2^{n}}{% endequation %}, כלומר מבצעים {% equation %}\left|\psi\right\rangle \leftarrow U\left|\psi\right\rangle {% endequation %}.</li>


<li>סוג נוסף של שינוי הוא <strong>מדידה</strong>, שבגרסה הפשוטה שלנו מוגדרת לכל קיוביט עבור שני אופרטורים {% equation %}M_{0},M_{1}{% endequation %} (שתלויים בקיוביט), בחירת {% equation %}M_{0}{% endequation %} בהסתברות {% equation %}\left\langle \psi\right|M_{0}\left|\psi\right\rangle {% endequation %} ובחירת {% equation %}M_{1}{% endequation %} בהסתברות {% equation %}\left\langle \psi\right|M_{1}\left|\psi\right\rangle {% endequation %} ובהינתן ש-{% equation %}M_{i}{% endequation %} עלה בגורל, הפלט שחוזר מהמדידה הוא {% equation %}i{% endequation %} והיא מעבירה את המצב הקוונטי של המערכת למצב {% equation %}\left|\psi\right\rangle \leftarrow\frac{M_{i}\left|\psi\right\rangle }{\sqrt{\left\langle \psi\right|M_{i}\left|\psi\right\rangle }}{% endequation %}.</li>

</ul>

זה הכל. מה שמעניין פה הוא שאלו הם חישובים שלא מסובך במיוחד לתכנת גם במחשב סטנדרטי. אמנם אין לנו יכולת לשמור מספרים מרוכבים ברמת דיוק אינסופית, אבל אנחנו לא באמת צריכים את זה - הייצוגים הקיימים של מרוכבים במחשב עובדים מספיק טוב. למעשה, אין שום בעיה עקרונית לכתוב סימולטור של חישוב קוונטי שרץ במחשב רגיל, וזה אפילו תרגיל נחמד למי שרוצה ללמוד את התחום (מגלים מהר מאוד שהפעלת אופרטורים זה עסק קצת מעצבן ויש דרכי קיצור). זה גורם לאתגר הגדול של בניית מחשבים קוונטיים להיראות קצת מיותר - מה הטעם ליצור מכשיר הנדסי מסובך שהחישוב שהוא מבצע זה משהו שאפשר לעשות במחשב רגיל?

לנקודה הזו כבר התייחסתי בעבר. מכיוון שהאובייקט הספציפי שאנחנו שומרים ופועלים עליו הוא וקטור ב-{% equation %}\mathbb{C}^{2^{n}}{% endequation %}, כמות המידע שצריך לשמור, והזמן שלוקח לפעול עליה, גדלה <strong>אקספוננציאלית</strong> עם {% equation %}n{% endequation %}. עבור 50 קיוביטים, למחשבים רגילים מאוד מאתגר לסמלץ חישוב קוונטי; עבור 100 קיוביטים כבר אין על מה לדבר. נכון לכתיבת שורות אלו יש ליבמ מחשב קוונטי פעיל של 127 קיוביטים, למרות שהחישוב בו לא חף מבעיות (מתישהו אני מקווה בסדרת הפוסטים הזו להגיע לדבר על רעשים ותיקון שגיאות), וזו רק תחילת הדרך. כשיהיה חישוב קוונטי רציני, לא יהיה שום סיכוי לסמלץ אותו במחשב.

אבל זה עדיין לא עונה על השאלה האמיתית - <strong>בשביל מה זה טוב</strong>? אילו בעיות נוכל לפתור עם מחשבים קוונטיים שלא נוכל לפתור במחשב רגיל? הדוגמא הנפוצה שנזרקת לחלל באוויר בשלב הזה היא <strong>בעיית הפירוק לגורמים</strong> שהאלגוריתם הקוונטי של שור פותר ביעילות. זו דוגמא מצויינת, אבל יש בה בעיה פשוטה - זה אלגוריתם מסובך יחסית וקשה להציג אותו ישר אחרי שמבינים איך עובד חישוב קוונטי. אז בפוסט הזה אני רוצה להציג בעיה פשוטה הרבה יותר, שנפתרת על ידי אלגוריתם פשוט בצורה קיצונית, אבל כבר היא מספיקה לתת תחושה טובה למה בחישוב קוונטי יש "יותר" מאשר בחישוב קלאסי. האלגוריתם שאציג נקרא <strong>אלגוריתם דויטש-ג'וזה</strong>.

נתחיל עם להציג את הבעיה עצמה. אני מזהיר מראש שזו <strong>לא</strong> בעיה "מעניינת". לפתור אותה לא הולך לשבור מערכות הצפנה. היא אפילו נראית די מלאכותית. היופי בבעיה הוא שקל מאוד להבין למה נסיון לפתור אותה קלאסית יהיה קשה, ואז העובדה שהיא נפתרת בקלות קוונטית מחדדת מאוד את ההבדל.

הקלט לבעיה הוא פונקציה {% equation %}f:\left\{ 0,1\right\} ^{n}\to\left\{ 0,1\right\} {% endequation %}, כלומר פונקציה <strong>בינארית</strong> שמקבלת קלט שהוא מחרוזת באורך {% equation %}n{% endequation %} של ביטים (אפשר לחשוב עליה בתור מספר טבעי בתחום {% equation %}0,1,\ldots,2^{n}-1{% endequation %}) ועל כל קלט כזה מחזירה 0 או 1. הפונקציה נתונה לנו בתור <strong>קופסה שחורה</strong>, כלומר משהו שאנחנו לא יכולים לראות איך המימוש שלו עובד; הדבר היחיד שאנחנו יכולים לעשות הוא לחשב את {% equation %}f{% endequation %} על קלטים מסוימים. תחשבו על {% equation %}f{% endequation %} כאילו מה שמחשב אותו יושב על מחשב מרוחק, וכל מה שאנחנו יכולים לעשות הוא לשלוח לו מחרוזות של {% equation %}n{% endequation %} ביטים ולקבל חזרה פלט של ביט בודד.

מה שידוע לנו על {% equation %}f{% endequation %} זה שהיא בדיוק אחד משני הבאים:

<ul> <li>{% equation %}f{% endequation %} <strong>קבועה</strong>, כלומר לכל קלט {% equation %}x{% endequation %} מתקיים {% equation %}f\left(x\right)=0{% endequation %}, או שלכל קלט {% equation %}x{% endequation %} מתקיים {% equation %}f\left(x\right)=1{% endequation %}.</li>


<li>{% equation %}f{% endequation %} <strong>מאוזנת</strong>, כלומר בדיוק על חצי מהקלטים מתקבל 0 ועל החצי השני מתקבל 1. אם נסמן {% equation %}N=2^{n}{% endequation %}, זה אומר ש-{% equation %}\left|\left\{ x\in\left\{ 0,1\right\} ^{n}\ |\ f\left(x\right)=0\right\} \right|=\left|\left\{ x\in\left\{ 0,1\right\} ^{n}\ |\ f\left(x\right)=1\right\} \right|=\frac{N}{2}{% endequation %}.</li>

</ul>

המשימה שלנו: לקבל מה משני המקרים הללו מתקיים.

איך עושים את זה באופן קלאסי? ובכן, אם לא מערבים הסתברות בסיפור, די ברור שאנחנו חייבים {% equation %}\frac{N}{2}+1{% endequation %} קריאות ל-{% equation %}f{% endequation %}. למה? כי אנחנו תמיד חושבים מה יקרה <strong>במקרה הגרוע ביותר</strong>, והמקרה הגרוע ביותר הוא זה שבו אין לנו מזל - ש-{% equation %}f{% endequation %} היא מאוזנת, ואיכשהו כל {% equation %}\frac{N}{2}{% endequation %} ההפעלות הראשונות שלה שביצענו נפלו <strong>בדיוק</strong> על כל הערכים שעליהם {% equation %}f{% endequation %} נותנת 0. בשלב הזה אנחנו עדיין לא יכולים להגיד בודאות האם {% equation %}f{% endequation %} תהיה 0 על הכל, או רק על חצי. רק כשנחשב את הערך שלה על האיבר ה-{% equation %}\frac{N}{2}+1{% endequation %} נוכל להיות בטוחים: אם קיבלנו {% equation %}0{% endequation %} אז {% equation %}f{% endequation %} קבועה, ואם קיבלנו 1 אז {% equation %}f{% endequation %} מאוזנת.

להראות שגם אם מערבים הסתברות עדיין נזדקק למספר גדול של שאילות זה חישוב מסובך יותר ולא אעשה אותו כרגע, כי אני לא צריך - אלגוריתם דויטש-ג'וזה הולך להשתמש בקריאה <strong>אחת בלבד</strong> לפונקציה, ולהחזיר תשובה שהיא <strong>נכונה תמיד</strong>, ב-100 אחוז מהמקרים, אפילו אם חישוב קוונטי הוא לכאורה עניין הסתברותי. איך זה יעבוד? ובכן, זה דורש מהקופסה השחורה שמחשבת את {% equation %}f{% endequation %} להיות קוונטית בעצמה: במקום לחשב את {% equation %}f{% endequation %} על ביט ספציפי {% equation %}x{% endequation %} שנותנים, לחשב את {% equation %}f{% endequation %} על <strong>סופרפוזיציה</strong>, כלומר: הקלט ש-{% equation %}f{% endequation %} תקבל יהיה מצב על {% equation %}n{% endequation %} קיוביטים, {% equation %}\left|\psi\right\rangle =\sum_{x\in\left\{ 0,1\right\} ^{n}}\alpha_{x}\left|x\right\rangle {% endequation %} ואינטואיטיבית, הפלט יהיה

{% equation %}f\left(\sum_{x\in\left\{ 0,1\right\} ^{n}}\alpha_{x}\left|x\right\rangle \right)=\sum_{x\in\left\{ 0,1\right\} ^{n}}\alpha_{x}f\left(\left|x\right\rangle \right){% endequation %}

האינטואיציה הזו לא מלאה; בדויטש-ג'וזה נשתמש בקופסה שחורה שמתנהגת קצת שונה, ואחר כך נסביר איך עוברים מהאינטואיציה שאני מציג כאן אל הקופסה השחורה של דויטש-ג'וזה.

ייתכן מאוד שהצלחתי לאכזב אתכם עם ה"הקופסה השחורה תהיה קוונטית". זה נשמע כאילו שיניתי פתאום את הגדרת הבעיה, ואין פלא שעם מחשב קוונטי אפשר להשיג יותר. אבל נניח שהייתי אומר מלכתחילה שהקופסה השחורה היא קוונטית, האם מחשב קלאסי היה מצליח יותר? הוא לא מסוגל לייצר סופרפוזיציה של מצבים קוונטיים, כל מה שהוא היה יכול לעשות הוא לשלוח מצבי בסיס {% equation %}\left|x\right\rangle {% endequation %}. זה שהקופסה השחורה היא קוונטית לא עוזר לנו בלי שיהיה לנו מחשב קוונטי שמנצל את זה. עדיין, אני לגמרי מסכים שזו לא דוגמת מחץ כמו האלגוריתם של שור, שלא נזקק לקופסאות שחורות קוונטיות שכאלו; תזכרו שמה שאני עושה כרגע הוא לא לתת דוגמת מחץ לעליונות החישוב הקוונטי, אלא לתת תחושה ראשונית של הקסם הנחמד הזה.

<h2>איך דויטש-ג'וזה עובד?</h2>

דויטש-ג'וזה הוא אלגוריתם פשוט בצורה קיצונית:

<ol> <li>אתחלו מצב קוונטי אל {% equation %}\left|0^{n}\right\rangle {% endequation %}</li>


<li>הפעילו {% equation %}H{% endequation %} על כל הקיוביטים.</li>


<li>הפעילו את הקופסה השחורה על המצב שקיבלתם.</li>


<li>הפעילו {% equation %}H{% endequation %} על המצב שקיבלתם.</li>


<li>מדדו את כל הקיוביטים במצב שקיבלתם.</li>


<li>אם קיבלתם {% equation %}0^{n}{% endequation %}, אז {% equation %}f{% endequation %} קבועה; אם קיבלתם משהו אחר, אז {% equation %}f{% endequation %} מאוזנת.</li>

</ol>

הדבר היחיד שלא הסברתי עדיין איך הוא בדיוק עובד הוא שלב "הפעלת הקופסה השחורה". לצורך כך אני מניח שיש לי אופרטור אוניטרי {% equation %}U_{f}{% endequation %} שפועל בצורה הבאה על איבר בסיס {% equation %}\left|x\right\rangle {% endequation %}:

<ul> <li>{% equation %}U_{f}\left|x\right\rangle =\left(-1\right)^{f\left(x\right)}\left|x\right\rangle {% endequation %}</li>

</ul>

במילים אחרות: אם {% equation %}f\left(x\right)=0{% endequation %} אז {% equation %}U_{f}{% endequation %} לא משנה את {% equation %}\left|x\right\rangle {% endequation %} , ואם {% equation %}f\left(x\right)=1{% endequation %} אז הוא מכפיל אותו ב-{% equation %}-1{% endequation %}. זה מזכיר את האופרטור {% equation %}Z{% endequation %}, רק כזה שפועל בבת אחת על {% equation %}n{% endequation %} קיוביטים ותלוי בתכונות הספציפיות של {% equation %}f{% endequation %}. איך אפשר לממש אופרטור קוונטי כזה? נדבר על זה בהמשך.

הנה איור סכמטי של האלגוריתם, במקרה של שלושה קיוביטים:

<img src="{{site.baseurl}}{{site.post_images}}/2022/deutsch_jozsa_3_qubits.png" alt=""/>

אפשר גם לצייר את זה באופן כללי ל-{% equation %}n{% endequation %} קיוביטים בצורה קומפקטית:

<img src="{{site.baseurl}}{{site.post_images}}/2022/deutsch_jozsa_n_qubits.png" alt=""/>

הסימן שנראה כמו מחוג של מכשיר מדידה בצד ימין הוא, ובכן, מדידה. ה-{% equation %}H^{\otimes n}{% endequation %} הוא הפעלת {% equation %}H{% endequation %} על כל השערים, שתכף אתאר; אני מניח שהרעיון ברור.

כרגע אני רוצה לראות איך האלגוריתם פותר לנו את הבעיה. בסופו של דבר, להבין את האלגוריתם קם ונופל על להבין משהו כללי קצת יותר ושימושי מאוד: מה בעצם הפעלת {% equation %}H{% endequation %} על כל הקיוביטים עושה.

כזכור, {% equation %}H{% endequation %} הוא האופרטור שיוצר לנו סופרפוזיציה אחידה:

{% equation %}H\left|0\right\rangle =\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %}

{% equation %}H\left|1\right\rangle =\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}{% endequation %}

אבל זה עבור קיוביט יחיד. מה קורה כשמפעילים {% equation %}H{% endequation %} על כל אחד מהקיוביטים? מקבלים את ההרכבה של {% equation %}H\otimes I\otimes\ldots\otimes I{% endequation %} ו-{% equation %}I\otimes H\otimes\ldots\otimes I{% endequation %} וכן הלאה - זה יוצא האופטור {% equation %}H\otimes H\otimes\ldots\otimes H{% endequation %}, או בסימון מקוצר, {% equation %}H^{\otimes n}{% endequation %}. עכשיו, אם נפעיל את האופרטור הזה על המצב ההתחלתי {% equation %}\left|0^{n}\right\rangle {% endequation %} נקבל:

{% equation %}H^{\otimes n}\left|0^{n}\right\rangle =\left(H\left|0\right\rangle \right)\otimes\ldots\otimes\left(H\left|0\right\rangle \right)=\left(\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\right)\otimes\ldots\otimes\left(\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}\right){% endequation %}

מה שצריך לזכור על מכפלה טנזורית הוא האופן שבו היא מתנהגת בדומה למכפלה רגילה - אפשר להוציא החוצה סקלרים (את כל ה-{% equation %}\frac{1}{\sqrt{n}}{% endequation %}), ואפשר להשתמש בדיסטריביוטיביות. יש לנו כאן מכפלה של {% equation %}n{% endequation %} מחוברים מהצורה {% equation %}\left(\left|0\right\rangle +\left|1\right\rangle \right){% endequation %}; זו סיטואציה שמזכירה, למשל, את הבינום של ניוטון. כשאנחנו פותחים סוגריים, אנחנו מקבלים סכום שכולל את כל המחוברים שהם מהצורה של מכפלה של {% equation %}n{% endequation %} איברים שכל אחד מהם הוא או {% equation %}\left|0\right\rangle {% endequation %} או {% equation %}\left|1\right\rangle {% endequation %} - במילים אחרות, הסכום {% equation %}\sum_{y\in\left\{ 0,1\right\} ^{n}}\left|y\right\rangle {% endequation %}. לכן בסך הכל קיבלנו:

{% equation %}H^{\otimes n}\left|0^{n}\right\rangle =\frac{1}{\sqrt{2^{n}}}\sum_{y\in\left\{ 0,1\right\} ^{n}}\left|y\right\rangle {% endequation %}

זה מתאים יפה לאינטואיציה שלפיה {% equation %}H{% endequation %} יוצר סופרפוזיציה אחידה: כשהפעלנו אותו על כל הקיוביטים, קיבלנו סופרפוזיציה אחידה של כל {% equation %}2^{n}{% endequation %} אברי הבסיס האפשריים. שימו לב, זה כבר קסם בפני עצמו - הפעלנו רק {% equation %}n{% endequation %} שערים (זה לוקח זמן קצר) וקיבלנו סופרפוזיציה של מספר אקספוננציאלי של איברים.

מה שעשינו פה הוא להבין איך {% equation %}H^{\otimes n}{% endequation %} עובד על מצב בסיס אחד ספציפי: {% equation %}\left|0^{n}\right\rangle {% endequation %}. אבל איך הוא עובד על מצבים אחרים, כאלו שיש בהם גם 1-ים? כאן אנחנו מגיעים לנקודה הכי טכנית בפוסט, אבל גם הכי יפה שלו. כמו שתמיד כדאי כדי להבין משהו מסובך, כדאי להסתכל על דוגמא פשוטה קודם.

נניח שאני מפעיל את {% equation %}H^{\otimes3}{% endequation %} על המצב {% equation %}\left|101\right\rangle {% endequation %}. מה אני אקבל? על פי מה שראינו קודם, נקבל

{% equation %}H^{\otimes3}\left|101\right\rangle =\frac{1}{\sqrt{2^{3}}}\left(\left|0\right\rangle -\left|1\right\rangle \right)\left(\left|0\right\rangle +\left|1\right\rangle \right)\left(\left|0\right\rangle -\left|1\right\rangle \right){% endequation %}

כשאני פותח סוגריים אני עדיין אקבל את כל האיברים מהצורה {% equation %}\left|x\right\rangle {% endequation %}, אבל הפעם חלקם יהיו עם מקדם <strong>מינוס</strong>. מתי? ובכן, בואו נתחיל לפתוח את הסוגריים. נניח שאני בוחר מכל אחד משלושת הסוגרים את האיבר <strong>הראשון</strong>, אני אכפיל שלושה איברים מהצורה {% equation %}\left|0\right\rangle {% endequation %} ואקבל {% equation %}\left|000\right\rangle {% endequation %} - בלי סימן מינוס. ולמה שיהיה סימן מינוס? על ה-{% equation %}\left|0\right\rangle {% endequation %}-ים אין מינוס בכלל. כדי שיהיה מינוס, חייב להשתתף {% equation %}\left|1\right\rangle {% endequation %} בסיפור הזה. למשל, אם אני אקח את האיבר <strong>השני</strong> מהסוגר הראשון, ומשני האחרים את האיבר <strong>הראשון</strong>, אני אקבל {% equation %}-\left|100\right\rangle {% endequation %}.

לעומת זאת, אם אני אקח את האיבר <strong>השני</strong> מהסוג <strong>השני</strong> ומשני האחרים את הראשון, אני אקבל {% equation %}\left|010\right\rangle {% endequation %}, בלי מינוס. למה? כי בסוגר השני, ה-{% equation %}\left|1\right\rangle {% endequation %} מופיע בלי סימן מינוס. ולמה לא? כי במצב המקורי שעליו פעלנו, {% equation %}\left|101\right\rangle {% endequation %}, הסוגר השני מתאים לאיבר השני במחרוזת, כלומר אל 0. מכאן המסקנה היא שכדי לקבל מינוס, אני חייב לקחת את {% equation %}\left|1\right\rangle {% endequation %} מתוך סוגריים ששייכים לאיבר בקלט שהיה {% equation %}\left|1\right\rangle {% endequation %} בעצמו.

זה תנאי <strong>הכרחי</strong> כדי לקבל מינוס, אבל הוא לא מספיק, כי בואו נראה למשל מה שקורה כשאני לוקח את ה-{% equation %}\left|1\right\rangle {% endequation %} מכל שלושת זוגות הסוגריים. אני מקבל את המכפלה

{% equation %}-\left|1\right\rangle \otimes\left|1\right\rangle \otimes\left(-\left|1\right\rangle \right)=\left|111\right\rangle {% endequation %}

כלומר, הפעם קיבלתי איבר ללא מינוס כי בדיוק <strong>שני</strong> איברים במכפלה היו עם סימן מינוס. הסימן באיבר שאקבל בסוף תלוי בשאלות הבאות:

<ul> <li>האם מופיעים 1-ים במצב שעליו פעלנו?</li>


<li>האם מופיעים 1-ים במצב שאנחנו מסתכלים עליו כרגע בפלט?</li>


<li>האם יש אינדקסים שבהם מופיע 1 גם בקלט <strong>וגם</strong> בפלט?</li>


<li>האם המספר של האינדקסים הללו הוא <strong>אי זוגי</strong>?</li>

</ul>

זה מאוד מסורבל לדבר על זה ככה, אבל למרבה השמחה יש כלי מתמטי פשוט מאוד שמאפשר לתאר את זה בצורה שקל לעבוד איתה: <strong>מכפלה סקלרית מודולו </strong><strong>2</strong>. בהינתן שני וקטורים מאותו אורך, {% equation %}x=\left(x_{1},\ldots,x_{k}\right){% endequation %} ו-{% equation %}y=\left(y_{1},\ldots,y_{k}\right){% endequation %}, המכפלה הסקלרית שלהם היא {% equation %}x\cdot y=\sum_{i=1}^{k}x_{i}y_{i}{% endequation %}. אם {% equation %}x,y\in\left\{ 0,1\right\} ^{k}{% endequation %} אז המכפלה הסקלרית שלהם תהיה מספר שלם, ואפשר לקחת אותו מודולו 2 (לחלק ב-2 ולהחזיר את השארית; 0 אם המספר זוגי ו-1 אם הוא אי זוגי). 

אולי אתן אומרות "היי, זו כמו מכפלה פנימית!" וזה נכון - אפשר לחשוב על מכפלות פנימיות כאילו הן מוגדרות בעזרת סכום כזה, אבל אין למכפלה פנימית משמעות מעל {% equation %}\mathbb{Z}_{2}{% endequation %} (השדה שמעליו אנחנו עובדים כרגע במובלע) אלא רק מעל {% equation %}\mathbb{R},\mathbb{C}{% endequation %}; כי למשל, אחת הדרישות ממכפלה פנימית היא שאם {% equation %}x\ne0{% endequation %} אז {% equation %}\left\langle x,x\right\rangle >0{% endequation %} וזה בוודאי לא מתקיים כאן (חשבו על הוקטור {% equation %}x=11{% endequation %}). אבל גם בלי להיות מכפלה פנימית, למכפלה סקלרית כזו יש תכונות אלגבריות נחמדות, למשל {% equation %}\left(x+y\right)\cdot z=x\cdot z+y\cdot z{% endequation %}.

בעזרת מכפלה סקלרית אפשר לנסח מאוד בקלות את המהומה שהלכה קודם:

{% equation %}H^{\otimes n}\left|x\right\rangle =\frac{1}{\sqrt{2^{n}}}\sum_{y\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{x\cdot y}\left|y\right\rangle {% endequation %}

כי מה קורה כאן? המכפלה הסקלרית {% equation %}x\cdot y=\sum_{i=1}^{k}x_{i}y_{i}{% endequation %} בעצם סופרת את מספר האינדקסים {% equation %}i{% endequation %} שבהם <strong>גם</strong> {% equation %}x_{i}=1{% endequation %} <strong>וגם</strong> {% equation %}y_{i}=1{% endequation %}, ביחד - אלו שני הדברים שהיו חייבים להתקיים סימולטנית כדי שהאינדקס {% equation %}i{% endequation %} יתרום {% equation %}-1{% endequation %} למקדם של {% equation %}\left|y\right\rangle {% endequation %}. כשלוקחים את זה מודולו 2, מקבלים 0 אם מספר המוכפלים זוגי (ולכן המקדם הכולל יהיה 1) ו-{% equation %}1{% endequation %} אם הוא יהיה אי זוגי (ולכן המקדם הכולל יהיה {% equation %}-1{% endequation %}). הטריק הזה של להעלות את {% equation %}-1{% endequation %} בחזקה שהיא או זוגית או אי זוגית כדי לקבל אפקט של כפל ב-1 או ב-{% equation %}-1{% endequation %} הוא נפוץ ביותר בכל חלקי המתמטיקה ומשרת אותנו גם כאן.

במקרה הפרטי שראינו בהתחלה, זה שבו {% equation %}x=0^{n}{% endequation %}, פשוט מתקיים {% equation %}x\cdot y=0{% endequation %} לכל {% equation %}y{% endequation %}, ולכן המקדם יוצא תמיד חיובי ואנחנו מקבלים את הסכום הנחמד שראינו קודם: {% equation %}H^{\otimes n}\left|0^{n}\right\rangle =\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left|x\right\rangle {% endequation %}.

עכשיו אפשר לחזור סוף סוף אל דויטש-ג'וזה ולהבין מה קורה בו: כל מה שנשאר לנו הוא חשבון פשוט ביותר.

ההתחלה של דויטש-ג'וזה מאפסת מצב התחלתי {% equation %}\left|0^{n}\right\rangle {% endequation %} ואז מפעילה עליו {% equation %}H^{\otimes n}{% endequation %}, כלומר אנחנו מגיעים אל {% equation %}\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left|x\right\rangle {% endequation %}. בשלב הבא מפעילים את הקופסה השחורה על המצב הזה. נזכיר מה היא עושה:

{% equation %}U_{f}\left|x\right\rangle =\left(-1\right)^{f\left(x\right)}\left|x\right\rangle {% endequation %}

ולכן נקבל

{% equation %}U_{f}\left(\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left|x\right\rangle \right)=\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}U_{f}\left(\left|x\right\rangle \right)={% endequation %}

{% equation %}=\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)}\left|x\right\rangle {% endequation %}

עכשיו על כל זה אני מפעיל שוב {% equation %}H^{\otimes n}{% endequation %} ומקבל סכום כפול:

{% equation %}H^{\otimes n}\left(\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)}\left|x\right\rangle \right)=\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)}H^{\otimes n}\left(\left|x\right\rangle \right)={% endequation %}

{% equation %}=\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)}\frac{1}{\sqrt{2^{n}}}\sum_{y\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{x\cdot y}\left|y\right\rangle {% endequation %}

זה סכום סופי, אז קל להפוך בו את סדר הסכימה: לכל {% equation %}y\in\left\{ 0,1\right\} ^{n}{% endequation %}, לקבץ את האיברים שמתאימים למקדם {% equation %}\left|y\right\rangle {% endequation %}:

{% equation %}=\frac{1}{2^{n}}\sum_{y\in\left\{ 0,1\right\} ^{n}}\left(\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)+x\cdot y}\right)\left|y\right\rangle {% endequation %}

ה-{% equation %}\left|y\right\rangle {% endequation %} השונים הם תוצאות המדידה השונות האפשריות, והמקדם שאני מחשב ילמד אותי מה ההסתברות להעלות את {% equation %}\left|y\right\rangle {% endequation %} בגורל. האלגוריתם, כזכור, מכריע את ההכרעה שלו על פי השאלה האם {% equation %}\left|0^{n}\right\rangle {% endequation %} עלה בגורל, אז בואו נבדוק ספציפית את המקדם של {% equation %}y=0^{n}{% endequation %}:

{% equation %}\frac{1}{2^{n}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)+x\cdot y}=\frac{1}{2^{n}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)}{% endequation %}

עכשיו, אם {% equation %}f{% endequation %} היא פונקציה קבועה, כל האיברים בסכום יהיו <strong>אותו הדבר</strong> ולכן נקבל {% equation %}\frac{1}{2^{n}}\cdot\left(\pm2^{n}\right)=\pm1{% endequation %}. זה לא משנה אם המקדם חיובי או שלילי, כי כזכור - כדי לקבל את ההסתברות אנחנו לוקחים ערך מוחלט של המקדם ומעלים אותו בריבוע, ולכן בכל אחד מהמקרים הללו נקבל 1: בהסתברות של 1 בדיוק מובטח לנו שנקבל את המצב {% equation %}0^{n}{% endequation %}, כמו שאמור לקרות.

אם {% equation %}f{% endequation %} היא פונקציה מאוזנת, אז {% equation %}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)}{% endequation %} הולך לכלול את אותו מספר של {% equation %}+1{% endequation %} ושל {% equation %}-1{% endequation %}, וכולם יבטלו זה את זה, כך שאני אקבל 0. עזבו אתכם ממה שקורה עם שאר המקדמים של שאר האיברים במצב שהגעתי אליו - המקדם של {% equation %}0^{n}{% endequation %} הוא 0, ולכן אין לי סיכוי לקבל אותו. אני בודאות אקבל תוצאה אחרת ולכן האלגוריתם יענה נכון גם במקרה הזה. זה מסיים את ההוכחה שהוא עובד, וגם נותן לנו תחושה טובה מאיפה הגיעו ה"פונקציה קבועה או מאוזנת" הללו; נראה כאילו היה לנו כאן אלגוריתם שחיפש בעיה לפתור, אבל זה לא משנה את זה שהפתרון מרהיב ממש באלגנטיות המתמטית שלו.

<h2>אלגוריתם ברנשטיין-וזירני</h2>

אמרתי שדויטש-ג'וזה נשמע כמו אלגוריתם שמחפש בעיה לפתור, והיופי פה הוא שבעצם יש <strong>עוד</strong> בעיה שאפשר לפתור, בצורה כזו שלא זורקת הצידה את תוצאת המדידה אם היא שונה מ-{% equation %}0^{n}{% endequation %}. גם הבעיה הנוספת הזו עדיין מרגישה קצת מלאכותית, אבל אולי פחות? בהקשר של הבעיה הזו, אלגוריתם דויטש-ג'וזה נקרא גם <strong>אלגוריתם ברנשטיין-וזירני</strong> למרות שזה אותו אלגוריתם בדיוק; המאמר המקורי של ברנשטיין ווזריני הוא גדול ומורכב ועוסק בהגדרות של מחלקות סיבוכיות קוונטיות והפרדה שלהן ממחלקות סיבוכיות הסתברותיות ובהקשר הזה מופיע השימוש שאני מתאר כאן; זה לא שברנשטיין-וזירני ישבו ואמרו "היי, תראו, יש עוד משמעות לדויטש-ג'וזה" וישבו לכתוב על זה מאמר.

דויטש-ג'וזה עוסק בנסיון להבין פונקציה {% equation %}f:\left\{ 0,1\right\} ^{n}\to\left\{ 0,1\right\} {% endequation %} כלשהי שהיא או קבועה, או מאוזנת. ברנשטיין-וזירני עוסק בנסיון להבין פונקציה {% equation %}f:\left\{ 0,1\right\} ^{n}\to\left\{ 0,1\right\} {% endequation %} שהיא לאו דווקא קבועה או מאוזנת, אבל היא <strong>לינארית</strong>, כלומר {% equation %}f\left(x+y\right)=f\left(x\right)+f\left(y\right){% endequation %} וגם {% equation %}f\left(\lambda x\right)=\lambda f\left(x\right){% endequation %} (לא כזה מרשים כי {% equation %}\lambda\in\left\{ 0,1\right\} {% endequation %}), כשהחיבור והכפל בסקלר הם מעל {% equation %}\mathbb{Z}_{2}^{n}{% endequation %}. בואו נראה שאפשר לחשוב על הפונקציה הזו בתור מכפלה סקלרית, כלומר שקיים {% equation %}w\in\left\{ 0,1\right\} ^{n}{% endequation %} כך ש-{% equation %}f\left(x\right)=w\cdot x{% endequation %}: 

אם נגדיר {% equation %}e_{i}=\left(0,\ldots,1,\ldots,0\right){% endequation %}, כלומר ה-{% equation %}1{% endequation %} נמצא רק במקום ה-{% equation %}i{% endequation %} של {% equation %}e_{i}{% endequation %}, אז נקבל בסיס של {% equation %}\mathbb{Z}_{2}^{n}{% endequation %}: אפשר להציג כל {% equation %}x\in\mathbb{Z}_{2}^{n}{% endequation %} בתור {% equation %}x=\sum_{i=1}^{n}x_{i}e_{i}{% endequation %}. מתכונת הלינאריות של {% equation %}f{% endequation %} נקבל

{% equation %}f\left(x\right)=f\left(\sum_{i=1}^{n}x_{i}e_{i}\right)=\sum_{i=1}^{n}x_{i}f\left(e_{i}\right){% endequation %}

אז פשוט נגדיר {% equation %}w_{i}=f\left(e_{i}\right){% endequation %} ונקבל שאכן, {% equation %}f\left(x\right)=w\cdot x{% endequation %} לכל {% equation %}x\in\mathbb{Z}_{2}^{n}{% endequation %}. שימו לב שרוב הפונקציות אינן לינאריות; יש {% equation %}2^{2^{n}}{% endequation %} פונקציות מ-{% equation %}\left\{ 0,1\right\} ^{n}{% endequation %} אל {% equation %}\left\{ 0,1\right\} {% endequation %}, אבל מכיוון שיש רק {% equation %}2^{n}{% endequation %} איברים {% equation %}w\in\left\{ 0,1\right\} ^{n}{% endequation %} יש רק {% equation %}2^{n}{% endequation %} פונקציות לינאריות. מכאן שברנשטיין-וזירני מראש מטפל רק במחלקה קטנה יחסית של פונקציות, בדומה לדויטש-ג'וזה.

המשימה של ברנשטיין-וזירני היא זו: בהינתן {% equation %}f{% endequation %} לינארית שכזו, למצוא את ה-{% equation %}w{% endequation %} שמגדיר אותה. שימו לב: בניגוד לדויטש-ג'וזה, כאן אנחנו לא רוצים להכריע בין שתי סיטואציות אלא ממש למצוא משהו. אבל אותו אלגוריתם יעבוד:

<ol> <li>אתחלו מצב קוונטי אל {% equation %}\left|0^{n}\right\rangle {% endequation %}</li>


<li>הפעילו {% equation %}H{% endequation %} על כל הקיוביטים.</li>


<li>הפעילו את הקופסה השחורה על המצב שקיבלתם.</li>


<li>הפעילו {% equation %}H{% endequation %} על המצב שקיבלתם.</li>


<li>מדדו את כל הקיוביטים במצב שקיבלתם.</li>


<li>תוצאת המדידות {% equation %}w{% endequation %} היא הערך המבוקש.</li>

</ol>

לי זה נראה כמו קסם, שפתאום נקבל את ה-{% equation %}w{% endequation %} הזה, אבל האמת היא שזה די פשוט. בואו ניזכר מה מקבלים אחרי שלב 4, כי כבר ביצענו את החישוב קודם:

{% equation %}\frac{1}{2^{n}}\sum_{y\in\left\{ 0,1\right\} ^{n}}\left(\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)+x\cdot y}\right)\left|y\right\rangle {% endequation %}

עכשיו, ה-{% equation %}f\left(x\right)+x\cdot y{% endequation %} הזה שלמעלה נהיה פשוט יותר במקרה שלנו, כי {% equation %}f\left(x\right)=w\cdot x=x\cdot w{% endequation %} ולכן נקבל

{% equation %}f\left(x\right)+x\cdot y=x\cdot w+x\cdot y=x\cdot\left(w+y\right){% endequation %}

עכשיו, במקרה שבו {% equation %}w=y{% endequation %} אנחנו מקבלים {% equation %}w+y=2y=0{% endequation %} (כי זכרו, אנחנו מעל {% equation %}\mathbb{Z}_{2}{% endequation %}) ולכן המקדם של {% equation %}\left|y\right\rangle =\left|w\right\rangle {% endequation %} יהיה

{% equation %}\frac{1}{2^{n}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)+x\cdot y}=\frac{1}{2^{n}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{0}=\frac{1}{2^{n}}\sum_{x\in\left\{ 0,1\right\} ^{n}}1=1{% endequation %}

קסם!

בשלב הזה אני כבר ממש מוטרד. זה מרגיש כמו "קסם" במובן של אחיזת עיניים של קוסם, שגורם לנו כל הזמן להתמקד במקום אחד - במקרה זה, במקדם של ה-{% equation %}\left|y\right\rangle {% endequation %} הספציפי שמעניין אותנו, ובגלל שהוא יוצא 1 אנחנו אמורים איכשהו להיות מרוצים ולהניח שכל שאר המקדמים יוצאים 0. אבל למה? ובכן, זה די קל: בואו ניקח {% equation %}y\ne w{% endequation %}, אז זה אומר ש-{% equation %}y+w\ne0{% endequation %} לפחות באינדקס אחד. נניח בלי הגבלת הכלליות שזה האינדקס הראשון, אז אפשר לכתוב {% equation %}y+w=1z^{\prime}{% endequation %} כאשר {% equation %}z^{\prime}\in\left\{ 0,1\right\} ^{n-1}{% endequation %}.

עכשיו, אנחנו מסתכלים על הסכום {% equation %}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)+x\cdot y}{% endequation %}, שאחרי הפישוטים שלנו יוצא {% equation %}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{x\cdot1z^{\prime}}{% endequation %}. אני הולך לחלק את ה-{% equation %}x{% endequation %}-ים לשתי קבוצות: אלו שמתחילים ב-0 ואלו שמתחילים ב-1. מן הסתם שתי הקבוצות הללו מאותו גודל, אבל שימו לב לכך שאם {% equation %}x=0x^{\prime}{% endequation %} אז {% equation %}x\cdot1z^{\prime}=x^{\prime}\cdot z^{\prime}{% endequation %} ואילו אם {% equation %}x=1x^{\prime}{% endequation %} אז {% equation %}x\cdot1z^{\prime}=1+x^{\prime}\cdot z^{\prime}{% endequation %}. במילים אחרות, הזוג {% equation %}0x^{\prime},1x^{\prime}{% endequation %} יניב תוצאות שונות כשמעלים את {% equation %}-1{% endequation %} בחזקת {% equation %}x\cdot1z^{\prime}{% endequation %}, ולכן הסכום של שניהם יצא 0. בצורה הזו חילקנו את <strong>כל</strong> ה-{% equation %}x{% endequation %}-ים שלנו לזוגות שמבטלים זה את זה, ולכן באמת נקבל 0. אני מקווה שזה משכנע גם את מי שכמוני קשה לו לקבל את זה שאם המקדם של איבר אחד יצא 1 זה אומר ששאר המקדמים הם בהכרח 0.

<h2>מה למדנו מכל זה?</h2>

כאמור, אני לא מביא את האלגוריתמים הללו בשביל להוכיח את עליונות החישוב הקוונטי על החישוב הרגיל, והטיעון המתמטי המדויק שרלוונטי לנסח בהקשר הזה הוא ארוך ומסובך למדי ואין לי כוח אליו. אני מביא אותם כדי שנרגיש מה הולך באלגוריתמים קוונטיים. באופן מאוד גס אוהבים לומר שהכוח של אלגוריתם קוונטי נובע משלושה היבטים של חישוב קוונטי:

<ul> <li>סופרפוזיציה</li>


<li>שזירה</li>


<li>התאבכות</li>

</ul>

בדויטש-ג'וזה-ברנשטיין-וזירני אין ממש שזירה (ה-{% equation %}H{% endequation %}-ים בהתחלה ובסוף לא יוצרים שזירה, וגם ה-{% equation %}U{% endequation %} באמצע לא חייבת ליצור שזירה). בהחלט יש סופרפוזיציה - זה מה שה-{% equation %}H{% endequation %} בהתחלה עושה לנו מייד. אבל האספקט המעניין שטרם ראינו הוא שיש כאן <strong>התאבכות</strong>.

בפיזיקה, במשמעות המקורית של המילהת "התאבכות" באה לתאר סיטואציה שבה גלים שונים ש"מתנגשים" יכולים לחזק או להחליש זה את זה בנקודות ההתנגשות, בהתאם למצב הנוכחי שלהם. אפשר לחשוב על גל בתור משהו שכל הזמן עולה ויורד. אם בנקודת ההתנגשות של שני גלים, שנים בנקודה הגבוהה ביותר שלהם, הם יחזקו זה את זה ונקבל גל עוד יותר גבוה ("התאבכות בונה") ואם הם ייפגשו בנקודה הנמוכה ביותר שלהם התוצאה תהיה עוד יותר נמוכה וגם זו תהיה התאבכות בונה. אבל אם גל אחד יהיה גבוה והשני נמוך, הם יבטלו זה את זה ונקבל איזור שבו לא רואים שום דבר ("התאבכות הורסת"). מה שיפה בדויטש-ג'וזה הוא שזה בדיוק מה שקורה גם כאן.

כשביצענו את הסופרפוזיציה הראשונית עם {% equation %}H^{\otimes n}{% endequation %}, אפשר לחשוב על כך כאילו לקחנו את המצב {% equation %}\left|0^{n}\right\rangle {% endequation %} ופירקנו אותו לסכום של {% equation %}2^{n}{% endequation %} גלים שונים: {% equation %}\frac{1}{\sqrt{2^{n}}}\sum_{x\in\left\{ 0,1\right\} ^{n}}\left|x\right\rangle {% endequation %}. ברגע הזה, כל הגלים נמצאים באיזור ה"גבוה" שלהם, שבא לידי ביטוי בפאזה החיובית שלהם (הפאזה בהקשר הנוכחי היא הסימן של המקדם של {% equation %}\left|x\right\rangle {% endequation %}).

אחר כך אנחנו מפעילים את {% equation %}U_{f}{% endequation %}, וההשפעה שלו היא פשוטה: הוא משנה את הפאזה של {% equation %}\left|x\right\rangle {% endequation %}-ים מסויימים, מחיובית לשלילית. במקום שכל הגלים יהיו מסונכרנים, {% equation %}U_{f}{% endequation %} פיצל את הגלים לשתי קבוצות, כל אחת עם הסינכרון שלה. לבסוף מגיע ה-{% equation %}H^{\otimes n}{% endequation %} השני, ומה שהוא עושה הוא לגרום לכל הגלים להתנגש ולהסתכל מה קרה. כשהגלים "מתנגשים", לכל {% equation %}\left|y\right\rangle {% endequation %} אנחנו מקבלים בנקודת ההתנגשות את

{% equation %}\frac{1}{\sqrt{2^{n}}}\left(\sum_{x\in\left\{ 0,1\right\} ^{n}}\left(-1\right)^{f\left(x\right)+x\cdot y}\right)\left|y\right\rangle {% endequation %}

בברנשטיין-וזירני, עבור רוב ערכי ה-{% equation %}\left|y\right\rangle {% endequation %}, ההתאבכות תהיה הורסת והם ייעלמו לגמרי. המקום היחיד שבו תהיה התאבכות בונה הוא ה-{% equation %}\left|y\right\rangle {% endequation %} שאנו חפצים ביקרו. בדויטש-ג'וזה תהיה התאבכות בונה ב-{% equation %}\left|0^{n}\right\rangle {% endequation %} רק אם הפונקציה קבועה, ואחרת תהיה שם התאבכות הורסת.

זו בעצם המהות של רבים מהאלגוריתמים הקוונטיים: לגרום איכשהו לחלקים השונים של הסופרפוזיציה "להתנגש" אלו באלו, כך שהחלקים הלא מועילים מתבטלים, והחלקים המועילים נשארים. בדויטש-ג'וזה, בגלל הפשטות הגדולה שלו, אנחנו יכולים לראות בדיוק מה גורם להתאבכויות הללו לעבוד - העובדה שהמקדמים של ה-{% equation %}\left|x\right\rangle {% endequation %}-ים יכולים להיות <strong>שליליים</strong>. וכאן אנחנו מגיעים אל מה שהוא אולי לב-לבו של ההבדל המרכזי בין חישוב קוונטי וחישוב הסתברותי "רגיל". ריצ'ארד פיינמן, בהרצאה מפורסמת שלו, Simulating Physics with Computers, אמר (כחלק מתיאור יותר מפורט, כמובן)


<blockquote dir="ltr" style="text-align:left">
  <p>The only difference between a probabilistic classical world and the equations of the quantum world is that somehow or other it appears as if the probabilities would have to go negative.</p>
</blockquote>


וזה בדיוק מה שקורה פה. אם אני מבצע חישוב הסתברותי "רגיל" שבו אני מגריל מחרוזת {% equation %}x\in\left\{ 0,1\right\} ^{n}{% endequation %} בהתפלגות אחידה, אפשר יהיה לחשוב על מצב החישוב שלי אחרי השלב הראשון הזה כאילו הוא ב"סופרפוזיציה" שבו ההסתברות של כל {% equation %}x{% endequation %} היא בדיוק {% equation %}\frac{1}{2^{n}}{% endequation %}. אחר כך אני יכול לבצע חישובים שעבור {% equation %}x{% endequation %}-ים שונים יובילו לאותה תוצאה, ובכך "לחזק" את ההסתברות של אותה תוצאה להתקבל. אבל האופן שבו ה"חיזוק" הזה מתבצע הוא על ידי חיבור הסתברויות, אין לי חיסור. אם לחדד: אפשר לתאר חישוב הסתברותי רגיל בתור כפל של וקטור <strong>סטוכסטי</strong> (וקטור שבו כל הכניסות בין 0 ל-1 ומסתכמות ל-1) במטריצה <strong>סטוכסטית</strong> (מטריצה שבה כל הכניסות בין 0 ל-1 וכל שורה מסתכמת ל-1). זה נותן הרבה, אבל זה פשוט לא מאפשר לנו לבצע את אותה אלגברה שאנחנו עושים בחישוב קוונטי, עם מטריצות שיש בהן גם מספרים שליליים.

עוד דרך לחשוב על זה: בחישוב הסתברותי, מה שיש לנו ביד בכל רגע נתון הוא ההסתברויות של התוצאות האפשריות. בחישוב קוונטי, מה שיש לנו ביד בכל רגע נתון הוא <strong>האמפליטודות</strong> של החישוב - אותן {% equation %}\alpha_{x}{% endequation %}-ים. ה-{% equation %}\alpha_{x}{% endequation %}-ים הן <strong>לא</strong> הסתברויות; הן מספרים שיכולים להיות גם שליליים וגם מרוכבים, ואת ההסתברויות אנחנו מחשבים מתוכן בעזרת שלב הביניים {% equation %}\left|\alpha_{x}\right|^{2}{% endequation %}. כלומר, אנחנו מסוגלים לבצע אלגברה יותר מתוחכמת, ש"מוסתרת" בסופו של דבר בידי המעבר מ-{% equation %}\alpha_{x}{% endequation %} אל {% equation %}\left|\alpha_{x}\right|^{2}{% endequation %}. אבל כל עוד לא מדדנו, אנחנו עדיין בעולם של האלגברה המתוחכמת יותר, והיא זו שמאפשרת לנו להשיג את האפקט של ההתאבכות. חישוב קוונטי מאפשר לנו לרתום את הטבע עצמו כדי לבצע אלגברה שהיא יותר מתוחכמת מאלגברה בוליאנית.

זהו, זו הדרך הכי טובה שיש לי לתת את האינטואיציה האישית שלי לסיבה שבגללה חישוב קוונטי הוא "יותר" מחישוב רגיל. עכשיו רק נשאר לי לסגור את החוב מתחילת הפוסט לגבי הקופסאות השחורות.

<h2>אז איך מממשים קופסא שחורה קוונטית?</h2>

בתחילת הפוסט מלמלתי משהו על חישוב של {% equation %}f{% endequation %} בעזרת קופסא שחורה ואז קפצתי לכך שיש לנו אופרטור {% equation %}U_{f}{% endequation %} שעושה את הקסם {% equation %}U_{f}\left|x\right\rangle =\left(-1\right)^{f\left(x\right)}\left|x\right\rangle {% endequation %}. אני עדיין צריך להסביר איך כזה דבר עובד.

אם תחשבו על זה רגע, עדיין בסדרת הפוסטים לא הסברתי איך מבצעים חישוב <strong>רגיל</strong> בעזרת מחשב קוונטי. אמנם, אמרתי ש-{% equation %}X{% endequation %} זה כמו NOT, אבל אין לי שום פעולה שהיא כמו AND, למשל: פעולה שמחזירה 1 רק אם שני הקלטים היו 1, ואחרת מחזירה 0. ויש סיבה טובה שבגללה אין לי כזו: כי AND היא פעולה <strong>לא הפיכה</strong> אבל בחישוב קוונטי כל פעולה צריכה להיות אופרטור אוניטרי, כלומר הפיכה. אם ב-AND קיבלתי 0, אני לא יודע אם זה בגלל ששני הקלטים היו 0, או בגלל שאחד מהם היה 0 והשני 1, ואיזה מהם. אינפורמציה הלכה לאיבוד.

האם זה אומר שלא ניתן לממש פעולת AND בחישוב קוונטי? לא בדיוק. אפשר, אבל צריך יהיה לשלם מחיר כלשהו. המחיר הוא שימוש בקיוביט "זבל" שישתתף בחישוב בתור מעין משתתף זמני ואחר כך נוכל לשכוח מערכו. אני לא אכנס לפרטים הללו עכשיו אלא אציג פוסט יותר מפורט עליהם בהמשך. למה לא הראיתי את זה קודם? כי זו אחת מהבעיות הללו שכל עוד לא מרגישים שחסר לה פתרון, קצת טרחני להציג אותו.

אז נניח שיש לנו מעגל קוונטי שיודע גם לבצע חישוב רגיל. יש לו {% equation %}n{% endequation %} קיוביטי קלט, וקיוביט נוסף שאנו מניחים שמאותחל ל-{% equation %}\left|0\right\rangle {% endequation %} ובסוף החישוב יהיה בו הפלט, ואולי גם קיוביט עזר שלא נטרח לכתוב. כלומר, מה שיש לנו הוא מעגל שמחשב

{% equation %}O_{f}\left(\left|x\right\rangle \otimes\left|0\right\rangle \right)=\left|x\right\rangle \otimes\left|f\left(x\right)\right\rangle {% endequation %}

שימו לב: כאן במכפלה הטנזורית, הרכיב השמאלי, {% equation %}\left|x\right\rangle {% endequation %}, הוא בעצמו מכפלה טנזורית של {% equation %}n{% endequation %} קיוביטים, בעוד שהרכיב הימני הוא קיוביט בודד.

הבעיה עם ההגדרה שנתתי כרגע היא שזו עדיין לא הגדרה שלמה. הגדרתי את {% equation %}O_{f}{% endequation %} <strong>לחלק </strong>מהקלטים שהם אברי בסיס, אבל לא לכולם. מה עם הקלטים מהצורה {% equation %}\left|x\right\rangle \otimes\left|1\right\rangle {% endequation %}? כדי לטפל בכל המקרים, אני אגדיר

{% equation %}O_{f}\left(\left|x\right\rangle \otimes\left|b\right\rangle \right)=\left|x\right\rangle \otimes\left|f\left(x\right)\oplus b\right\rangle {% endequation %}

כאן {% equation %}\oplus{% endequation %} מציין חיבור מודולו 2, ולכן מה ש-{% equation %}O_{f}{% endequation %} עושה הוא או להחזיר את {% equation %}f\left(x\right){% endequation %} (אם הקלט הנוסף הוא 0) או את {% equation %}\neg f\left(x\right){% endequation %} (אם הקלט הנוסף הוא 1). מה שאני רוצה להסביר עכשיו הוא איך לבנות את {% equation %}U_{f}{% endequation %} שבו השתמשתי קודם מתוך {% equation %}O_{f}{% endequation %} הזה. הטריק הוא חמוד ממש: במקום להפעיל את {% equation %}O_{f}{% endequation %} על {% equation %}\left|x\right\rangle \otimes\left|0\right\rangle {% endequation %} או על {% equation %}\left|x\right\rangle \otimes\left|1\right\rangle {% endequation %}, אני אפעיל אותו על {% equation %}\left|x\right\rangle \otimes\left|-\right\rangle {% endequation %}.

כזכור, {% equation %}\left|-\right\rangle {% endequation %} הוא המצב הקוונטי שמתקבל מ-{% equation %}H\left|1\right\rangle {% endequation %}, כלומר {% equation %}\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}{% endequation %}. בואו נראה מה {% equation %}O_{f}{% endequation %} עושה כשהוא מקבל קלט כזה, תוך התבססות על הלינאריות שלו:

{% equation %}O_{f}\left(\left|x\right\rangle \otimes\left|-\right\rangle \right)=\frac{1}{\sqrt{2}}\left[O_{f}\left(\left|x\right\rangle \otimes\left|0\right\rangle \right)-O_{f}\left(\left|x\right\rangle \otimes\left|1\right\rangle \right)\right]={% endequation %}

{% equation %}=\frac{1}{\sqrt{2}}\left[\left|x\right\rangle \left|f\left(x\right)\right\rangle -\left|x\right\rangle \left|f\left(x\right)\oplus1\right\rangle \right]={% endequation %}

{% equation %}=\left|x\right\rangle \frac{\left|f\left(x\right)\right\rangle -\left|f\left(x\right)\oplus1\right\rangle }{\sqrt{2}}{% endequation %}

עכשיו, בואו נבדיל בין שני המקרים האפשריים:

<ul> <li>אם {% equation %}f\left(x\right)=0{% endequation %} אז מה שקיבלנו מימין ל-{% equation %}\left|x\right\rangle {% endequation %} הוא את {% equation %}\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}=\left|-\right\rangle {% endequation %}</li>


<li>אם {% equation %}f\left(x\right)=1{% endequation %} אז מה שקיבלנו מימין ל-{% equation %}\left|x\right\rangle {% endequation %} הוא את {% equation %}\frac{\left|1\right\rangle -\left|0\right\rangle }{\sqrt{2}}=-\left|-\right\rangle {% endequation %}</li>

</ul>

ובמילים אחרות, קיבלנו ש-

{% equation %}O_{f}\left(\left|x\right\rangle \left|-\right\rangle \right)=\left(-1\right)^{f\left(x\right)}\left|x\right\rangle \left|-\right\rangle {% endequation %}

קיבלנו שהפעלה של {% equation %}O_{f}{% endequation %} לא משנה את המצב הקוונטי כלל, חוץ מאשר על ידי כפל שלו ב-{% equation %}\left(-1\right)^{f\left(x\right)}{% endequation %}. לכן, אם נסתכל על האפקט רק ל-{% equation %}n{% endequation %} הקיוביטים הראשונים, נקבל בדיוק את {% equation %}U_{f}{% endequation %} שרצינו. זה מסיים גם את ההסבר שלי לגבי הופעת הקופסה השחורה המסתורת {% equation %}U_{f}{% endequation %}, אבל עדיין נשאר לי חוב של להסביר איך בכלל מבצעים חישובים רגילים בעזרת חישוב קוונטי. אל זה נגיע בעתיד. אסיים עם האיור שנותן לנו את כל דויטש-ג'וזה בעזרת {% equation %}O_{f}{% endequation %} הזה, שכן גם באיור הזה אפשר להיתקל לפעמים ושווה לראות אותו, עכשיו כשאנחנו מבינים שזה אותו הדבר:

<img src="{{site.baseurl}}{{site.post_images}}/2022/deutsch_jozsa_full.png" alt=""/> 
