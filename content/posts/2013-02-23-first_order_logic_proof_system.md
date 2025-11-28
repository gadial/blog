---
id: 2357
title: "מערכת הוכחה ללוגיקה מסדר ראשון"
date: 2013-02-23 16:54:04
layout: post
categories: 
  - לוגיקה
tags: 
  - לוגיקה מסדר ראשון
  - לוגיקה מתמטית
  - מערכות הוכחה
---
סדרת הפוסטים שלי על לוגיקה הגיעה עד לתיאור של הסינטקס והסמנטיקה של <a href="http://www.gadial.net/2012/06/17/first_order_logic/">לוגיקה מסדר ראשון</a> ושם עצרתי, כי השלב הבא, שעליו אני רוצה לדבר עכשיו, הוא לא פשוט. בתחשיב הפסוקים, שהצגתי בתור "חימום" ללוגיקה מסדר ראשון, היעד שלנו היה הצגת <strong>מערכת הוכחה: </strong>אוסף של אקסיומות וכללי גזירה שמאפשרים, בהינתן קבוצת פסוקים כלשהי ("הנחות"), לגזור את כל המסקנות הסמנטיות מאותה קבוצת פסוקים באופן סינטקטי לגמרי: לכל מסקנה שכזו תהיה הוכחה, שהיא בסך הכל סדרה סופית של פסוקים שכל אחד מהם הוא אקסיומה, הנחה או נובעת מפסוקים קודמים על ידי כללי הגזירה. אחרי ש<a href="http://www.gadial.net/2012/04/04/propositional_caclulus_proofs/">הצגתי</a> את מערכת ההוכחה <a href="http://www.gadial.net/2012/04/08/propositional_calculus_completeness/">הראיתי</a> שהיא <strong>נאותה</strong> ו<strong>שלמה</strong>, כאשר נאותות פירושה היה "כל מה שיכיח, נכון" ואילו שלמות הייתה "כל מה שנכון, יכיח". ההוכחה של משפט השלמות הייתה מורכבת יחסית; בלוגיקה מסדר ראשון יש לנו רמת סיבוך נוספת.

נתחיל עם הצגה של מערכת ההוכחה שלי עבור לוגיקה מסדר ראשון. כדאי להעיר שאין קונצנזוס בנקודה הזו: יש מערכות הוכחה רבות ושונות בספרות, למרות שבשורה התחתונה ההוכחות של משפט השלמות והנאותות שלהן דומות באופיין. אני בוחר להציג כאן את זו שבעיני אישית היא הפשוטה ביותר. אני מניח שהקוראים זוכרים בערך איך מוגדרים הסינטקס והסמנטיקה של לוגיקה מסדר ראשון, כמו גם מה בערך הולך במערכת ההוכחה של תחשיב הפסוקים; לא אחזור על זה שוב כאן.

מכיוון שלוגיקה מסדר ראשון היא מעין הכללה של תחשיב הפסוקים, די ברור שמערכת ההוכחה שלנו תהיה הכללה של זו של תחשיב הפסוקים. כזכור, במערכת ההוכחה הזו השתמשתי בשלוש "תבניות אקסיומה":
<ol>
	<li>{% equation %}\alpha\to\left(\beta\to\alpha\right){% endequation %}</li>
	<li>{% equation %}\left[\alpha\to\left(\gamma\to\beta\right)\right]\to\left[\left(\alpha\to\gamma\right)\to\left(\alpha\to\beta\right)\right]{% endequation %}</li>
	<li>{% equation %}\left(\neg\alpha\to\neg\beta\right)\to\left(\beta\to\alpha\right){% endequation %}</li>
</ol>
אלו "תבניות" כי במקום {% equation %}\alpha,\beta,\gamma{% endequation %} אפשר להציב פסוקים כלשהם. באותו האופן התבניות הללו יהיו שייכות גם למערכת ההוכחה של לוגיקה מסדר ראשון, כאשר במקום {% equation %}\alpha,\beta,\gamma{% endequation %} מציבים נוסחאות כלשהן בלוגיקה מסדר ראשון. תבנית כזו היא בעלת התכונה הסמנטית שלא חשוב מה נציב בה - בכל מבנה ובכל השמה, הפסוק שמתקבל מההצבות הללו יהיה בעל ערך אמת, ואפילו אם הנוסחאות שמציבים הן מורכבות וכללות כמתים ופונקציות ואקשן. הסיבה פשוטה: אם מחשבים את ערך האמת של הפסוק שמתקבל מההשמות, בסופו של דבר נקבל שכל מה שהצבנו במקום {% equation %}\alpha{% endequation %} מתורגם לאחד משניים: או {% equation %}\mbox{T}{% endequation %} או {% equation %}\mbox{F}{% endequation %}, וכך גם עבור {% equation %}\beta,\gamma{% endequation %}, מה שאומר שלא משנה איזו נוסחה מורכבת אפשר להציב במקום {% equation %}\alpha,\beta,\gamma{% endequation %}, עדיין תחת מבנה והשמה נתונים הם מתנהגים כמו משתנים בתחשיב הפסוקים, ולכן תבנית אקסיומה שהייתה טאוטולוגיה בתחשיב הפסוקים נותרת כזו גם כעת.

