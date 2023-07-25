---
title: "בעקבות השערת הרצף, חלק ב': האקסיומות של צרמלו-פרנקל"
layout: post
categories:
  - תורת הקבוצות
tags:
  - השערת הרצף
image: "/assets/img/main/forcing.png"
---

המטרה שלנו בסדרת הפוסטים הנוכחית היא להוכיח שהשערת הרצף היא בלתי תלויה במערכת האקסיומות ZFC, אז כדאי שנתחיל עם הצגה מסודרת של ZFC. אני מניח שהמוטיבציה כבר ברורה כי דיברתי עליה מספיק, אז בואו ניגש לפורמליזם.

ראשית כל, ZFC היא מה שנקרא <strong>תורה מסדר ראשון</strong>. הסברתי את זה לא מזמן <a href="https://gadial.net/2023/01/18/classes_and_transfinite/">כשדיברתי על מחלקות</a>, אבל הנה עוד תזכורת זריזה, פורמלית יותר: באופן כללי, שפה מסדר ראשון נבנית כוללת אוסף של סימנים עבור <strong>יחסים</strong> {% equation %}R_{1},R_{2},\ldots,R_{n}{% endequation %}, עבור <strong>פונקציות</strong> ועבור <strong>קבועים</strong>, אבל במקרה של ZFC אין שימוש בסימני פונקציה או <strong>קבועים</strong> וזה מפשט משמעותית עניינים מסויימים, כך שלא אכנס להגדרות הנוספות שקשורות ליצורים הללו (<a href="https://gadial.net/2012/06/17/first_order_logic/">הנה פוסט שלי</a> על לוגיקה מסדר ראשון כללית, לסקרניות).

אל סימני היחסים אנחנו מצרפים עוד דברים: קבוצה אינסופית בת מניה של סימנים עבור <strong>משתנים</strong>, וסימנים של <strong>קשרים לוגיים</strong> {% equation %}\neg,\wedge,\vee,\to,\leftrightarrow{% endequation %} <strong>וכמתים לוגיים</strong> {% equation %}\forall,\exists{% endequation %} וסימנים לסוגריים. מכל אלו בונים <strong>נוסחאות</strong> על פי ההגדרה הרקורסיבית הבאה:

<ul> <li>אם {% equation %}R{% endequation %} הוא סימן יחס עם {% equation %}n{% endequation %} מקומות ו-{% equation %}x_{1},\ldots,x_{n}{% endequation %} הם משתנים כלשהם (לאו דווקא {% equation %}n{% endequation %} המשתנים הראשונים בקבוצת המשתנים שלנו; כל אוסף של {% equation %}n{% endequation %} משתנים), אז {% equation %}R\left(x_{1},\ldots,x_{n}\right){% endequation %} היא נוסחה. נוסחאות שנבנות כך נקראות <strong>נוסחאות אטומיות</strong> כי הן הסוג הבסיסי ביותר של נוסחה - זה שלא ניתן לחלק אותו עוד ועדיין לקבל נוסחה.</li>


<li>אם {% equation %}\varphi,\psi{% endequation %} הן נוסחאות אז {% equation %}\left(\neg\varphi\right),\left(\varphi\wedge\psi\right),\left(\varphi\vee\psi\right),\left(\varphi\to\psi\right),\left(\varphi\leftrightarrow\psi\right){% endequation %} הן נוסחאות.</li>


<li>אם {% equation %}\varphi{% endequation %} היא נוסחה ו-{% equation %}x{% endequation %} הוא משתנה אז {% equation %}\left(\forall x\varphi\right){% endequation %} ו-{% equation %}\left(\exists x\varphi\right){% endequation %} הן נוסחאות.</li>

</ul>

אני כותב פה סוגריים כי הן הכרחיות לצורך זה שתהיה דרך אחת ויחידה לקרוא נוסחה, אבל לרוב אני אשמיט אותן אם אין בהן צורך.

