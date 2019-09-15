---
id: 2363
title: "משפט השלמות של גדל, ההוכחה (חלק א')"
date: 2013-02-25 22:52:55
layout: post
categories: 
  - לוגיקה
tags: 
  - לוגיקה מסדר ראשון
  - משפט השלמות של גדל
---
ב<a href="http://www.gadial.net/2013/02/23/first_order_logic_proof_system/">פוסט הקודם</a> הצגתי מערכת הוכחה ללוגיקה מסדר ראשון, והפעם אני רוצה להתחיל את ההוכחה שהמערכת הזו היא שלמה ונאותה. למעשה, אני הולך לדלג על הוכחת הנאותות כי די כיסיתי אותה בפוסט הקודם - שכנעתי אתכם (אני מקווה) שהאקסיומות של המערכת הן אמיתות לוגיות, ושכללי ההיסק משמרים נביעה לוגית, ומכאן ההוכחה היא שגרתית. אם כן, החלק המעניין פה הוא הוכחת השלמות. משפט השלמות הוכח במקור על ידי קורט גדל בשנת 1930 ולכן הוא נקרא "משפט השלמות של גדל" (עם זאת, ההוכחה שאראה היא לא של גדל אלא של הנקין מ-1949); צריך כמובן להיזהר ולא לבלבל את זה עם משפטי אי השלמות של גדל שהוכחו ב-1931 ומדברים על סוג שונה של שלמות. משפטי אי השלמות מדברים על אי-שלמות של <strong>תורות</strong>: על כך שאם קבוצה של פסוקים {% equation %}\Phi{% endequation %} בלוגיקה מסדר ראשון מקיימת אי-אילו תכונות, אז קיים פסוק {% equation %}\varphi{% endequation %}כך ש-{% equation %}\Phi\not\vdash\varphi{% endequation %} וגם {% equation %}\Phi\not\vdash\neg\varphi{% endequation %} - כלומר, {% equation %}\Phi{% endequation %} לא מוכיחה לא אותו ואת שלילתו. משפט השלמות מדבר על שלמות של <strong>מערכת ההוכחה</strong>, והוא אומר שאם {% equation %}\Phi\models\varphi{% endequation %} עבור {% equation %}\Phi,\varphi{% endequation %} כלשהם, אז {% equation %}\Phi\vdash\varphi{% endequation %} - כלומר, כל מה שנובע לוגית גם יכיח.

משטיפלנו בבלבול הזה אפשר לגשת לעבודה. בואו נתחיל בלהיזכר באופן שבו הוכחנו את משפט השלמות עבור תחשיב הפסוקים, כי הרעיון הבסיסי עדיין עובד גם כאן: הוכחנו טענה שנראית ממבט ראשון שונה לגמרי - שאם קבוצה {% equation %}\Phi{% endequation %} היא עקבית, אז קיים לה מודל, כאשר "עקבית" פירושו שהיא אינה מוכיחה דבר והיפוכו. הטענה הזו גוררת מיידית את משפט השלמות באופן הבא: נניח כי {% equation %}\Phi\models\varphi{% endequation %} ונניח בשלילה ש-{% equation %}\Phi\cup\left\{ \neg\varphi\right\} {% endequation %} עקבית, אז קיים ל-{% equation %}\Phi\cup\left\{ \neg\varphi\right\} {% endequation %} מודל {% equation %}\mathcal{M}{% endequation %}, ובפרט {% equation %}\mathcal{M}\models\Phi{% endequation %} ולכן {% equation %}\mathcal{M}\models\varphi{% endequation %} (זו המשמעות של הטענה ש-{% equation %}\varphi{% endequation %} נובע לוגית מ-{% equation %}\Phi{% endequation %}). מצד שני, {% equation %}\mathcal{M}\models\neg\varphi{% endequation %} וזו סתירה (בהינתן מודל ופסוק, ערך האמת של הפסוק נקבע בצורה יחידה והוא תמיד הפוך מזה של שלילתו). לכן נובע ש-{% equation %}\Phi\cup\left\{ \neg\varphi\right\} {% endequation %} אינה עקבית, ומכך נובע ש-{% equation %}\Phi\vdash\varphi{% endequation %}. את השלב האחרון ("משפט ההוכחה בדרך השלילה") הוכחתי עבור תחשיב הפסוקים וההוכחה תקפה באותה מידה גם בלוגיקה מסדר ראשון, עד כדי נקודה קטנה אך מהותית: המשפט הזה מתבסס על מה שנקרא <strong>משפט הדדוקציה</strong>, וההוכחה של משפט הדדוקציה ללוגיקה מסדר ראשון דורשת עוד טיפה עבודה.