כלל ההיסק שלנו בתחשיב הפסוקים היה מודוס פוננס, {% equation %}\mbox{MP}{% endequation %}, שמתוך {% equation %}\alpha{% endequation %} ו-{% equation %}\alpha\to\beta{% endequation %} גזר את {% equation %}\beta{% endequation %}. נשתמש בו גם כעת. כפי שראינו, זה מספיק כדי לגזור כל טאוטולוגיה בתחשיב הפסוקים. הבעיה היא שבלוגיקה מסדר ראשון יש עוד דברים. מן הסתם יהיו אלה דברים שקשורים לכמתי ה"קיים" ו"לכל" שאין משהו דומה להם בתחשיב הפסוקים. בואו ניתן דוגמה:

{% equation %}\forall x\left(R\left(x\right)\right)\to R\left(y\right){% endequation %}

זו נוסחה שמשתמשת בסימן יחס חד-מקומי {% equation %}R{% endequation %}, ויש בה משתנה קשור אחד {% equation %}x{% endequation %} ומשתנה חופשי אחד {% equation %}y{% endequation %}. בכל מבנה {% equation %}\mathcal{M}{% endequation %} ערך האמת של הרישא של הפסוק - {% equation %}\forall x\left(R\left(x\right)\right){% endequation %} - נקבע באופן יחיד, והוא יהיה {% equation %}\mbox{T}{% endequation %} אם ורק אם {% equation %}R^{\mathcal{M}}=D^{\mathcal{M}}{% endequation %}, כלומר אם היחס {% equation %}R{% endequation %} מתפרש ב-{% equation %}\mathcal{M}{% endequation %} בתור "כל העולם". כעת, אם הערך של {% equation %}\forall x\left(R\left(x\right)\right){% endequation %} הוא {% equation %}\mbox{F}{% endequation %} אז הנוסחה כולה היא תמיד בעל ערך אמת {% equation %}\mbox{T}{% endequation %}; ואילו אם ערך האמת שלו הוא {% equation %}\mbox{T}{% endequation %} אז {% equation %}R^{\mathcal{M}}=D^{\mathcal{M}}{% endequation %} ולכן לכל השמה אפשרית, לא משנה איזה ערך היא נותנת ל-{% equation %}y{% endequation %}, יתקיים ש-{% equation %}R\left(y\right){% endequation %} הוא {% equation %}\mbox{T}{% endequation %} ולכן שוב הנוסחה כולה תהיה {% equation %}\mbox{T}{% endequation %}. במילים אחרות, הנוסחה {% equation %}\forall x\left(R\left(x\right)\right)\to R\left(y\right){% endequation %}היא בעלת ערך האמת {% equation %}\mbox{T}{% endequation %} בכל מבנה ובכל השמה אפשריים. לנוסחה בעלת התכונה הזו אני קורא <strong>אמת לוגית</strong>, ובכוונה אני לא קורא לה "טאוטולוגיה" כמו בתחשיב הפסוקים. במילה "טאוטולוגיה" בלוגיקה מסדר ראשון אני משתמש כדי לתאר את מה שמתקבל מלקיחת טאוטולוגיה בתחשיב הפסוקים ואז הצבת נוסחאות בתור המשתנים, ואילו {% equation %}\forall x\left(R\left(x\right)\right)\to R\left(y\right){% endequation %} בבירור לא יכול להתקבל בצורה הזו. הדרך היחידה שבה הוא יכול להתקבל היא על ידי הצבה בפסוק {% equation %}X\to Y{% endequation %}, אבל הפסוק הזה כלל אינו טאוטולוגיה.