בשפה של ZFC יש שני סימני יחס: {% equation %}\in{% endequation %} ו-{% equation %}={% endequation %}. הסימן {% equation %}={% endequation %} באופן כללי בשפות מסדר ראשון הוא מיוחד; אסביר את זה כשנדבר על הסמנטיקה של נוסחאות, מה שיקרה בהמשך. עוד דבר שיהיה ברור יותר בהמשך הוא למה קוראים לשפה כזו "מסדר ראשון" ומה זה סדר גבוה יותר; הכוונה היא שהכמתים {% equation %}\forall,\exists{% endequation %} מתייחסים לאיברים ספציפיים, לא <strong>לאוספים</strong> של איברים (זה מבלבל במיוחד בהקשר שלנו כי "איבר" הוא קבוצה, וגם "אוסף של איברים" הוא קבוצה, אז אני אתן דוגמא שאני מקווה שתקל על העניין).

הגדרה אחת אחרונה היא של משתנה חופשי ומשתנה קשור. לא פורמלית, משתנה הוא <strong>חופשי</strong> בתוך נוסחה מסויימת אם הוא לא נופל תחת כמת עבורו בתוך הנוסחה, ו<strong>קשור</strong> אם הוא לא חופשי. למשל בנוסחה {% equation %}\forall x\left(x=y\right){% endequation %} המשתנה {% equation %}y{% endequation %} הוא חופשי (כי הוא נופל רק תחת הכמת {% equation %}\forall x{% endequation %} שמיועד עבור {% equation %}x{% endequation %} ולא עבורו והמשתנה {% equation %}x{% endequation %} הוא קשור.

אם {% equation %}\varphi{% endequation %} היא נוסחה אטומית, המשתנים שמופיעים בה כולם חופשיים. המשתנים החופשיים בנוסחאות כמו {% equation %}\left(\neg\varphi\right),\left(\varphi\wedge\psi\right),\left(\varphi\vee\psi\right),\left(\varphi\to\psi\right),\left(\varphi\leftrightarrow\psi\right){% endequation %} הם המשתנים החופשיים של {% equation %}\varphi,\psi{% endequation %}. לעומת זאת, המשתנים החופשיים של {% equation %}\left(\forall x\varphi\right){% endequation %} ושל {% equation %}\left(\exists x\varphi\right){% endequation %} הם המשתנים החופשיים של {% equation %}\varphi{% endequation %} למעט {% equation %}x{% endequation %} אם הוא הופיע במשתנים החופשיים הללו.

לבסוף, אנחנו אומרים על נוסחה שהיא <strong>פסוק</strong> אם אין בה משתנים חופשיים. הסיבה שזו סיטואציה מעניינת היא שערך האמת של פסוק לא תלוי בהשמה ספציפית למשתנים שלו; מרגע שקבענו מה הקונטקסט (מה ה"יקום" שממנו נלקחים איברים ומה המשמעות של סימן היחס {% equation %}\in{% endequation %}) ערך האמת של הפסוק נקבע באופן יחיד. כל האקסיומות שאנחנו הולכים לנסח יהיו פסוקים, כי הרעיון הוא שמרגע שקבענו יקום מתמטי אנחנו יכולים להגיד האם הוא מקיים את ZFC או לא מקיים את ZFC; זה לא משהו שאמור להיות תלוי בהשמה מסויימת למשתנים.

עכשיו אפשר לנסח את אקסיומות ZFC. כולן, עד לאחרונה שבהן. אני קודם אתן לכל אחת תיאור מילולי, ואחר כך אציג את כולן ברמה הפורמלית. הדבר היחיד שקריטי לזכור הוא שב-ZFC <strong>כל האיברים הם קבוצות</strong>. לכן אם אני אומר "קבוצה {% equation %}X{% endequation %}" אין לי צורך לומר "קבוצה {% equation %}X{% endequation %} שכל אבריה הן קבוצות". בהמשך נבין באיזה מובן האקסיומות אכן גורמות לכך שכל האיברים יהיו קבוצות.

<ul> <li>(היקפיות): אם לשתי קבוצות יש את אותם איברים, הן שוות.</li>


<li>(זיווג) לכל שתי קבוצות {% equation %}x,y{% endequation %} קיימת הקבוצה {% equation %}\left\{ x,y\right\} {% endequation %}.</li>


<li>(איחוד) לכל קבוצה {% equation %}X{% endequation %} קיימת הקבוצה {% equation %}\bigcup X{% endequation %}.</li>


<li>(קבוצת החזקה): לכל קבוצה {% equation %}x{% endequation %}, הקבוצה {% equation %}\mathcal{P}\left(x\right){% endequation %} של כל תתי הקבוצות של {% equation %}x{% endequation %} קיימת.</li>


<li>(יסוד): לכל קבוצה לא ריקה קיים איבר מינימלי ביחס ל-{% equation %}\in{% endequation %}.</li>


<li>(אינסוף): קיימת קבוצה {% equation %}x{% endequation %} כך ש-{% equation %}\emptyset\in x{% endequation %} ואם {% equation %}y\in x{% endequation %} אז גם {% equation %}y\cup\left\{ y\right\} \in x{% endequation %}.</li>


<li>(סכמת ההפרדה): לכל קבוצה {% equation %}x{% endequation %} תת-הקבוצה של האיברים {% equation %}u\in x{% endequation %} שעבורם {% equation %}\varphi{% endequation %} מתקיים קיימת.</li>


<li>(סכמת ההחלפה): לכל {% equation %}x{% endequation %}, אם {% equation %}\varphi\left(u,v\right){% endequation %} שמצומצמת ל-{% equation %}x{% endequation %} היא פונקציה {% equation %}x{% endequation %} אז הקבוצה {% equation %}\varphi\left(x\right){% endequation %} קיימת.</li>


<li>(בחירה): לכל אוסף {% equation %}X{% endequation %} של קבוצות לא ריקות קיימת פונקציית בחירה: {% equation %}f:X\to\bigcup X{% endequation %} כך ש-{% equation %}f\left(a\right)\in a{% endequation %} לכל {% equation %}a\in X{% endequation %}.</li>

</ul>

נקודה אחת שצריך לשים לב אליה כבר עכשיו: סכמת ההפרדה וסכמת ההחלפה הן לא אקסיומות בודדות; הן <strong>סכמות</strong>, כלומר הן אוסף אינסופי של אקסיומות, אחת לכל נוסחה {% equation %}\varphi{% endequation %} אפשרית. בסכמת ההפרדה אנחנו מניחים שב-{% equation %}\varphi{% endequation %} יש משתנה חופשי יחיד ובסכמת ההחלפה אנחנו מניחים שב-{% equation %}\varphi{% endequation %} יש שני משתנים חופשיים, אבל זהו; לכל נוסחה שמתאימה כך לאחת מהסכמות קיימת אקסיומה ב-ZFC.

עכשיו אפשר לראות את הניסוח הפורמלי עד הסוף. כדי לעשות אותו קצת קל יותר לקריאה אני אשתמש במשתנים {% equation %}A,B{% endequation %} כדי לתאר קבוצות, {% equation %}x,y,z{% endequation %} כדי לתאר "איברים של קבוצות" (שהם בעצמם קבוצות כמובן) ו-{% equation %}\mathcal{F}{% endequation %} כדי לתאר "משפחה של קבוצות" (שגם היא קבוצה, כמובן).

<ul> <li>(היקפיות): {% equation %}\forall A\forall B\left(\forall x\left(x\in A\leftrightarrow x\in B\right)\to A=B\right){% endequation %}</li>


<li>(זיווג): {% equation %}\forall x\forall y\exists A\left(x\in A\wedge y\in A\right){% endequation %}</li>


<li>(איחוד): {% equation %}\forall\mathcal{F}\exists X\left(\forall A\forall x\left(\left(A\in\mathcal{F}\wedge x\in A\right)\to x\in X\right)\right){% endequation %}</li>


<li>(קבוצת החזקה): {% equation %}\forall A\exists X\forall B\left(\forall x\left(x\in B\to x\in A\right)\to B\in X\right){% endequation %}</li>

</ul>

עד עכשיו הפורמליזציה הייתה די פשוטה, אבל כבר בקבוצת החזקה אפשר להרגיש שהסימונים מתחילים להסתרבל לנו. דרך מקוצרת לכתוב את אקסיומת קבוצת החזקה היא על ידי

{% equation %}\forall A\exists X\forall B\left(B\subseteq A\to B\in X\right){% endequation %}

כאשר {% equation %}B\subseteq A{% endequation %} הוא <strong>סימון לא פורמלי</strong>, כלומר, הסימן {% equation %}\subseteq{% endequation %} הוא לא סימן יחס, הוא פשוט כתיב מקוצר; אנחנו כותבים {% equation %}B\subseteq A{% endequation %} במקום לכתוב את הנוסחה {% equation %}\forall x\left(x\in B\to x\in A\right){% endequation %} שהופיעה קודם. נזדקק לגישה המקוצרת הזו אם לא נרצה להשתגע כשיגיע הזמן לנסח את אקסיומת האינסוף, למשל.

נקודה אחרת שצריך לשים לב אליה הוא שאקסיומות הזיווג, האיחוד וקבוצת החזקה, בהגדרה הפורמלית שלהן, <strong>לא</strong> אומרות שהקבוצות שהן מיועדות להבטיח את קיומן אכן קיימות. הן רק מראות שקיימת קבוצה <strong>שמכילה</strong> אותן. למשל, אקסיומת הזיווג אומרת שקיימת {% equation %}A{% endequation %} שמכילה גם את {% equation %}x{% endequation %} וגם את {% equation %}y{% endequation %}; היא לא אומרת ש-{% equation %}A=\left\{ x,y\right\} {% endequation %}, ולא שוללת את האפשרות שיש ב-{% equation %}A{% endequation %} עוד איברים. זה מכוון, כי עכשיו אפשר להכניס לתמונה את סכמת אקסיומת ההפרדה.

בואו ננסח את אקסיומת ההפרדה הכי פורמלי שאפשר. ניקח נוסחה {% equation %}\varphi\left(u,p_{1},\ldots,p_{n}\right){% endequation %} <strong>כלשהי</strong> כך שהמשתנים החופשיים שלה שייכים לקבוצה {% equation %}\left\{ x,p_{1},\ldots,p_{n}\right\} {% endequation %}. קונספטואלית אנחנו חושבים על {% equation %}p_{1},\ldots,p_{n}{% endequation %} בתור משתנים שמגדירים <strong>פרמטרים</strong> ועל {% equation %}x{% endequation %} בתור המשתנה שמקבל את האיברים שבודקים את שייכותם לתת-הקבוצה שאקסיומת ההפרדה בונה. עכשיו אפשר לעבור לאקסיומה עצמה:

<ul> <li>(סכמת אקסיומת ההפרדה): {% equation %}\forall A\forall p_{1}\ldots\forall p_{n}\exists B\forall x\left(x\in B\leftrightarrow x\in A\wedge\varphi\right){% endequation %}</li>

</ul>

כלומר, בהינתן קבוצה {% equation %}A{% endequation %} והשמה כלשהי של ערכים לפרמטרים, קיימת קבוצה {% equation %}B{% endequation %} שכל איבריה הם בדיוק האיברים של {% equation %}A{% endequation %} שעל הדרך גם מספקים את {% equation %}\varphi{% endequation %} עם הפרמטרים הנתונים.

בואו נשתמש בזה כדי לייצר את הקבוצות של אקסיומות הזיווג/איחוד/קבוצת החזקה. עבור הזיווג, נשתמש בנוסחה {% equation %}z=x\vee z=y{% endequation %} (כאשר כאן {% equation %}z{% endequation %} הוא המשתנה שמייצג את האיבר שאנחנו "מסננים" מתוך {% equation %}A{% endequation %}) - הנוסחה הזו מבטיחה שהאיבר שאנחנו מסננים יהיה או {% equation %}x{% endequation %} או {% equation %}y{% endequation %} ושום דבר פרט אליהם.

עבור איחוד הקבוצות ששייכות ל-{% equation %}X{% endequation %}, נשתמש בנוסחה {% equation %}\exists A\left(A\in X\wedge z\in A\right){% endequation %} שמבטיחה שנסנן רק איברים שנמצאים באחת מהקבוצות ב-{% equation %}X{% endequation %}. ועבור קבוצת החזקה, נשתמש בנוסחה {% equation %}\exists B\left(B\subseteq A\wedge z\in B\right){% endequation %} (כאן השתמשנו שוב ב-{% equation %}\subseteq{% endequation %} בתור קיצור לנוסחה מורכבת יותר).

אם כבר הצגתי סכמת אקסיומות אחת, למה לא להציג את השניה, סכמת אקסיומת ההחלפה? כזכור, אקסיומת ההחלפה מניחה שאנחנו עובדים עם נוסחה {% equation %}\varphi{% endequation %} שמייצגת <strong>פונקציה</strong>: זה אומר שהיא מקבלת שני קלטים, ואולי פרמטרים נוספים: {% equation %}\varphi\left(x,y,p_{1},\ldots,p_{n}\right){% endequation %}. הדרישה היא שלכל {% equation %}x{% endequation %} יהיה קיים {% equation %}y{% endequation %} <strong>יחיד</strong> שעבורו {% equation %}\varphi\left(x,y,p_{1},\ldots,p_{n}\right){% endequation %} מתקיים. אפשר לנסח את זה יחסית בקלות כנוסחה:

{% equation %}\exists y\varphi\left(x,y,p_{1},\ldots,p_{n}\right)\wedge\left(\forall z\varphi\left(x,z,p_{1},\ldots,p_{n}\right)\to z=y\right){% endequation %}

את הנוסחה הזו אני אסמן בצורה מקוצרת בתור {% equation %}\exists!y\varphi\left(x,y,p_{1},\ldots,p_{n}\right){% endequation %}.

עוד דבר ששווה לכתוב בצורה מקוצרת הוא הגבלה של כמת כך שירוץ רק על אברי קבוצה מסוימת. אני ארצה לכתוב דבר כזה בתור {% equation %}\forall x\in A\left(\psi\right){% endequation %} או {% equation %}\exists x\in A\left(\psi\right){% endequation %}. הראשון הוא סימון מקוצר עבור {% equation %}\forall x\left(x\in A\to\psi\right){% endequation %} והשני עבור {% equation %}\exists x\left(x\in A\wedge\psi\right){% endequation %}.

כל אלו יקלו עלינו לכתוב את סכמת אקסיומת ההחלפה:

<ul> <li>(סכמת אקסיומת ההחלפה): {% equation %}\forall A\forall p_{1}\ldots\forall p_{n}\left(\forall x\in A\exists!y\varphi\to\exists B\forall x\in A\exists y\in B\varphi\right){% endequation %}</li>

</ul>

גם כאן, שימו לב שזה לא מוכיח באופן ישיר שהקבוצה {% equation %}\varphi\left(A\right){% endequation %} קיימת; רק שקיימת קבוצה שמכילה את {% equation %}\varphi\left(A\right){% endequation %} ואפשר לקבל אותה בעזרת אקסיומת ההפרדה.

נשארנו עם שלוש אקסיומות, המורכבות ביותר לניסוח פורמלי: יסוד, אינסוף, ובחירה.

בואו נתחיל מאקסיומת היסוד. באופן לא פורמלי היא אומרת "לכל קבוצה לא ריקה קיים איבר מינימלי ביחס ל-{% equation %}\in{% endequation %}". כלומר, לכל קבוצה {% equation %}A{% endequation %}, אם {% equation %}A\ne\emptyset{% endequation %}, אז קיימת {% equation %}B\in A{% endequation %} כך ש... מה? איך מנסחים את "{% equation %}B{% endequation %} מינימלית ביחס ל-{% equation %}\in{% endequation %}"? זה נראה לי מפחיד בהתחלה אבל זה בעצם די פשוט: אם {% equation %}B{% endequation %} <strong>אינה</strong> מינימלית ביחס ל-{% equation %}\in{% endequation %} זה אומר שקיימת ב-{% equation %}A{% endequation %} קבוצה נוספת, {% equation %}C\in A{% endequation %}, כך ש-{% equation %}C\in B{% endequation %}; הרי המשמעות של "{% equation %}b{% endequation %} הוא איבר מינימלי" בהקשר של יחס סדר {% equation %}\le{% endequation %} היא שאין {% equation %}c{% endequation %} כך ש-{% equation %}c\le b{% endequation %}; זה בדיוק מה שמדובר עליו פה. עכשיו, אם הייתה קיימת {% equation %}C{% endequation %} כזו כך ש-{% equation %}C\in A{% endequation %} וגם {% equation %}C\in B{% endequation %}, אז היה מתקיים {% equation %}C\in B\cap A{% endequation %}; זה מה שאני הולך להשתמש בו.

אם כן, בכתיב פורמלי, אפשר לתאר את האקסיומה כך:

<ul> <li>(אקסיומת היסוד): {% equation %}\forall A\left(A\ne\emptyset\to\exists B\left(B\in A\wedge B\cap A=\emptyset\right)\right){% endequation %}</li>

</ul>

זה כתיב פורמלי, אבל עם סימונים מקוצרים שצריך להסביר איך כותבים בצורה מלאה. ראשית, {% equation %}A\ne\emptyset{% endequation %} זו הנוסחה {% equation %}\exists x\left(x\in A\right){% endequation %}. שנית, {% equation %}B\cap A=\emptyset{% endequation %} זו הנוסחה {% equation %}\neg\exists x\left(x\in B\wedge x\in A\right){% endequation %}.

את אקסיומת האינסוף כבר ניסחנו בצורה המפורשת שלה - במקום לומר "קיימת קבוצה אינסופית", אמרנו "קיימת קבוצה {% equation %}x{% endequation %} כך ש-{% equation %}\emptyset\in x{% endequation %} ואם {% equation %}y\in x{% endequation %} אז גם {% equation %}y\cup\left\{ y\right\} \in x{% endequation %}". מכאן הפורמליזציה מגיעה מעצמה:

<ul> <li>(אקסיומת האינסוף): {% equation %}\exists A\left(\emptyset\in A\wedge\forall x\left(x\in A\to x\cup\left\{ x\right\} \in A\right)\right){% endequation %}</li>

</ul>

גם כאן השתמשתי בקיצורים. ראשית, {% equation %}\emptyset\in A{% endequation %} הוא קיצור ל-{% equation %}\exists y\left(\forall z\neg\left(z\in y\right)\wedge y\in A\right){% endequation %}. שנית, {% equation %}x\cup\left\{ x\right\} \in A{% endequation %} זה קיצור ל-{% equation %}\exists y\left(y\in A\wedge\forall z\left(z\in y\leftrightarrow\left(z=x\vee z\in x\right)\right)\right){% endequation %}.

נשארה רק אקסיומת הבחירה, שאותה אני <strong>באמת</strong> מפחד מלכתוב פורמלי; אולי אפשר פשוט להגיד שקיים לה כתיב פורמלי וזהו? למה הכל חייב להיות קונסטרוקטיבי?

טוב, האמת היא שלא באמת צריך לכתוב את זה פורמלי - תפתחו ספר אקראי בתורת הקבוצות האקסיומטית ותראו שהם לא טורחים לעשות את זה. אפשר גם אולי לנסות לנסח את אקסיומת הבחירה בעזרת ניסוח של עקרון הסדר הטוב או הלמה של צורן ששקולות אליה. אבל אפשר גם פשוט לכתוב את זה:

<ul> <li>(אקסיומת הבחירה): {% equation %}\forall A\left(\emptyset\notin A\to\exists f:A\to\bigcup A\forall a\in A\left(f\left(a\right)\in a\right)\right){% endequation %}</li>

</ul>

כאן הקיצורים באמת קשים לניסוח פורמלי. ב-{% equation %}\emptyset\notin A{% endequation %} קל לטפל, כי זה בסך הכל {% equation %}a\in A\to\exists b\left(b\in a\right){% endequation %}. אבל קיום של פונקציה {% equation %}f{% endequation %}? פונקציה היא קבוצה של זוגות סדורים שמקיימת כל מני תנאים. צריך קיצורים בתוך הקיצורים. בואו נפרוט את זה צעד-צעד.

ראשית, מופיע שם {% equation %}\bigcup A{% endequation %} וזה מסבך אותי. אז נוסיף לפסוק את {% equation %}\exists X\left(\forall B\forall b\left(B\in A\wedge b\in B\right)\to b\in X\right){% endequation %} - די דומה לאקסיומת האיחוד שכבר ראינו. אחרי שהוספנו את הנוסחה הזו לפסוק, במקום לכתוב {% equation %}\bigcup A{% endequation %} אפשר לכתוב את {% equation %}X{% endequation %} וזהו. אז כשאני בא לכתוב את {% equation %}\exists f:A\to\bigcup A{% endequation %} אני אראה איך במקום זה כותבים פסוק עבור {% equation %}\exists f:A\to B{% endequation %} עם {% equation %}A,B{% endequation %} כלליים.

ה-{% equation %}f:A\to B{% endequation %} אומר בעצם שלושה דברים:

<ul> <li>{% equation %}f{% endequation %} היא קבוצה של זוגות סדורים {% equation %}\left(a,b\right){% endequation %} כך ש-{% equation %}a\in A{% endequation %} ו-{% equation %}b\in B{% endequation %}.</li>


<li>לכל {% equation %}a\in A{% endequation %} קיים {% equation %}b\in B{% endequation %} כך ש-{% equation %}\left(a,b\right)\in f{% endequation %}.</li>


<li>לכל {% equation %}a\in A{% endequation %} ולכל {% equation %}b_{1},b_{2}\in B{% endequation %}, אם מתקיים {% equation %}\left(a,b_{1}\right)\in f{% endequation %} וגם {% equation %}\left(a,b_{2}\right)\in f{% endequation %} אז {% equation %}b_{1}=b_{2}{% endequation %}.</li>

</ul>

התנאים הללו הם קלים יחסית לניסוח פורמלי, בהינתן שאנחנו יודעים לתאר זוגות סדורים:

<ul> <li>{% equation %}\forall a\forall b\left(\left(a,b\right)\in f\to\left(a\in A\wedge b\in B\right)\right){% endequation %}</li>


<li>{% equation %}\forall a\left(a\in A\to\exists b\left(b\in B\wedge\left(a,b\right)\in f\right)\right){% endequation %}</li>


<li>{% equation %}\forall a\forall b_{1}\forall b_{2}\left(\left(\left(a,b_{1}\right)\in f\wedge\left(a,b_{2}\right)\in f\right)\to b_{1}=b_{2}\right){% endequation %}</li>

</ul>

וגם קל לתאר את {% equation %}f\left(a\right)\in a{% endequation %} בהינתן שאנחנו יודעים לתאר זוגות סדורים:

<ul> <li>{% equation %}\exists b\left(\left(a,b\right)\in f\wedge b\in a\right){% endequation %}</li>

</ul>

אז מה שנשאר לי לעשות הוא להסביר איך לתאר משהו כמו {% equation %}\left(a,b\right)\in f{% endequation %}. זה תלוי באופן שבו אנחנו בונים זוגות סדורים מלכתחילה; הבניה הסטנדרטית, <a href="https://gadial.net/2019/10/19/what_is_set_theory/">שהראיתי כבר כאן</a>, היא {% equation %}\left(a,b\right)\triangleq\left\{ \left\{ a\right\} ,\left\{ a,b\right\} \right\} {% endequation %}. אז בתור {% equation %}\left(a,b\right)\in f{% endequation %} אפשר לכתוב

<ul> <li>{% equation %}\exists A\left(A\in f\wedge A=\left\{ \left\{ a\right\} ,\left\{ a,b\right\} \right\} \right){% endequation %}</li>

</ul>

אבל איך אני כותב ביטוי כמו {% equation %}A=\left\{ \left\{ a\right\} ,\left\{ a,b\right\} \right\} {% endequation %} פורמלית? הנה בעיה קצת יותר כללית: איך אני כותב {% equation %}A=\left\{ a_{1},\ldots,a_{n}\right\} {% endequation %}, עבור קבוצה סופית {% equation %}A{% endequation %} כלשהי? פשוט מאוד:

<ul> <li>{% equation %}a_{1}\in A\wedge\ldots\wedge a_{n}\in A\wedge\forall b\left(b\in A\to\left(b=a_{1}\vee\ldots\vee b=a_{n}\right)\right){% endequation %}</li>

</ul>

כלומר: {% equation %}A{% endequation %} מכילה את כל האיברים {% equation %}a_{1},\ldots,a_{n}{% endequation %} ואם היא מכילה איבר כלשהו, הוא אחד מהם. השתמשתי בשלוש נקודות בתור קיצור כאן, כי פסוקים שונים נכתבים שונה בהתאם למספר האיברים של {% equation %}A{% endequation %}, אבל כל עוד {% equation %}A{% endequation %} סופית אפשר לכתוב פסוק כזה במפורש.

בהינתן שאנחנו יודעים לכתוב פסוק כזה, ברור איך לממש את {% equation %}A=\left\{ \left\{ a\right\} ,\left\{ a,b\right\} \right\} {% endequation %}:

<ul> <li>{% equation %}\exists B\exists C\left(B=\left\{ a\right\} \wedge C=\left\{ a,b\right\} \wedge A=\left\{ B,C\right\} \right){% endequation %}</li>

</ul>

שמשתמש בבניה הזו שלוש פעמים. אם ננסה לכתוב במפורש את הנוסחה של אקסיומת הבחירה היא תהיה ארוכה להחריד, אבל למרבה המזל אנחנו לא צריכים את זה.

אם כן - זהו, סיימנו! הצגנו בצורה הכי פורמלית שאפשר את ZFC, מה שייתן לנו תירוץ מעכשיו קצת לחפף בפורמליזם כי אנחנו מבינים איך עושים אותו ושזה אפשרי, וגם שאם מנסים לעשות את זה עד הסוף זה כואב ממש.

לאן הולכים עכשיו? השלב הראשון יהיה להציג באופן פורמלי את הרעיון של צמצום היקום של תורת הקבוצות לכדי "תת-יקום" כלשהו {% equation %}\mathcal{M}{% endequation %} ש-ZFC מתקיימת גם בו במובן מסוים - רעיון שנקרא <strong>רלטיביזציה</strong>. את זה נראה בפוסט הבא. 