משפט הדדוקציה אומר, כזכור, שאם {% equation %}\Phi\cup\left\{ \alpha\right\} \vdash\beta{% endequation %} אז {% equation %}\Phi\vdash\alpha\to\beta{% endequation %}. בתחשיב הפסוקים ראינו כיצד להוכיח זאת במקרה שבו {% equation %}\beta{% endequation %} היא אקסיומה, הנחה מתוך {% equation %}\Phi{% endequation %}, {% equation %}\alpha{% endequation %} בעצמה, או מתקבלת על ידי MP מפסוקים שעבורם אנו כבר יודעים שמשפט הדדוקציה נכון. עם זאת, בלוגיקה מסדר ראשון צריך גם להתייחס למקרה שבו {% equation %}\beta{% endequation %} מתקבלת מהפעלת GEN, כלומר {% equation %}\beta=\forall x\gamma{% endequation %} כאשר {% equation %}\gamma{% endequation %} כבר מקיימת את משפט הדדוקציה, כלומר {% equation %}\Phi\vdash\alpha\to\gamma{% endequation %}.

אם כן, מה עושים? למרבה המזל, יש לנו תבנית אקסיומה שנבחרה בדיוק כדי להתמודד עם הסיטואציה הזו - תבנית אקסיומה מס' 5, {% equation %}\forall x\left(\varphi\to\psi\right)\to\left(\varphi\to\forall x\psi\right){% endequation %}. הדרישה של תבנית האקסיומה הזו היא ש-{% equation %}x{% endequation %} לא יהיה משתנה חופשי ב-{% equation %}\varphi{% endequation %}. במקרה שלנו {% equation %}\varphi{% endequation %} הוא {% equation %}\alpha{% endequation %}, והרי {% equation %}\beta{% endequation %} מתקבל על ידי הוכחה מ-{% equation %}\Phi\cup\left\{ \alpha\right\} {% endequation %} ודרשתי במפורש שאם GEN יופעל, אז זה יהיה רק עם משתנה שאינו מופיע חופשי ב-{% equation %}\Phi\cup\left\{ \alpha\right\} {% endequation %}, ומכאן ש-{% equation %}x{% endequation %} אינו חופשי ב-{% equation %}\alpha{% endequation %}. לכן אפשר לכתוב את ההוכחה הפורמלית הבאה:
<ol>
	<li>{% equation %}\alpha\to\gamma{% endequation %} (הנחה).</li>
	<li>{% equation %}\forall x\left(\alpha\to\gamma\right){% endequation %} (GEN על 1 עם משתנה שאינו מופיע חופשי ב-{% equation %}\Phi{% endequation %})</li>
	<li>{% equation %}\forall x\left(\alpha\to\gamma\right)\to\left(\alpha\to\forall x\gamma\right){% endequation %} (תבנית אקסיומה 5).</li>
	<li>{% equation %}\alpha\to\forall x\gamma{% endequation %} (MP על 2,3).</li>
</ol>
וקיבלנו בדיוק את {% equation %}\alpha\to\beta{% endequation %} כפי שרצינו. זה מסיים את ההעברה של המשפטים מתחשיב הפסוקים ללוגיקה מסדר ראשון ומאפשר לנו להתמקד בעיקר.

אם כן, מעתה היעד שלנו הוא להוכיח שלקבוצה עקבית {% equation %}\Phi{% endequation %} של פסוקים קיים מודל. בתחשיב הפסוקים "מודל" היה דבר פשוט למדי - השמה של ערכי אמת לכל המשתנים, וחסל. בלוגיקה מסדר ראשון מודל הוא עסק מסובך הרבה יותר - צריך להגדיר עולם שהוא קבוצה כלשהי של איברים, ולכל הסימנים במילון של {% equation %}\Phi{% endequation %} צריך להתאים יחסים, פונקציות וקבועים מתוך העולם. על פניו בכלל לא ברור <strong>מאיפה</strong> אנחנו הולכים להמציא את העולם הזה. כאן נכנס לתמונה התעלול הראשון: האיברים של העולם שלנו יהיו (בערך - אני משקר כאן כרגע) הקבועים של המילון של {% equation %}\Phi{% endequation %}. אלא שזה נשמע על פניו מטופש - מה אם במילון אין בכלל קבועים?

ובכן, בתחשיב הפסוקים האופן שבו התמודדנו עם בעיית ה"ממש לא ברור לי מאיפה להתחיל" היה לקחת את קבוצת הפסוקים שלנו ו<strong>להרחיב</strong> אותה כך שנקבל קבוצה שבה יהיה לנו מעט מאוד חופש פעולה - קבוצה כזו שאם קיים לה מודל, אז די ברור לנו איך הוא <strong>חייב</strong> להיראות. צמצום חופש הבחירה עזר לנו מאוד. אותו הדבר יקרה גם כאן - אנחנו ניקח את {% equation %}\Phi{% endequation %} ונרחיב אותה, אבל גם ניקח אתצ {% equation %}\tau{% endequation %}, המילון של {% equation %}\Phi{% endequation %}, ונרחיב גם אותו על ידי הוספה של המון סימני קבועים. אחרי שנקבל את {% equation %}\Phi{% endequation %} המורחבת מעל המילון המורחב כבר יהיה די ברור איך המודל חייב להיראות, וכל מה שיישאר הוא לטפל בפרטים הטכניים.