זה מראה לנו שהסיבות לכך ש-{% equation %}\forall x\left(R\left(x\right)\right)\to R\left(y\right){% endequation %} היא אמת לוגית הן עמוקות יותר מאשר הסיבות לכך שנוסחה כמו {% equation %}\forall x\left(R\left(x\right)\right)\to\left(R\left(y\right)\to\forall x\left(R\left(x\right)\right)\right){% endequation %} היא אמת לוגית; השניה מתקבלת מהצבה בפסוק {% equation %}X\to\left(Y\to X\right){% endequation %} שהוא כן טאוטולוגיה של תחשיב הפסוקים, ולכן ערך האמת שלה נובע במובן מסויים רק מתכונות ה<strong>קשרים</strong> ({% equation %}\to{% endequation %} במקרה הזה), בעוד שערך האמת הלוגית של {% equation %}\forall x\left(R\left(x\right)\right)\to R\left(y\right){% endequation %} נובע גם מתכונות ה<strong>כמתים</strong> (שימו לב: אם נחליף את {% equation %}\forall{% endequation %} ב-{% equation %}\exists{% endequation %} נקבל משהו שאינו אמת לוגית). אני מקווה שזה עוזר להבין למה מה שעשינו בתחשיב הפסוקים רחוק מלהיות מספיק גם בתחשיב היחסים.

הנוסחה שלעיל מרמזת על סוג חדש של תבנית אקסיומה שנזדקק לו. אבל איך אפשר לפרמל אותה? בואו נראה עוד כמה דוגמאות לפני שנציג את המקרה הכללי. ראשית, הביטו בנוסחה הזו:

{% equation %}\forall x\left(\exists y\left(x+y&gt;c\right)\right)\to \left(\exists y\left(z+y&gt;c\right)\right){% endequation %}

כאן המשתנים {% equation %}x,y{% endequation %} הם קשורים ואילו {% equation %}z{% endequation %} הוא המשתנה החופשי; {% equation %}c{% endequation %} הוא סימן קבוע, {% equation %}+{% endequation %}הוא סימן פונקציה ו-{% equation %}&gt;{% endequation %} הוא סימן יחס. לא קשה לראות שגם הנוסחה הזו היא אמת לוגית. מה הדמיון בינה ובין הנוסחה הקודמת שהצגתי? בשתיהן יש "לכל {% equation %}x{% endequation %} <strong>משהו </strong>עבור<strong> {% equation %}x{% endequation %}</strong> גורר <strong>משהו</strong> עבור {% equation %}y{% endequation %}". שם ה"משהו" היה {% equation %}R\left(x\right){% endequation %} וכאן ה"משהו" הוא {% equation %}\exists y\left(x+y&gt;c\right){% endequation %} . באופן כללי "משהו" כזה יכול להיות כל נוסחה, אפילו נוסחאות שבהן {% equation %}x{% endequation %} בכלל לא מופיע. אז לכאורה הצורה של האקסיומה צריכה להיות {% equation %}\forall x\varphi\to\varphi{% endequation %}, אבל הצורה הזו <strong>לא כללית מספיק</strong>. היא מסוגלת ליצור משהו כמו {% equation %}\forall x\left(R\left(x\right)\right)\to R\left(x\right){% endequation %}, אבל הוא לא מסוגלת ליצור משהו כמו {% equation %}\forall x\left(R\left(x\right)\right)\to R\left(y\right){% endequation %}.

אם כן, אולי אפשר לומר שהצורה של האקסיומה תהיה {% equation %}\forall x\varphi\to\psi{% endequation %}, כאשר {% equation %}\psi{% endequation %} מתקבל מ-{% equation %}\varphi{% endequation %} על ידי <strong>שינוי השם</strong> של המשתנה {% equation %}x{% endequation %}. זה כבר יותר בכיוון, אבל הנה נוסחה שהיא אמת לוגית ולא יכולה להתקבל כך:

{% equation %}\forall x\left(x\ge0\right)\to\left(1\ge0\right){% endequation %}

כאן {% equation %}0,1{% endequation %} הם סימני קבועים של השפה ו-{% equation %}\ge{% endequation %} הוא סימן יחס. כאן כבר לא סתם שינינו את השם של {% equation %}x{% endequation %} אלא ממש החלפנו אותו בקבוע. ואפשר היה לעשות גם משהו כזה:

{% equation %}\forall x\left(x\ge0\right)\to\left(\left(1+z\right)^{2}\ge0\right){% endequation %}