מה שנרצה לעשות הוא להרחיב את אוסף הקבועים של {% equation %}\tau{% endequation %} ואת {% equation %}\Phi{% endequation %} כך שהם יקיימו את התכונה הבאה: ש-{% equation %}\Phi{% endequation %} המורחבת תוכל להוכיח שלכל נוסחה {% equation %}\varphi\left(x\right){% endequation %} עם משתנה חופשי יחיד {% equation %}x{% endequation %}, אם {% equation %}\exists x\varphi\left(x\right){% endequation %} מתקיים אז קיים קבוע ש"מוכיח" את זה, כלומר יש קבוע {% equation %}c{% endequation %} כך ש-{% equation %}\varphi\left(c\right){% endequation %} מתקיים. פורמלית אנו אומרים שקבוצת סימני קבועים {% equation %}C{% endequation %} היא קבוצת <strong>עדים</strong> עבור {% equation %}\Phi{% endequation %} אם לכל נוסחה {% equation %}\varphi\left(x\right){% endequation %} עם משתנה חופשי יחיד קיים {% equation %}c\in C{% endequation %} כך שמתקיים

{% equation %}\Phi\vdash\exists x\varphi\left(x\right)\to\varphi\left(c\right){% endequation %}

כאן {% equation %}\varphi\left(c\right){% endequation %} פירושו מה שמקבלים כאשר מציבים ב-{% equation %}\varphi{% endequation %} את הקבוע {% equation %}c{% endequation %} במקום {% equation %}x{% endequation %}.

אז כמו בתחשיב הפסוקים, יש לנו שני שלבים: שלב ההרחבה של {% equation %}\Phi{% endequation %} ו-{% equation %}\tau{% endequation %}, ושלב ההוכחה שלתורה המורחבת יש מודל. מכיוון שמודל לתורה המורחבת מעל המילון המורחב הוא עדיין מודל גם לתורה המקורית מעל המילון המקורי, זה יסיים את ההוכחה.

למרות שמבחינה מעשית שלב ההרחבה קודם לשלב בניית המודל, אני מעדיף לבצע אותם בסדר הפוך, מכיוון ששלב ההרחבה בעייתי יותר טכנית מסיבות שאתאר בהמשך, והרעיון היפה המרכזי בהוכחה נמצא בשלב בניית המודל. אם כן, אני מניח כרגע שנתונה לי תורה (קבוצת פסוקים עקבית) {% equation %}\Phi{% endequation %} מעל מילון {% equation %}\tau{% endequation %} כך שמתקיימות שתי התכונות הבאות:
<ol>
	<li>{% equation %}\Phi{% endequation %} עקבית מקסימלית, במובן זה שהוספת כל פסוק ל-{% equation %}\Phi{% endequation %} יהפוך את {% equation %}\Phi{% endequation %} ללא-עקבית.</li>
	<li>קיימת קבוצת עדים {% equation %}C{% endequation %} עבור {% equation %}\Phi{% endequation %}, כלומר לכל נוסחה {% equation %}\varphi\left(x\right){% endequation %} עם משתנה חופשי יחיד {% equation %}x{% endequation %} קיים קבוע {% equation %}c\in C{% endequation %} כך ש-{% equation %}\Phi\vdash\exists x\varphi\left(x\right)\to\varphi\left(c\right){% endequation %}.</li>
</ol>
בואו נבנה ל-{% equation %}\Phi{% endequation %} מודל {% equation %}\mathcal{M}{% endequation %}. מודל כולל <strong>עולם</strong> שהוא קבוצה של איברים, ו<strong>פרשנויות</strong> לסימני היחס, הפונקציות והקבועים של {% equation %}\tau{% endequation %}. הרעיון האינטואיטיבי הוא לעשות את הדבר הבא: להגדיר את העולם להיות שווה לקבוצת הקבועים של {% equation %}\tau{% endequation %}, כלומר לקחת את האובייקט ה<strong>סינטקטי</strong> של סימני קבועים, ולהגדיר את המודל <strong>באמצעותו</strong>. אחר כך, בהינתן סימן יחס {% equation %}R\left(x,y\right){% endequation %} (נניח לצורך הדוגמה שהוא דו-מקומי) להגדיר יחס {% equation %}R^{\mathcal{M}}\left(x,y\right){% endequation %} במודל על ידי כך שלכל שני איברים {% equation %}c,d{% endequation %} של העולם, {% equation %}\left(c,d\right)\in R^{\mathcal{M}}{% endequation %} אם ורק אם הפסוק {% equation %}R\left(c,d\right){% endequation %} יכיח מתוך {% equation %}\Phi{% endequation %}. זה הרעיון, והוא פשוט ומבריק ויפהפה. כמובן שהפרטים הטכניים קצת מסתבכים עכשיו.

ההוכחה מתפצלת כאן למעשה לשתי אפשרויות, בהתאם לשאלה אם הגדרנו לוגיקה מסדר ראשון עם סימן השוויון או בלעדיו. אני בחרתי להגדיר עם; כפי שנראה, זה גורם לנו לאי-אלו קשיים, אבל אסביר בהמשך אילו קשיים היו נוצרים אם הייתי בוחר לעבוד בלעדיו (זה היה מוביל לבניית מודל שמרגיש לי מלאכותי יותר).

אז נניח שאנחנו עובדים בלוגיקה עם סימן השוויון. הנה הבעיה - הביטו לרגע בפסוק {% equation %}c=d{% endequation %} כאשר {% equation %}c,d{% endequation %} הם שני איברים של {% equation %}C{% endequation %}. נניח שהוא יכיח מתוך {% equation %}\Phi{% endequation %} (וזה בהחלט יכול לקרות). פירוש הדבר הוא ש<strong>אסור</strong> לנו להגדיר את {% equation %}c,d{% endequation %} בתור איברים שונים בעולם של {% equation %}\mathcal{M}{% endequation %}, כי אז הפסוק {% equation %}c=d{% endequation %} לא יהיה ספיק במודל הזה (ומכיוון שמערכת ההוכחה שלנו נאותה, ינבע מכך ש-{% equation %}\mathcal{M}{% endequation %} אינו מודל של {% equation %}\Phi{% endequation %}). הבעיה הזו מכריחה אותנו להגדיר את העולם של {% equation %}\mathcal{M}{% endequation %} באופן קצת יותר מחוכם. מה שנעשה הוא להגדיר <strong>יחס שקילות</strong> על אברי {% equation %}C{% endequation %}, כך ש-{% equation %}c\equiv d{% endequation %} אם ורק אם {% equation %}\Phi\vdash c=d{% endequation %}. כלומר, אנחנו אומרים שכל הקבועים של {% equation %}C{% endequation %} ש-{% equation %}\Phi{% endequation %} "מוכיחה שהם שווים" יהיו שקולים האחד לשני.

צריך להוכיח שהיחס הזה הוא אכן יחס שקילות. לצורך כך נצטרך להוכיח דברים על יחס השוויון, אז בואו ניזכר באקסיומות שהיו קשורות אליו והכנסנו למערכת ההוכחה שלנו:
<ol>
	<li>{% equation %}x=x{% endequation %}</li>
	<li>{% equation %}x=y\to t=s{% endequation %} כאשר {% equation %}s{% endequation %} מתקבל מ-{% equation %}t{% endequation %} על ידי החלפת מופע אחד או יותר של {% equation %}x{% endequation %} ב-{% equation %}y{% endequation %}.</li>
	<li>{% equation %}x=y\to\left[\varphi\to\psi\right]{% endequation %} כאשר {% equation %}\psi{% endequation %} מתקבל מ-{% equation %}\varphi{% endequation %} על ידי החלפת מופע אחד או יותר של {% equation %}x{% endequation %} ב-{% equation %}y{% endequation %}.</li>