כאשר כאן העלאה בריבוע היא סימן פונקציה, וגם חיבור הוא סימן פונקציה. מה שקרה הוא שהחלפנו את {% equation %}x{% endequation %} ב<strong>שם עצם</strong>: {% equation %}\left(1+z\right)^{2}{% endequation %}. אם כן, אפשר לומר שהצורה של האקסיומה תהיה {% equation %}\forall x\varphi\to\psi{% endequation %} כאשר {% equation %}\psi{% endequation %} מתקבל מ-{% equation %}\varphi{% endequation %} על ידי החלפת כל מופע של {% equation %}x{% endequation %} בשם עצם ספציפי כלשהו {% equation %}t{% endequation %}. זה בהחלט בכיוון, אבל זה כבר <strong>כללי יותר מדי</strong>. אם נעשה את זה, אנחנו עלולים לקבל נוסחאות שאינן אמיתות לוגיות. הנה דוגמה. ניקח את {% equation %}\varphi{% endequation %} להיות {% equation %}\exists y\left(y&gt;x\right){% endequation %} ואת {% equation %}t{% endequation %} להיות {% equation %}y{% endequation %} ונקבל:

{% equation %}\forall x\left(\exists y\left(y&gt;x\right)\right)\to\exists y\left(y&gt;y\right){% endequation %}

וזה בבירור לא פסוק שהוא אמת לוגית, כי קחו בתור מודל את המספרים הטבעיים - לכל מספר טבעי {% equation %}x{% endequation %} קיים מספר גדול ממנו {% equation %}y{% endequation %}, אבל אין אף מספר טבעי שגדול מעצמו. מה השתבש? הבעיה היא שאנחנו משתמשים ב-{% equation %}y{% endequation %} בתפקיד כפול: בתוך {% equation %}\varphi{% endequation %} הוא משתנה <strong>מכומת</strong>, בעוד ש-{% equation %}x{% endequation %} הוא משתנה <strong>חופשי</strong> בתוך {% equation %}\varphi{% endequation %}. בכך שאנחנו מציבים את {% equation %}y{% endequation %} במקום {% equation %}x{% endequation %} אנחנו הופכים משהו שלפני שניה היה חופשי (ולכן לא מושפע מהכמת {% equation %}\exists y{% endequation %}) למשהו קשור (שכן מושפע מהכמת הזה). זה סוג שינוי שאנחנו חייבים למנוע. זה מוביל אותנו להגדרה שהיא קצת קשה לעיכול אם לא רואים לה קודם מוטיבציה: שם עצם {% equation %}t{% endequation %} הוא <strong>חופשי להצבה</strong> במקום {% equation %}x{% endequation %} בפסוק {% equation %}\varphi{% endequation %} אם {% equation %}t{% endequation %} לא מכיל אף משתנה {% equation %}y{% endequation %} כך שיש מופע חופשי של {% equation %}x{% endequation %} ב-{% equation %}\varphi{% endequation %} שנופל תחת כמת עבור {% equation %}y{% endequation %}. זו הגדרה מסובכת מבחינה מילולית, אבל העיקרון ברור - אנחנו לא רוצים להחליף את {% equation %}x{% endequation %} במשהו, ואז לגלות שבתוך המשהו היה משתנה שפתאום הופך להיות מכומת.

עוד נקודה שצריך לשים לב אליה היא ש-{% equation %}\varphi{% endequation %} עשוי להכיל גם מופעים לא חופשיים של {% equation %}x{% endequation %}, ובהם אסור להציב. זה מקרה קצה מוזר למדי אבל עדיין יש להתחשב בו. הנה דוגמה: ניקח בתור {% equation %}\varphi{% endequation %} את {% equation %}\exists x\left(x&gt;0\right){% endequation %} ובתור {% equation %}t{% endequation %} את הקבוע {% equation %}0{% endequation %}, ונקבל:

{% equation %}\forall x\left(\exists x\left(x&gt;0\right)\right)\to\left(\exists x\left(0&gt;0\right)\right){% endequation %}

שהוא כמובן לא נכון. הבעיה כאן היא הפוכה ביחס לבעיה הקודמת: קודם הפכנו מישהו לא מכומת למכומת, ואילו כאן אנחנו משתמשים בהצבה לתוך {% equation %}x{% endequation %} כדי "להימלט" מהכמת {% equation %}\exists x{% endequation %}. הפתרון הוא פשוט למדי: לא מציבים את {% equation %}t{% endequation %} בתוך מופעים מכומתים של {% equation %}x{% endequation %} ב-{% equation %}\varphi{% endequation %} אלא רק במופעים החופשיים שלו.