</ol>
בואו נתחיל. ראשית, אם {% equation %}c\in C{% endequation %} כלשהו צריך להראות ש-{% equation %}\Phi\vdash c=c{% endequation %}. הנה הוכחה פורמלית:
<ol>
	<li>{% equation %}x=x{% endequation %} (אקסיומת שוויון מס' 1)</li>
	<li>{% equation %}x=x\to c=c{% endequation %} (אקסיומת שוויון מס' 2 עם {% equation %}t=s=c{% endequation %})</li>
	<li>{% equation %}c=c{% endequation %} (MP על 1,2).</li>
</ol>
עכשיו, אם {% equation %}c,d\in C{% endequation %} הם איברים כלשהם כך ש-{% equation %}\Phi\vdash c=d{% endequation %} צריך להוכיח שגם {% equation %}\Phi\vdash d=c{% endequation %}:
<ol>
	<li>{% equation %}x=y\to\left(x=x\to y=x\right){% endequation %} (אקסיומת שוויון מס' 3 עם {% equation %}\varphi=\left(x=x\right){% endequation %} ו-{% equation %}\psi=\left(y=x\right){% endequation %}).</li>
	<li>{% equation %}\forall x\forall y\left(x=y\right)\to\left(x=x\to y=x\right){% endequation %} (Gen על 1).</li>
	<li>{% equation %}\left[\forall x\forall y\left(x=y\right)\to\left(x=x\to y=x\right)\right]\to\left[\left(c=d\right)\to\left(c=c\to d=c\right)\right]{% endequation %} (תבנית אקסיומה 4)</li>
	<li>{% equation %}c=d\to\left(c=c\to d=c\right){% endequation %} (MP על 2,3).</li>
	<li>{% equation %}c=d{% endequation %} (יכיח מ-{% equation %}\Phi{% endequation %}).</li>
	<li>{% equation %}c=c\to d=c{% endequation %} (MP על 4,5).</li>
	<li>{% equation %}c=c{% endequation %} (יכיח מ-{% equation %}\Phi{% endequation %}).</li>
	<li>{% equation %}d=c{% endequation %} (MP על 6,7).</li>
</ol>
זה היה מבעית למדי, מה שמעלה את החשש שהוכחת טרנזיטיביות תהיה גרועה עוד יותר. נניח ש-{% equation %}c,d,e\in C{% endequation %} מקיימים {% equation %}\Phi\vdash c=d{% endequation %} וגם {% equation %}\Phi\vdash d=e{% endequation %}, אז צריך להוכיח ש-{% equation %}\Phi\vdash c=e{% endequation %}. כפי שאולי הבנתם מההוכחה הקודמת, מספיק להוכיח ש-{% equation %}x=y\to\left(y=z\to x=z\right){% endequation %} כדי לסיים, אבל זו הרי בדיוק אקסיומת שוויון מס' 3 עם {% equation %}\varphi=\left(x=z\right){% endequation %} ו-{% equation %}\psi=\left(y=z\right){% endequation %}, כך שאחסוך מכם את המשך ההוכחה המפלצתית. זה מוכיח לנו שהיחס שהגדרתי לעיל הוא אכן יחס שקילות, ולכן אפשר לדבר על <strong>מחלקות השקילות</strong> שלו. כזכור, אם {% equation %}c\in C{% endequation %} הוא איבר כלשהו, אז מסמנים {% equation %}\left[c\right]=\left\{ d\in C\ |\ c\equiv d\right\} {% endequation %}. הקבוצה {% equation %}\left[c\right]{% endequation %} נקראת <strong>מחלקת השקילות</strong> של {% equation %}c{% endequation %} ולא קשה לראות ש-{% equation %}C{% endequation %} מתפרקת לאיחוד זר של מחלקות שקילות של איברים בה.

כעת אפשר להתחיל את הגדרת המודל {% equation %}\mathcal{M}{% endequation %}. ראשית נגדיר את העולם שלו: {% equation %}D^{\mathcal{M}}=\left\{ \left[c\right]\ |\ c\in C\right\} {% endequation %}. כעת נותר לתת פרשנויות לסימני היחס, הקבועים והפונקציות.

נתחיל מסימני היחס. יהא {% equation %}R\left(x_{1},\dots,x_{n}\right)\in\tau{% endequation %} סימן יחס {% equation %}n{% endequation %}-מקומי. נגדיר יחס {% equation %}R^{\mathcal{M}}\subseteq\left(D^{\mathcal{M}}\right)^{n}{% endequation %} באופן הבא: לכל {% equation %}c_{1},\dots,c_{n}\in C{% endequation %}, {% equation %}\left(\left[c_{1}\right],\dots,\left[c_{n}\right]\right)\in R^{\mathcal{M}}{% endequation %} אם ורק אם {% equation %}\Phi\vdash R\left(c_{1},\dots,c_{n}\right){% endequation %}. זו הגדרה שנראית הגיונית, אבל כמו כל הגדרה שמערבת מחלקות שקילות, יש סכנה שהיא <strong>לא מוגדרת היטב</strong>. למה הכוונה? ייתכן שיש {% equation %}d_{1},\dots,d_{n}\in C{% endequation %} כך ש-{% equation %}\left[c_{i}\right]=\left[d_{i}\right]{% endequation %} (כלומר, מחלקת השקילות של {% equation %}c_{i}{% endequation %} ו-{% equation %}d_{i}{% endequation %} זהות, לכל {% equation %}1\le i\le n{% endequation %}) ועם זאת {% equation %}\Phi\vdash R\left(c_{1},\dots,c_{n}\right){% endequation %} אבל {% equation %}\Phi\not\vdash R\left(d_{1},\dots,d_{n}\right){% endequation %}, מה שאומר שההחלטה אם {% equation %}\left(\left[c_{1}\right],\dots,\left[c_{n}\right]\right)\in R^{\mathcal{M}}{% endequation %} אינה תלויה במחלקות השקילות בלבד אלא ממש ב<strong>נציגים</strong> שאנחנו בוחרים להן, ואסור לנו לעשות את זה - אנחנו חייבים לקבוע באופן חד משמעי עבור כל מחלקת שקילות מה יקרה איתה.

במקרה שלנו אין בעיה אמיתית שכזו. נניח ש-{% equation %}\Phi\vdash R\left(c_{1},\dots,c_{n}\right){% endequation %} וכמו כן ש-{% equation %}c_{1}\equiv d_{1}{% endequation %}, כלומר {% equation %}\Phi\vdash c_{1}=d_{1}{% endequation %}. אז מהאקסיומה {% equation %}x=y\to R\left(x,c_{2},\dots,c_{n}\right)=R\left(y,c_{2},\dots,c_{n}\right){% endequation %} אפשר לקבל חיש קל ש-{% equation %}\Phi\vdash R\left(d_{1},\dots,c_{n}\right){% endequation %} וכך להחליף בהדרגתיות את כל ה-{% equation %}c{% endequation %}-ים ב-{% equation %}d{% endequation %}-ים. עם זאת, חשוב היה לי להדגיש שזו נקודה שיש לשים לב אליה במהלך ההגדרה, וזה חלק מהסיבוך הנוסף שנגרם לנו מכך שהלוגיקה מסדר ראשון שלנו כוללת שוויון.

נעבור לקבועים. מפתה להגיד שלכל סימן קבוע {% equation %}c\in\tau{% endequation %}, נגדיר את הפרשנות שלו להיות {% equation %}c^{\mathcal{M}}=\left[c\right]{% endequation %}, וזה אכן הרעיון הכללי, אבל זה <strong>לא מספיק</strong>. הבעיה היא שאולי יש סימני קבועים שבכלל לא שייכים ל-{% equation %}C{% endequation %}. הפואנטה היא שגם במקרה זה, הפרשנות שנותנים לסימנים הללו <strong>חייבת</strong> להיות זהה לפרשנות שנותנים לפחות לאחד מהקבועים. למה? או, זו הזדמנות לראות את עניין ה"{% equation %}C{% endequation %} היא קבוצת עדים" בפעולה.

נניח ש-{% equation %}d\in\tau{% endequation %} הוא סימן קבוע כלשהו. אז אנחנו יודעים שהפסוק הבא הוא אמת לוגית: {% equation %}\exists x\left(x=d\right){% endequation %}. עכשיו, {% equation %}\Phi{% endequation %} היא קבוצה עקבית מקסימלית, מה שאומר (ואת זה אנחנו יודעים עוד מתחשיב הפסוקים) שלכל פסוק היא מוכיחה אותו או את שלילתו (אחרת היה אפשר להוסיף את הפסוק אליה ולקבל קבוצה גדולה יותר שעדיין עקבית). בגלל נאותות מערכת ההוכחה לא ייתכן שהיא תוכיח דבר שהוא סתירה לוגית, ולכן {% equation %}\Phi\vdash\exists x\left(x=d\right){% endequation %}, ומכיוון ש-{% equation %}C{% endequation %} היא קבוצת עדים, אז קיים {% equation %}c\in C{% endequation %} כך ש-{% equation %}\Phi\vdash\exists x\left(x=d\right)\to\left(c=d\right){% endequation %}, ומשילוב שני אלו נקבל ש-{% equation %}\Phi\vdash c=d{% endequation %}, וקיבלנו את מה שצריכה להיות הפרשנות של {% equation %}d{% endequation %}: {% equation %}d^{\mathcal{M}}=\left[c\right]{% endequation %}. גם כאן, התהליך היה מוגדר היטב: אם במקום {% equation %}c{% endequation %} היינו מוצאים עד אחר, היינו מקבלים גם עבורו שהוא שווה ל-{% equation %}d{% endequation %} ומהטרנזיטיביות שכבר ראינו של השוויון היינו מקבלים ש-{% equation %}\Phi{% endequation %} מוכיחה את הפסוק שאומר ששני העדים שווים ולכן מחלקת השקילות שלהם שווה.

בפונקציות מטפלים באופן דומה. אם {% equation %}f\left(x_{1},\dots,x_{n}\right)\in\tau{% endequation %} הוא סימן פונקציה {% equation %}n{% endequation %} מקומי, ואנחנו צריכים להגדיר את {% equation %}f^{\mathcal{M}}\left(\left[c_{1}\right],\dots,\left[c_{n}\right]\right){% endequation %} אז נתבונן בפסוק {% equation %}\exists x\left(f\left(c_{1},\dots,c_{n}\right)=x\right){% endequation %}, ניקח עד {% equation %}c{% endequation %} עבורו ונגדיר {% equation %}f^{\mathcal{M}}\left(\left[c_{1}\right],\dots,\left[c_{n}\right]\right)=\left[c\right]{% endequation %}. גם פה צריך להוכיח שהכל מוגדר היטב אבל נדמה לי שכבר הבנתם את הרעיון. זה מסיים את הגדרת המודל {% equation %}\mathcal{M}{% endequation %}.

כמובן שהגדרת המודל היא רק חלק מהעבודה, עכשיו צריך גם להוכיח שהמודל "עובד", כלומר שהוא מספק כל פסוק ב-{% equation %}\Phi{% endequation %}. איך נראים פסוקים באופן כללי? ובכן, פסוק הוא נוסחה שאין בה משתנים חופשיים. אז אפשר להתחיל מנוסחאות שאין בהן משתנים בכלל - כל שמות העצם שמופיעים בהן מורכבים רק מקבועים וסימני פונקציות. פסוק בסיסי מסוג זה חייב לכלול יחס (שם עצם לבדו אינו פסוק; פסוק מורכב מיחסים על שמות עצם, שמעורבבים האחד עם השני עם קשרים וכמתים). אז ראשית כל יש לנו פסוקים מהצורה

{% equation %}t_{1}=t_{2}\in\Phi{% endequation %}

כאשר {% equation %}t_{1},t_{2}{% endequation %} שמות עצם שאינם כוללים משתנים. אנחנו רוצים לחשב את הערך של שני שמות העצם הללו במודל ולראות שהוא זהה. לא ממש ברור איך לעשות את זה באופן ישיר, אבל קל לעשות את זה באופן עקיף: נסתכל על הפסוק {% equation %}\exists x\left(t_{1}=x\right){% endequation %} ונקבל, כרגיל, שיש {% equation %}c\in C{% endequation %} כך ש-{% equation %}t_{1}=c\in\Phi{% endequation %}. בדומה נקבל ש-{% equation %}t_{2}=d\in\Phi{% endequation %} עבור {% equation %}d\in C{% endequation %} כלשהו, וכבר ראינו שאפשר להוכיח טרנזיטיביות, כלומר ש-{% equation %}c=d\in\Phi{% endequation %} ולכן {% equation %}\left[c\right]=\left[d\right]{% endequation %} וזהו הערך שהמודל מעניק לשני שמות העצם {% equation %}t_{1},t_{2}{% endequation %} כך שבמקרה הזה טיפלנו.

כעת, הסוג הנוסף של פסוק בסיסי הוא פסוק מהצורה

{% equation %}R\left(t_{1},\dots,t_{n}\right)\in\Phi{% endequation %}

כאשר {% equation %}R{% endequation %} סימן יחס כלשהו ו-{% equation %}t_{1},\dots,t_{n}{% endequation %} שמות עצם כלשהם שאינם כוללים משתנים. כמקודם, מוצאים {% equation %}c_{1},\dots,c_{n}{% endequation %} כך ש-{% equation %}t_{i}=c_{i}\in\Phi{% endequation %} ומכאן נוכל להוכיח ש-{% equation %}R\left(c_{1},\dots,c_{n}\right)\in\Phi{% endequation %}, מה שיגרור ש-{% equation %}\left(\left[c_{1}\right],\dots,\left[c_{n}\right]\right)\in R^{\mathcal{M}}{% endequation %}, מה שמסיים את המקרה הזה. כדאי לשים לב שבגלל ש-{% equation %}\Phi{% endequation %} עקבית מקסימלית הרי שבשני המקרים הוכחנו יותר מאשר את מה שרצינו - הוכחנו גם שאם {% equation %}t_{1}=t_{2}\notin\Phi{% endequation %} אז הערכים שהמודל מעניק לשמות העצם הללו שונים (אחרת אפשר היה להוסיף את {% equation %}t_{1}=t_{2}{% endequation %} ל-{% equation %}\Phi{% endequation %} מבלי לפגוע בעקביות) וכך גם עבור ה-{% equation %}R{% endequation %}-ים. זה יועיל לנו בהמשך.

כעת אפשר להמשיך באינדוקציה על מבנה יתר הפסוקים הקיימים. לכל פסוק {% equation %}\varphi{% endequation %} נרצה להראות ש-{% equation %}\mathcal{M}\models\varphi{% endequation %} אם ורק אם {% equation %}\varphi\in\Phi{% endequation %}. נתחיל עם פסוקים מהצורה {% equation %}\neg\varphi{% endequation %} כאשר {% equation %}\varphi{% endequation %} הוא פסוק שעליו כבר הוכחנו את הטענה. אז מכיוון ש-{% equation %}\Phi{% endequation %} עקבית מקסימלית, {% equation %}\neg\varphi\in\Phi{% endequation %} אם ורק אם {% equation %}\varphi\notin\Phi{% endequation %} אם ורק אם {% equation %}\mathcal{M}\not\models\varphi{% endequation %}, אם ורק אם {% equation %}\mathcal{M}\models\varphi{% endequation %}. זה היה קל.

עבור פסוק מהצורה {% equation %}\varphi\to\psi{% endequation %} הנימוק ארוך יותר אבל לא באמת מסובך יותר. מכיוון שלמשהו כמו {% equation %}\varphi\to\psi{% endequation %} יש רק השמה לא מספקת אחת, יהיה קל יותר להוכיח ש-{% equation %}\varphi\to\psi\notin\Phi{% endequation %} אם ורק אם {% equation %}\mathcal{M}\models\varphi{% endequation %} וגם {% equation %}\mathcal{M}\not\models\psi{% endequation %}. אם כן, {% equation %}\varphi\to\psi\notin\Phi{% endequation %} אם ורק אם {% equation %}\neg\left(\varphi\to\psi\right)\in\Phi{% endequation %}. כעת, תעלול: הבה ונסתכל על הפסוקים {% equation %}\neg\left(\varphi\to\psi\right)\to\varphi{% endequation %} ו-{% equation %}\neg\left(\varphi\to\psi\right)\to\neg\psi{% endequation %}. בדיקה ישירה תראה לנו שהם טאוטולוגיות, ולכן יכיחים מ-{% equation %}\Phi{% endequation %} בלי הנחות כלל, רק על ידי אקסיומות 1-3 ו-MP. לכן נקבל ש-{% equation %}\Phi\vdash\varphi{% endequation %} ו-{% equation %}\Phi\vdash\neg\psi{% endequation %}, מה שקורה אם ורק אם {% equation %}\mathcal{M}\models\varphi{% endequation %} וגם {% equation %}\mathcal{M}\not\models\psi{% endequation %}, כנדרש.

מה נותרו? כמתים. יהיה יותר פשוט רעיונית לטפל ב-{% equation %}\exists{% endequation %}; הטיפול ב-{% equation %}\forall{% endequation %} יהיה זהה מכיוון ש-{% equation %}\exists x\varphi\left(x\right){% endequation %} שקול לפסוק {% equation %}\neg\forall x\neg\varphi\left(x\right){% endequation %}.

אם כן, נוכיח ש-{% equation %}\exists x\varphi\left(x\right)\in\Phi{% endequation %} אם ורק אם {% equation %}\mathcal{M}\models\exists x\varphi\left(x\right){% endequation %}. הבעיה היא ש-{% equation %}\varphi\left(x\right){% endequation %} הוא לא פסוק, כי {% equation %}x{% endequation %} חופשי בו, ולכן אי אפשר להשתמש עליו בהנחת האינדוקציה והכל קורס, <strong>אלמלא</strong> היה לנו את התכונה המוזרה והכל כך לא ברורה במבט ראשון של "עד להוכחה". בגלל ש-{% equation %}C{% endequation %} היא קבוצת עדים, אז קיים קבוע {% equation %}c{% endequation %} כך ש-{% equation %}\Phi\vdash\exists x\varphi\left(x\right)\to\varphi\left(c\right){% endequation %}, ולכן {% equation %}\varphi\left(c\right)\in\Phi{% endequation %} ו-{% equation %}\varphi\left(c\right){% endequation %} הוא פסוק כך שהנחת האינדוקציה פועלת עליו, ו-{% equation %}\mathcal{M}\models\varphi\left(c\right){% endequation %}, כלומר {% equation %}\mathcal{M}\models\exists x\varphi\left(x\right){% endequation %} (פורמלית: אם {% equation %}z{% endequation %} היא השמה כלשהי, אז {% equation %}\mathcal{M}\models_{z\left[x\leftarrow\left[c\right]\right]}\varphi\left(x\right){% endequation %} ולכן {% equation %}\mathcal{M}\models_{z}\exists x\varphi\left(x\right){% endequation %}). הטיעון עובד באותו האופן בכיוון השני עד שמגיעים לכך ש-{% equation %}\varphi\left(c\right)\in\Phi{% endequation %} ורוצים להסיק מכך ש-{% equation %}\exists x\varphi\left(x\right)\in\Phi{% endequation %}; את זה עושים באמצעות הפסוק {% equation %}\varphi\left(c\right)\to\exists x\varphi\left(x\right){% endequation %} שיכיח מ-{% equation %}\Phi{% endequation %}. אם אתם תוהים למה הוא יכיח, הנה הוכחה פורמלית:
<ol>
	<li>{% equation %}\forall x\neg\varphi\left(x\right)\to\neg\varphi\left(c\right){% endequation %} (תבנית אקסיומה 4).</li>
	<li>{% equation %}\left[\forall x\neg\varphi\left(x\right)\to\neg\varphi\left(c\right)\right]\to\left[\neg\neg\varphi\left(c\right)\to\neg\forall x\neg\varphi\left(x\right)\right]{% endequation %} (תבנית אקסיומה 3).</li>
	<li>{% equation %}\neg\neg\varphi\left(c\right)\to\neg\forall x\neg\varphi\left(x\right){% endequation %} (MP על 1,2).</li>
	<li>{% equation %}\neg\neg\varphi\left(c\right)\to\exists x\varphi\left(x\right){% endequation %} (סתם שינוי סימון שיהיה קריא).</li>
	<li>{% equation %}\left[\neg\neg\varphi\left(c\right)\to\exists x\varphi\left(x\right)\right]\to\left[\varphi\left(c\right)\to\exists x\varphi\left(x\right)\right]{% endequation %} (טאוטולוגיה של תחשיב הפסוקים: {% equation %}\left(\neg\neg A\to B\right)\to\left(A\to B\right){% endequation %}).</li>
	<li>{% equation %}\varphi\left(c\right)\to\exists x\varphi\left(x\right){% endequation %} (MP על 4,5).</li>
</ol>
וזה <strong>מסיים את ההוכחה</strong>! רק שכמובן, זה לא מסיים את הוכחת משפט השלמות של גדל; זה מסיים את ההוכחה לכך שאם יש לנו תורה {% equation %}\Phi{% endequation %} שהיא עקבית מקסימלית וקיימת לה קבוצת עדים, אז יש לה מודל. עוד נשאר לנו להוכיח שכל תורה עקבית אפשר להרחיב לתורה שכזו, ואת זה נעשה בפוסט הבא.

כעת אפשר לחשוב על האופן שבו ההוכחה מתקלקלת (או הופכת לפשוטה יותר) אם שוויון הוא לא חלק מהלוגיקה שלנו. כדאי להעיר שאנחנו <strong>רוצים</strong> שוויון בלוגיקה שלנו מהרבה סיבות ולכן גם אם הוספת שוויון רק מקשה עלינו חבל לוותר עליו. עדיין, מבחינה רעיונית אולי פשוט יותר להציג קודם כל את ההוכחה עבור לוגיקה ללא שוויון כדי להימנע מיחסי שקילות ואקשן שכזה; מצד שני, במקרה הזה לא מספיק לבנות את המודל מתוך הקבועים של {% equation %}C{% endequation %} - <strong>כל שם עצם</strong> של השפה שלנו יהיה חייב להיות איבר בעולם של המודל. לי זה מרגיש מעט יותר מלאכותי, כאמור, אבל כל אחד ואיך שנוח לו. גם כך וגם כך הרעיון הזה, של בניה של המודל (האובייקט הסמנטי) מתוך השפה עצמה (האובייקט הסינטקטי) הוא אחד מהרעיונות החביבים עלי במתמטיקה.