עכשיו אפשר סוף סוף לנסח את תבנית האקסיומה במפורש. התבנית היא:
<ol start="4">
	<li>{% equation %}\forall x\varphi\to\psi{% endequation %}</li>
</ol>
כאשר {% equation %}\psi{% endequation %} מתקבל מ-{% equation %}\varphi{% endequation %} על ידי הצבה בכל מופע חופשי של {% equation %}x{% endequation %} ב-{% equation %}\varphi{% endequation %} שם עצם {% equation %}t{% endequation %} כלשהו שהוא חופשי להצבה במקום {% equation %}x{% endequation %} ב-{% equation %}\varphi{% endequation %}.

צריך כמובן להוכיח שכל נוסחה כזו היא אכן אמת לוגית, מה שניתן לעשות באופן ישיר למדי הישר מהגדרות הסמנטיקה של לוגיקה מסדר ראשון ואוותר על כך כאן (ההוכחה דומה למה שעשיתי לעיל עבור {% equation %}\varphi=R\left(x\right){% endequation %}).

בואו נעבור להתבונן על נוסחה אחרת שעדיין אין לנו יכולת להוכיח במערכת שלנו:

{% equation %}\forall x\left(R\left(y\right)\to S\left(x\right)\right)\to\left(R\left(y\right)\to\forall xS\left(x\right)\right){% endequation %}

כאן {% equation %}R,S{% endequation %} הם סימני יחס כלשהם שנמצאים פה בעיקר לצורך הדוגמה. מה הולך פה? הנוסחה הזו היא פשוט דרך אחרת להגיד שאם יש לנו כמת על שני דברים (במקרה שלנו {% equation %}R,S{% endequation %}) כך שהכמת בכלל לא רלוונטי לראשון מביניהם, אפשר להעביר אותו אל השני בלבד וחסל. נסו להוכיח שהנוסחה הזו היא אמת לוגית; אין כאן הרבה יותר ממשחק בהגדרות.

הפורמליזציה של תבנית האקסיומה הזו פשוטה:
<ol start="5">
	<li>{% equation %}\forall x\left(\varphi\to\psi\right)\to\left(\varphi\to\forall x\psi\right){% endequation %}</li>
</ol>
כאשר הדרישה היא ש-{% equation %}x{% endequation %} איננו משתנה חופשי ב-{% equation %}\varphi{% endequation %}. קל לראות שהדרישה הזו הכרחית כדי שהתבנית תגדיר נוסחאות אמיתיות לוגיות; בואו נביט על {% equation %}\forall x\left(x&gt;0\to x&gt;0\right)\to\left(x&gt;0\to\forall x\left(x&gt;0\right)\right){% endequation %} שהוא בבירור לא אמת לוגית - אגף ימין שלו בבירור מתקיים אבל אגף שמאל אומר שאם {% equation %}x{% endequation %} <strong>ספציפי</strong> הוא גדול מאפס אז נובע מכך ש<strong>כל {% equation %}x{% endequation %}</strong> הוא גדול מאפס וזה בוודאי לא נכון.

האם באמת היה צריך להוסיף את תבנית האקסיומה החדשה הזו? האם אי אפשר לקבל אותה מהדברים הקיימים? לא ממש. התבנית הקודמת שהצגתי יודעת <strong>להסיר</strong> {% equation %}\forall{% endequation %}; היא לא יודעת <strong>להזיז</strong> אותו. זה מרמז גם על מה שעדיין חסר לנו - דרך <strong>לייצר</strong> {% equation %}\forall{% endequation %}. לצורך כך אוסיף <strong>כלל היסק</strong> חדש שנקרא {% equation %}\mbox{Gen}{% endequation %} (מלשון Generalization - הכללה). הכלל מקבל פסוק {% equation %}\varphi{% endequation %} ומייצר ממנו את {% equation %}\forall x\varphi{% endequation %} עבור משתנה כלשהו {% equation %}x{% endequation %}, וניתן להשתמש בו גם כאשר {% equation %}x{% endequation %} כן מופיע חופשי ב-{% equation %}\alpha{% endequation %}. עם זאת, יש עליו סייג קטן: אם {% equation %}\Phi{% endequation %} היא קבוצת ההנחות שבה אנחנו משתמשים בהוכחה שלנו, אסור להשתש ב-Gen עבור אף משתנה {% equation %}x{% endequation %} שמופיע חופשי בהנחה כלשהי ב-{% equation %}\Phi{% endequation %}. אצלנו ממילא אנחנו הולכים לדבר רק על קבוצת הנחות שהן <strong>פסוקים</strong>, כלומר נוסחאות בלי משתנים חופשיים, כך שהסייג הזה לא יהיה רלוונטי לנו ונוכל להשתמש ב-Gen בחופשיות.

תחת הסייג הזה פשוט למדי להוכיח ש-Gen עובד: נניח ש-{% equation %}\Phi\models\varphi{% endequation %}, כלומר כל מבנה {% equation %}\mathcal{M}{% endequation %} והשמה {% equation %}z{% endequation %} מקיימים שאם {% equation %}\mathcal{M}\models_{z}\Phi{% endequation %} אז {% equation %}\mathcal{M}\models_{z}\varphi{% endequation %}. כדי להראות ש-{% equation %}\mathcal{M}\models_{z}\forall x\varphi{% endequation %} צריך להראות שמתקיים {% equation %}\mathcal{M}\models_{z\left[x\leftarrow a\right]}\varphi{% endequation %} לכל {% equation %}a\in D^{\mathcal{M}}{% endequation %}. כעת, מכיוון ש-{% equation %}x{% endequation %} לא מופיע חופשי באף הנחה ב-{% equation %}\Phi{% endequation %} הרי ש-{% equation %}\mathcal{M}\models_{z\left[x\leftarrow a\right]}\Phi{% endequation %} (השינוי של הערך ש-{% equation %}x{% endequation %} מקבל בהשמה {% equation %}z{% endequation %} לא משפיע על ערך האמת ש-{% equation %}z{% endequation %} נתנה לפסוקי {% equation %}\Phi{% endequation %}) ולכן {% equation %}\mathcal{M}\models_{z\left[x\leftarrow a\right]}\varphi{% endequation %}.

האם סיימנו להציג את מערכת ההוכחה? תלוי. בהגדרות מסויימות של לוגיקה מסדר ראשון, כן; אבל אני הגדרתי לוגיקה מסדר ראשון כשהיא כוללת את סימן השוויון, והוא זקוק לטיפול מיוחד, מכיוון שהסמנטיקה שלו מיוחדת. הדרך הפשוטה ביותר להבין זאת היא להיות מודעים לכך שכרגע אין למערכת ההוכחה שלנו שום דרך להוכיח את הנוסחה הבאה:

{% equation %}x=x{% endequation %}

די ברור שאפשר להוסיף אותה כתבנית אקסיומה, אבל זה עדיין לא מספיק. צריך עוד תבנית אקסיומה שתגיד לנו שאם שני משתנים הם שווים בערכם, אז כל שני שמות עצם שזהים פרט לאותם משתנים גם כן שווים בערכם, וכל שתי נוסחאות שזהות פרט לאותם משתנים הן שקולות. פורמלית, אז אלו האקסיומות שקשורות לשוויון ({% equation %}x,y{% endequation %} מייצגים משתנים, {% equation %}t,s{% endequation %} מייצגים שמות עצם, {% equation %}\varphi,\psi{% endequation %} מייצגים נוסחאות):
<ol>
	<li>{% equation %}x=x{% endequation %}</li>
	<li>{% equation %}x=y\to t=s{% endequation %} כאשר {% equation %}s{% endequation %} מתקבל מ-{% equation %}t{% endequation %} על ידי החלפת מופע אחד או יותר של {% equation %}x{% endequation %} ב-{% equation %}y{% endequation %}.</li>
	<li>{% equation %}x=y\to\left[\varphi\to\psi\right]{% endequation %} כאשר {% equation %}\psi{% endequation %} מתקבל מ-{% equation %}\varphi{% endequation %} על ידי החלפת מופע אחד או יותר של {% equation %}x{% endequation %} ב-{% equation %}y{% endequation %}.</li>
</ol>
האם סיימנו? באופן מפתיע למדי, התשובה היא כן! מסתבר שדי באקסיומות וכללי ההיסק שהראיתי כדי להוכיח כל פסוק בלוגיקה מסדר ראשון שנובע לוגית מקבוצת פסוקים של הנחות. כלומר, כעת אני יכול להוכיח את משפט השלמות והנאותות הבא: אם {% equation %}\Phi{% endequation %} היא קבוצת פסוקים בלוגיקה מסדר ראשון ו-{% equation %}\varphi{% endequation %} הוא פסוק כלשהו, אז {% equation %}\Phi\vdash\varphi\iff\Phi\models\varphi{% endequation %}. את ההוכחה אתחיל להציג בפוסט הבא.
