---
title: "תורת הקבוצות - מחלקות, אקסיומת ההחלפה ואינדוקציה ורקורסיה על-סופיות"
layout: post
categories:
  - תורת הקבוצות
tags:
  - סודרים
image: "/assets/img/main/set_theory.png"
---


<h2>מה זו מחלקה ולמה זו לא רמאות</h2>

<a href="https://gadial.net/2023/01/14/ordinal_arithmetic/">בפוסט הקודם</a> הצגתי את ההגדרות לאריתמטיקה של סודרים. הכל היה (בתקווה) די פשוט ואינטואיטיבי, אבל הזהרתי שאני לא פורמלי עד הסוף, כי ההגדרה שלי הייתה רקורסיבית ולא נתתי עדיין נימוק למה "מותר" להשתמש בהגדרות כאלו. בפוסט הזה אני רוצה לדבר על הגדרות רקורסיביות, ועל הוכחות באינדוקציה שדרושות בשבילן ובשביל שלל דברים נוספים, בהקשר של הסודרים. בהקשר הזה קוראים להן "אינדוקציה על-סופית" ו"רקורסיה על-סופית" (Transfinite באנגלית). אלא שאי אפשר לדבר על הדברים הללו בלי להגיע סוף סוף לעניין קצת מלוכלך שטאטאתי עד כה מתחת לשטיח כי העדפתי לא להסביר בלי דוגמא צמודה, והגענו בדיוק אל הדוגמא הזו. המשהו המלוכלך זה מה שנקרא <strong>מחלקות</strong>, ובשמיעה ראשונה עליו יכול להישמע כמו רמאות גדולה במיוחד, ודי קריטי שנבין למה זו לא רמאות לפני שנמשיך.

כבר <a href="https://gadial.net/2019/10/19/what_is_set_theory/">כשהתחלתי לדבר</a> על תורת הקבוצות הצגתי את <strong>הפרדוקס של ראסל</strong>. הפרדוקס הזה מלמד אותנו שאי אפשר סתם לקרוא בשם "קבוצה" לכל אוסף של איברים; אינטואיטיבית, יש אוספים שהם גדולים מדי מכדי להיחשב קבוצות, וההנחה שהן קבוצות מובילה לפרדוקסים. כפועל יוצא מכך הגיעו אקסיומות צרמלו-פרנקל שמדברות בדיוק על איך נראות קבוצות ואיך אפשר לבנות אותן זו מזו.

עכשיו, בואו נסתכל על אוסף כל הסודרים, שאני מכנה {% equation %}\text{Ord}{% endequation %}. האם הוא קבוצה? ובכן, ראינו בפוסט מוקדם יותר שאם יש לנו קבוצה {% equation %}A{% endequation %} של סודרים, גם {% equation %}\bigcup A{% endequation %} היא סודר. כלומר, גם {% equation %}\bigcup\text{Ord}{% endequation %} צריך להיות סודר. אבל אם הוא סודר, יש לו עוקב, {% equation %}\bigcup\text{Ord}+1{% endequation %}. מכיוון שגם העוקב הזה הוא סודר, הוא שייך לקבוצת כל הסודרים, {% equation %}\text{Ord}{% endequation %}, ולכן נקבל {% equation %}\bigcup\text{Ord}+1\in\text{Ord}\subseteq\bigcup\text{Ord}{% endequation %}, כלומר {% equation %}\bigcup\text{Ord}+1<\bigcup\text{Ord}{% endequation %} ומצד שני {% equation %}\bigcup\text{Ord}<\bigcup\text{Ord}+1{% endequation %} וזה כמובן בלתי אפשרי. קיבלנו סתירה בסגנון הפרדוקס של ראסל שמראה לנו ש-{% equation %}\text{Ord}{% endequation %} לא יכול להיות קבוצה. אז מה הוא <strong>כן</strong>?

ובכן, אנחנו קוראים לאוסף הזה <strong>מחלקה</strong> (Class). זה השם ה"רשמי" שלנו כדי לתאר אוסף <strong>שאנחנו מסוגלים לתאר</strong> אבל הוא לא בהכרח קבוצה בעצמו (משתמשים ב-Proper Class כדי לתאר מחלקה שאכן איננה קבוצה, ואני ככל הנראה אשתמש חופשי ב"מחלקה" כדי לומר "מחלקה שאיננה קבוצה"). מה זאת אומרת "מסוגלים לתאר", בעזרת מה? בלי להסביר את זה בצורה הכי מדוקדקת שאפשר זה נשמע כאילו אני מרמה. התשובה היא - בעזרת <strong>לוגיקה מסדר ראשון</strong>. ספציפית, בעזרת התורה מסדר ראשון של קבוצות.

<a href="https://gadial.net/2012/06/17/first_order_logic/">יש לי פוסטים</a> על לוגיקה מסדר ראשון, ולכן כאן אני אסתפק בתיאור קצר יחסית. האובייקט הבסיסי בלוגיקה מסדר ראשון הוא <strong>נוסחה</strong>, שהיא סדרה סופית של תווים. יש לנו תווים שמתארים <strong>משתנים</strong>, למשל {% equation %}x,y,z,A,B,C{% endequation %} וכדומה (אפשר להניח שיש לנו אינסוף כאלו). בין כל שני משתנים אפשר לכתוב אחד משני סימני יחס: או לכתוב {% equation %}x=y{% endequation %} או לכתוב {% equation %}x\in y{% endequation %}. שני הביטויים הללו הם <strong>נוסחאות הבסיס</strong> שלנו - כלומר, כל נוסחת בסיס {% equation %}\varphi{% endequation %} מורכבת משני משתנים עם אחד משני סימני היחס ביניהם. הרעיון בנוסחאות בסיס הוא שבהינתן <strong>השמה למשתנים</strong> כל נוסחת בסיס מקבלת ערך שהוא או "אמת", T או "שקר", F; אם שמנו במשתנה {% equation %}x{% endequation %} את הקבוצה {% equation %}a{% endequation %} ושמנו במשתנה {% equation %}y{% endequation %} את הקבוצה {% equation %}b{% endequation %}, אז הנוסחה {% equation %}x=y{% endequation %} מקבלת ערך "אמת" רק אם {% equation %}a,b{% endequation %} הן אותה קבוצה בדיוק, ו-{% equation %}x\in y{% endequation %} מקבלת ערך "אמת" רק אם הקבוצה {% equation %}a{% endequation %} היא איבר של הקבוצה {% equation %}b{% endequation %}.

מנוסחאות בסיס אפשר לבנות נוסחאות מורכבות יותר בעזרת <strong>קשרים לוגיים</strong>: {% equation %}\neg\varphi,\varphi\wedge\psi,\varphi\vee\psi,\varphi\to\psi,\varphi\leftrightarrow\psi{% endequation %}. הקשרים הללו הם פונקציות על ערכי אמת: {% equation %}\neg{% endequation %} ("שלילה") הופך T ל-F ו-F ל-T; {% equation %}\wedge{% endequation %} ("וגם") מחזיר T רק אם שני הקלטים היו T; {% equation %}\vee{% endequation %} ("או") מחזיר F רק אם שני הקלטים היו F, {% equation %}\to{% endequation %} ("גרירה") מחזיר F רק אם הקלט השמאלי היה T והימני היה F; ו-{% equation %}\leftrightarrow{% endequation %} ("שקילות") מחזיר T רק אם שני הקלטים שווים.

המרכיב האחרון בבניית נוסחת הוא <strong>כמתים</strong>. אם {% equation %}\varphi{% endequation %} היא נוסחה, אז גם {% equation %}\forall x\varphi{% endequation %} ("לכל {% equation %}x{% endequation %} מתקיים {% equation %}\varphi{% endequation %}") ו-{% equation %}\exists x\varphi{% endequation %} ("קיים {% equation %}x{% endequation %} שעבורו מתקיים {% equation %}\varphi{% endequation %}") הן נוסחאות. {% equation %}\forall x\varphi{% endequation %} מקבלת ערך T רק אם לכל קבוצה שמציבים במקום {% equation %}x{% endequation %} בנוסחה {% equation %}\varphi{% endequation %} מקבלים ערך T, ו-{% equation %}\exists x\varphi{% endequation %} מקבלת ערך T רק אם קיימת קבוצה שאם מציבים אותה במקום {% equation %}x{% endequation %} בנוסחה {% equation %}\varphi{% endequation %} מקבלים ערך T.

החלק המוזר בכל הסיפור הזה הוא האמירה שלי "קיימת קבוצה" כי אני לא מסביר - קיימת קבוצה <strong>איפה</strong>? וכאן הסיפור באמת מתחיל להסתבך. כשיש לי אוסף של נוסחאות מסדר ראשון, מה שאני קורא לו <strong>תורה</strong>, ואני בא להבין מה ערכי האמת של נוסחאות מסדר ראשון, צריך להתחיל עם <strong>פרשנות</strong> לסימונים שמופיעים בה. כאן אנחנו מניחים במובלע קיום של יקום מתמטי שממנו נלקחות הקבוצות שאפשר להציב בתוך המשתנים, אבל אנחנו לא יכולים לשלול את הקיום של <strong>כמה יקומים שונים</strong> כאלו, ובפרט לא לשלול את אפשרות הקיום של יקומי "צעצוע" שהם קטנים למדי ביחס ליקום המפלצתי שאנחנו חושבים עליו. למשל, אפשר לקחת בתור יקום מתמטי את {% equation %}\omega{% endequation %} עצמו; זה אומר שכל קבוצה שנציב במשתנים שלנו תהיה איבר של {% equation %}\omega{% endequation %} ושום דבר חוץ מזה. אם זה יהיה היקום שלנו, נראה מהר מאוד שבניסוח הפורמלי של אקסיומות צרמלו-פרנקל, כל האקסיומות מתקיימות יפה מאוד, למעט אחת: אקסיומת האינסוף. כלומר, מנקודת המבט הזו אקסיומת האינסוף לא מראה לנו שמשהו קיים, אלא <strong>שוללת פרשנות</strong> אפשרית אחת לתורה שלנו. זו דרך מאוד מועילה לחשוב על אקסיומות - בתור "פילטרים" שמסננים פרשנויות לא מתאימות של התורה שלנו. עוד נחזור לכל העניינים הללו בהמשך.

כרגע, אבל, אני לא מניח עוד הנחות על היקום המתמטי שלנו חוץ מזה שכל איבריו הם קבוצות. אני מסמן אותו ב-{% equation %}V{% endequation %} וחסל. כזכור, {% equation %}V{% endequation %} הזה לא יכול להיות קבוצה ("קבוצת כל הקבוצות" לא קיימת), אבל קל לתת נוסחה ש"מתארת" אותו: {% equation %}x=x{% endequation %}. הנוסחה הזו נכונה <strong>לכל</strong> איבר של {% equation %}V{% endequation %}, ולכן אפשר לתאר את {% equation %}V{% endequation %} בתור "אוסף כל האיברים שמקיימים {% equation %}x=x{% endequation %}", או אפילו להתחצף ולכתוב {% equation %}V=\left\{ x\ |\ x=x\right\} {% endequation %}. הכתיב הזה הוא חצוף משתי סיבות: ראשית, כי אני מערבב בין {% equation %}x{% endequation %} שהוא סימן של משתנה (מה שמופיע בנוסחה {% equation %}x=x{% endequation %}) ובין {% equation %}x{% endequation %} שהוא סימון של איבר קונקרטי של {% equation %}V{% endequation %} (מה שמופיע בצד שמאל) אבל זה לא נורא. מה שבאמת נורא הוא שאני משתמש בכתיב הסוגריים המסולסלים שמשמש אותנו להגדיר קבוצות, למרות ש-{% equation %}V{% endequation %} היא לא קבוצה. ומה ש<strong>הכי</strong> נורא זה שאני אשתמש בסימון כמו {% equation %}x\in V{% endequation %} כדי לתאר שייכות למחלקה. כל זה נראה לגמרי כאילו אני מתייחס למחלקות בתור קבוצות. אז למה זה בסדר? ובכן, כי כל מה שאני עושה עם מחלקות זה בסך הכל <strong>כתיב מקוצר</strong>. אני יכול להעלים את הכתיב המקוצר הזה ולהישאר במקומו עם נוסחאות לוגיות והכל יעבוד באותה מידה בדיוק.

בואו נראה דוגמא יותר קונקרטית - הסודרים. כשאני כותב {% equation %}\alpha\in\text{Ord}{% endequation %}, כלומר "{% equation %}\alpha{% endequation %} הוא סודר", למה אני מתכוון? אם נחזור להגדרה, סודר הוא קבוצה שהיא 1) טרנזיטיבית ו-2) סדורה בסדר מלא על ידי {% equation %}\in{% endequation %}. את שני אלו אפשר לנסח באמצעות נוסחה לוגית:

{% equation %}\forall\beta\forall\gamma\left(\left(\gamma\in\beta\wedge\beta\in\alpha\right)\to\gamma\in\alpha\right)\wedge\forall\beta\forall\gamma\left(\left(\beta\in\alpha\wedge\gamma\in\alpha\right)\to\left(\beta\in\gamma\vee\gamma\in\beta\right)\right){% endequation %}

במקום לכתוב את כל הנוסחה הזו, אפשר לכתוב פשוט {% equation %}\alpha\in\text{Ord}{% endequation %}; זה סימון מקוצר מוסכם. זה לא אומר ש-{% equation %}\text{Ord}{% endequation %} היא קבוצה; כלומר, זה לא אומר שיש איבר ביקום שהאיברים שלו הם בדיוק האיברים של {% equation %}\text{Ord}{% endequation %}. הטענה שיש כזה איבר מנוסחת כך:

{% equation %}\exists A\left(\alpha\in A\leftrightarrow\alpha\in\text{Ord}\right){% endequation %}

כאשר כאמור, ה-{% equation %}\alpha\in\text{Ord}{% endequation %} הוא פשוט העתק-הדבק של הנוסחה הגדולה מקודם. עכשיו, מה שראינו הוא שהנוסחה הזו של ה-{% equation %}\exists A{% endequation %} היא <strong>שקר</strong>, כלומר לא קיימת {% equation %}A{% endequation %} כזו. זו הסיבה שאנחנו אומרים ש-{% equation %}\text{Ord}{% endequation %} היא "מחלקה ממש".

מוזר? כן, אז בואו נעבור לראות עוד שימוש של המושג הזה. איך אמר ג'ון פון-נוימן? "במתמטיקה לא מבינים דברים, במתמטיקה מתרגלים לדברים". אחרי שמתרגלים גם קל יותר להבין.

<h2>אקסיומת ההחלפה</h2>

מבין כל האקסיומות של צרמלו-פרנקל שתיארתי בסדרת הפוסטים הזו, אקסיומת ההחלפה היא זו שהכי חיפפתי וטרם הצגתי בצורה פורמלית, למרות השימושיות הרבה שלה. סוף סוף הגיע הזמן להציג אותה פורמלית, אז כמובן שכדאי להתחיל מהצגה לא פורמלית: בהצגה הזו, אקסיומת ההחלפה אומרת שאם מחלקה {% equation %}F{% endequation %} היא פונקציה ו-{% equation %}A{% endequation %} היא קבוצה, אז {% equation %}F\left(A\right){% endequation %} היא קבוצה.

אבל רגע, מה זאת אומרת "מחלקה {% equation %}F{% endequation %} היא פונקציה"? הרי "פונקציה" הוגדרה בתור סוג של יחס, שהוא קבוצה. איך משהו שאיננו קבוצה יכול להיות פונקציה? אנחנו שוב מותחים את השימוש בשפה שלנו. מה שקורה בפועל הוא ש-{% equation %}F{% endequation %} כזו היא סימון מקוצר לנוסחה {% equation %}\varphi\left(x,y,a_{1},\ldots,a_{n}\right){% endequation %}. הכתיב הזה עם הסוגריים אומר "יש בנוסחה {% equation %}\varphi{% endequation %} את המשתנים החופשיים {% equation %}x,y,a_{1},\ldots,a_{n}{% endequation %}" כש"משתנה חופשי" הוא משתנה שלא נופל תחת הטווח של כמת עם השם שלו. למשל בנוסחה {% equation %}\forall x\left(x=y\right){% endequation %} המשתנה {% equation %}y{% endequation %} חופשי והמשתנה {% equation %}x{% endequation %} לא (אם ההגדרות הללו לא ברורות באמת שכדאי לקרוא קודם על לוגיקה מסדר ראשון, זה לא כזה קשה!)

בנוסחה {% equation %}\varphi\left(x,y,a_{1},\ldots,a_{n}\right){% endequation %} הזו אני חושב על {% equation %}x,y{% endequation %} בתור האיברים של הזוג ש-{% equation %}\varphi{% endequation %} מגדירה, ועל {% equation %}a_{1},\ldots,a_{n}{% endequation %} בתור "פרמטרים" שמאפיינים את {% equation %}\varphi{% endequation %}. למשל, הנוסחה שהמשתנים שלה הם רק {% equation %}x,y{% endequation %} (בלי פרמטרים)

{% equation %}x\in y\wedge\forall z\in x\left(z\in y\right)\wedge\forall z\in y\left(z=x\vee z\in x\right){% endequation %}

מה היא אומרת? ש-{% equation %}y=x\cup\left\{ x\right\} {% endequation %} (מה שעבור סודרים סימנתי ב-{% equation %}y=x+1{% endequation %} אבל כאן אנחנו עוסקים בקבוצות כלליות, לאו דווקא סודרים). כלומר, {% equation %}\varphi\left(x,y\right){% endequation %} מקבלת ערך T אם ורק אם {% equation %}y=x\cup\left\{ x\right\} {% endequation %}. אפשר גם לסמן את זה {% equation %}\left(x,y\right)\in F{% endequation %}, כפי שכבר עשיתי קודם עם מחלקות.

עכשיו, קל להוכיח שאם {% equation %}\varphi\left(x,y_{1}\right){% endequation %} מקבלת ערך T וגם {% equation %}\varphi\left(x,y_{2}\right){% endequation %} מקבלת ערך T (עבור הצבות קונקרטיות של קבוצות {% equation %}x,y_{1},y_{2}{% endequation %} למשתנים) אז {% equation %}y_{1}=y_{2}{% endequation %}; זו בדיוק התכונה שאנחנו דורשים מפונקציות. אז אפשר להשתמש בסימון {% equation %}F\left(x\right){% endequation %} כדי לציין את {% equation %}y{% endequation %}, ואפשר לכתוב {% equation %}F\left(x\right)=x\cup\left\{ x\right\} {% endequation %} ויהיה ברור אל מה הכוונה אפילו אם {% equation %}F{% endequation %} איננה קבוצה. ואם {% equation %}A{% endequation %} היא כן קבוצה, אני יכול לחשוב על הקבוצה {% equation %}F\left(A\right)=\left\{ F\left(a\right)\ |\ a\in A\right\} {% endequation %}, אבל "לחשוב על הקבוצה" לא מוכיח שהיא קיימת; בשביל זה אני צריך את אקסיומת ההחלפה.

פורמלית, אקסיומת ההחלפה היא לא אקסיומה בודדת, כלומר פסוק אחד ויחיד; יש לנו אקסיומת החלפה לכל נוסחה {% equation %}\varphi\left(x,y,a_{1},\ldots,a_{n}\right){% endequation %} אפשרית (לכן לפעמים מדברים על <strong>סכמת</strong> אקסיומת ההחלפה - מין תבנית כזו שיוצקים לתוכה את ה-{% equation %}\varphi{% endequation %} ומקבלים אקסיומה), ועבור {% equation %}\varphi{% endequation %} הזה אקסיומת ההחלפה היא

{% equation %}\forall x\forall y\forall z\left(\varphi\left(x,y,a_{1},\ldots,a_{n}\right)\wedge\varphi\left(x,z,a_{1},\ldots,a_{n}\right)\to y=z\right)\to{% endequation %}

{% equation %}\to\forall A\exists B\forall y\left(y\in B\leftrightarrow\left(\exists x\in A\right)\varphi\left(x,y,a_{1},\ldots,a_{n}\right)\right){% endequation %}

החצי הראשון של האקסיומה אומר "<strong>אם</strong> {% equation %}\varphi{% endequation %} מתארת פונקציה" והחצי השני אומר "<strong>אז</strong> לכל קבוצה {% equation %}A{% endequation %} שעליה מפעילים את הפונקציה, קיימת קבוצה {% equation %}B{% endequation %} שהיא התמונה של {% equation %}A{% endequation %}".

עכשיו אפשר סוף סוף לעשות עם זה משהו: אינדוקציה ורקורסיה על-סופיות. אבל מה זה אומר בכלל?

<h2>אינדוקציה על-סופית</h2>

במתמטיקה הרבה פעמים משתמשים בחופשיות במושגים "אינדוקציה" ו"רקורסיה" בתור מילים נרדפות, אבל עמוק בפנים יש להן משמעות פורמלית שונה. <strong>אינדוקציה</strong> מתארת את האופן שבו <strong>מוכיחים</strong> משהו בתהליך של הסקה מהפרט אל הכלל; <strong>רקורסיה</strong> מתארת את האופן שבו <strong>מגדירים</strong> משהו על קלט מסוים מתוך גרסאות פשוטות יותר של אותו הקלט. זה מה שצריך להיות לנו בראש - עם רקורסיה מגדירים, עם אינדוקציה מוכיחים.

כשאני מדבר על אינדוקציה או רקורסיה "על-סופיות" ("טרנספיניטיות") אני מתכוון לכאלו שמסתמכות על כלל הסודרים; ככה אפשר להבדיל מסוגים אחרים של אינדוקציה ורקורסיה. למשל, האינדוקציה ה"רגילה" מתבססת רק על המספרים הטבעיים.

בואו ניזכר איך אינדוקציה רגילה עובדת: יש לנו טענה {% equation %}P{% endequation %} שיכולה להיות נכונה או שגויה עבור מספרים טבעיים שונים ומשונים. אנחנו כותבים {% equation %}P\left(n\right){% endequation %} כדי לומר "הטענה {% equation %}P{% endequation %} מתקיימת עבור המספר הטבעי {% equation %}n{% endequation %}". הוכחה באינדוקציה פירושה להוכיח ש-{% equation %}P{% endequation %} מתקיימת <strong>לכל</strong> הטבעיים, וזאת על ידי הוכחה של שתי טענות:

<ol> <li>{% equation %}P\left(0\right){% endequation %} (הטענה מתקיימת עבור המספר הטבעי 0)</li>


<li>{% equation %}P\left(n\right)\to P\left(n+1\right){% endequation %} (<strong>אם</strong> הטענה מתקיימת עבור המספר הטבעי {% equation %}n{% endequation %} <strong>אז</strong> היא מתקיימת עבור המספר הטבעי {% equation %}n+1{% endequation %}).</li>

</ol>

שני אלו ביחד, כאמור, מוכיחים שהטענה מתקיימת לכל הטבעיים, כלומר {% equation %}\forall nP\left(n\right){% endequation %} כשהכמת {% equation %}\forall{% endequation %} ("לכל") רץ על כל הטבעיים.

לפעמים אוהבים קצת לחסוך בכתיבה ולנסח אינדוקציה מתמטית בצורה הבאה:

{% equation %}\forall n\left(\forall k<n\left(P\left(k\right)\right)\to P\left(n\right)\right)\to\forall nP\left(n\right){% endequation %}

הזוועה הזו אומרת "אם לכל {% equation %}n{% endequation %} טבעי זה נכון שאם לכל {% equation %}k<n{% endequation %} מתקיים {% equation %}P\left(k\right){% endequation %} נובע מכך ש-{% equation %}P\left(n\right){% endequation %}, אז {% equation %}P{% endequation %} נכון לכל הטבעיים". הניסוח הזה נקרא <strong>אינדוקציה שלמה</strong> והוא שקול לאינדוקציה "רגילה" אבל לפעמים יותר נוח, כי כדי להוכיח ש-{% equation %}P\left(n\right){% endequation %} מתקיים אפשר להשתמש ישירות בכך ש-{% equation %}P\left(k\right){% endequation %} מתקיים לכל {% equation %}k<n{% endequation %} ולא רק למספר שבא מייד לפני {% equation %}n{% endequation %}. לפעמים הניסוח הזה לא חוסך הרבה; עדיין צריך להוכיח בנפרד את המקרה עבור 0, וכשמוכיחים לאיבר כללי מספיק להסתמך על זה שהטענה מתקיימת לזה שלפניו.

מה שנחמד בניסוח של אינדוקציה שלמה זה שהוא עובד בדיוק באותה מידה עבור סודרים:

{% equation %}\forall\alpha\left(\forall\beta<\alpha\left(P\left(\beta\right)\right)\to P\left(\alpha\right)\right)\to\forall\alpha P\left(\alpha\right){% endequation %}

כלומר, דרך להוכיח שטענה מתקיימת לכל הסודרים (כולם! אפילו שראינו שמחלקת כל הסודרים גדולה מכדי להיות קבוצה!) היא להוכיח שלכל סודר, אם הטענה מתקיימת לכל הסודרים הקטנים ממנו, היא מתקיימת גם עבורו.

איך מוכיחים שאינדוקציה כזו באמת עובדת? ובכן, נניח ש-{% equation %}P{% endequation %} מקיימת את התכונה שתיארתי: לכל {% equation %}\alpha{% endequation %}, אם {% equation %}P\left(\beta\right){% endequation %} לכל {% equation %}\beta<\alpha{% endequation %} נובע מכך ש-{% equation %}P\left(\alpha\right){% endequation %}, ועכשיו בואו נניח ש-{% equation %}P{% endequation %} <strong>לא</strong> מתקיימת לכל הסודרים, אז קיים סודר מינימלי {% equation %}\alpha{% endequation %} שעבורו היא לא מתקיימת, אבל המינימליות שלו פירושה שלכל {% equation %}\beta<\alpha{% endequation %} <strong>כן</strong> מתקיים {% equation %}P\left(\beta\right){% endequation %}, ומכאן שגם {% equation %}P\left(\alpha\right){% endequation %} עצמו מתקיים.

בהוכחה הזו השתמשתי די בחופשיות בכך שבכל מחלקה של סודרים (לאו דווקא קבוצה) יש איבר מינימלי. זה לא נראה מובן מאליו אבל זה די פשוט: ניקח סודר <strong>כלשהו</strong> ששייך למחלקה; אז אנחנו יודעים שא) הסודר הזה הוא <strong>כן</strong> קבוצה, וקבוצה סדורה היטב, כלומר בכל תת-קבוצה שלו יש איבר מינימלי; וב) הסודר הזה מכיל את כל הסודרים שקטנים ממנו, ובפרט את כל האיברים באוסף שקטנים ממנו. לכן או שהוא האיבר המינימלי, או שאפשר לשלוף מתוכו את האיבר המינימלי.

יופי, אז הוכחנו שאינדוקציה על-סופית "עובדת", אבל אני עדיין רוצה לנסח אותה באופן שמזכיר אינדוקציה "רגילה" ולא אינדוקציה שלמה. בשביל זה אני צריך מושג חדש. השלב שבו אינדוקציה על מספרים טבעיים מפסיקה לעבוד הוא כשמגיעים אל {% equation %}\omega{% endequation %}; זה סודר שהוא לא עוקב מיידי של אף מספר טבעי (כלומר, לא שווה {% equation %}n+1{% endequation %} לאף טבעי {% equation %}n{% endequation %}) ולכן האינדוקציה לא "מגיעה" אליו. אנחנו צריכים חוק חדש שמדבר על {% equation %}\omega{% endequation %} וסודרים שדומים לו.

אז אני מגדיר <strong>סודר גבולי</strong> בתור סודר שהוא לא עוקב מיידי של אף סודר אחר, כלומר הוא לא מהצורה {% equation %}\alpha+1{% endequation %} עבור אף סודר (כזכור, {% equation %}\alpha+1\triangleq\alpha\cup\left\{ \alpha\right\} {% endequation %}). הסודר הגבולי הראשון הוא 0, והשני הוא {% equation %}\omega{% endequation %} וכן הלאה.

עכשיו אפשר לנסח אינדוקציה על-סופית בצורה יותר "קלאסית". נניח שיש לנו טענה {% equation %}P{% endequation %} על סודרים שמקיימת

<ol> <li>{% equation %}P\left(0\right){% endequation %}</li>


<li>אם {% equation %}P\left(\alpha\right){% endequation %} אז {% equation %}P\left(\alpha+1\right){% endequation %}</li>


<li>אם {% equation %}\alpha\ne0{% endequation %} הוא סודר גבולי ולכל {% equation %}\beta<\alpha{% endequation %} מתקיים {% equation %}P\left(\beta\right){% endequation %}, אז {% equation %}P\left(\alpha\right){% endequation %}</li>

</ol>

אז אפשר להסיק ש-{% equation %}P{% endequation %} מתקיימת לכל {% equation %}\alpha{% endequation %}.

עכשיו אפשר לעבור לדבר על רקורסיה, סוף סוף.

<h2>רקורסיה על-סופית</h2>

כמו עם אינדוקציה, גם כאן כדאי להתחיל עם דוגמא מעולם המספרים הטבעיים. איזו דוגמא מפורסמת יש למשהו שמוגדר ברקורסיה? זה קל: <strong>סדרת פיבונאצ'י</strong> היא ללא ספק הסדרה הרקורסיבית המפורסמת בעולם. בואו נזכיר מהי: זו סדרה {% equation %}F_{0},F_{1},F_{2},\ldots{% endequation %} שמוגדרת על ידי הכללים:

<ul> <li>{% equation %}F_{0}=0{% endequation %}</li>


<li>{% equation %}F_{1}=1{% endequation %}</li>


<li>{% equation %}F_{n}=F_{n-1}+F_{n-2}{% endequation %} לכל {% equation %}n>1{% endequation %}</li>

</ul>

הכללים הללו בעצם נחלקים לשני סוגים: יש לנו <strong>תנאי התחלה</strong>, שהם ערכים מפורשים של {% equation %}F{% endequation %} עבור איברים ספציפיים, במקרה שלנו {% equation %}F_{0},F_{1}{% endequation %}, ויש לנו <strong>כלל רקורסיבי</strong> שמאפשר לקבל את {% equation %}F_{n}{% endequation %} מתוך ערכים קודמים בסדרה. אנחנו רוצים להכליל את הרעיון הזה גם לסודרים, אבל בסודרים הסיטואציה קצת יותר מסובכת בגלל שיש לנו סודרים גבוליים שלא נוכל לכתוב {% equation %}\alpha-1{% endequation %} וכדומה עבורם. אז בואו נשתמש בניסוח קצת שונה, וקצת יותר מסורבל למראה במבט ראשון, גם עבור מספרים טבעיים.

הרעיון הוא כזה. מה זו בעצם "סדרה"? אנחנו חושבים עליה בתור פונקציה {% equation %}F:\mathbb{N}\to A{% endequation %} עבור קבוצה {% equation %}A{% endequation %} כלשהי; כלומר, דרך כלשהי להתאים לכל מספר טבעי איבר של {% equation %}A{% endequation %}. בסדרה רקורסיבית, כל איבר נבנה בצורה כלשהי מהאיברים הקודמים; פורמלית, יש פונקציה {% equation %}G{% endequation %} שמקבלת סדרה {% equation %}G\left(a_{0},a_{1},\ldots,a_{n-1}\right){% endequation %} ומוציאה כפלט את {% equation %}a_{n}{% endequation %}, שהוא האיבר הבא שאמור להופיע בסדרה בתנאי שהאיברים הקודמים היו {% equation %}a_{0},\ldots,a_{n}{% endequation %}. עכשיו, כשאנחנו בונים את הסדרה {% equation %}F{% endequation %}, אנחנו עושים את זה על ידי הפעלות של {% equation %}G{% endequation %} שמקבלת בכל פעם את האיברים של {% equation %}F{% endequation %} שכבר נבנו; אפשר לסמן את זה {% equation %}F|_{n}{% endequation %} - הצמצום של התחום של {% equation %}F{% endequation %} מהקבוצה {% equation %}\mathbb{N}{% endequation %} לקבוצה {% equation %}n=\left\{ 0,1,2,\ldots,n-1\right\} {% endequation %}, ואז מה שקורה הוא

{% equation %}F\left(n\right)=G\left(F|_{n}\right){% endequation %}

כלומר, הסדרה ה<strong>אינסופית</strong> {% equation %}F{% endequation %} נבנית איכשהו מתוך פונקציה {% equation %}G{% endequation %} שהקלטים שלה הן סדרות <strong>סופיות</strong>.

מסורבל? כן, אבל מה שנחמד פה הוא שזה עובד באותה מידה גם עבור הסודרים. אבל צריך להיזהר קצת. אם אנחנו רוצים ש-{% equation %}F{% endequation %} תהיה סדרה על-סופית, כלומר פונקציה שתוכל לקבל כקלט כל סודר, זה אומר שהתחום של {% equation %}F{% endequation %} הוא אוסף כל הסודרים - והאוסף הזה, כבר אמרתי, גדול מכדי להיות קבוצה. לכן {% equation %}F{% endequation %} היא מחלקה. כבר ראינו שמחלקה יכולה לתאר פונקציה, אז אני מקווה שאנחנו בסדר עם זה; כל החלק הראשון של הפוסט היה מיועד כדי שלא נתקומם כאן.

אם כן, הרעיון הוא שאם נתונה לי פונקציה {% equation %}G{% endequation %} (וגם זו "פונקציה" במובן של מחלקה) שמוגדרת על מחלקת כל הקבוצות {% equation %}V{% endequation %}, אני יכול להשתמש בה כדי ליצור סדרה על-סופית אחת ויחידה {% equation %}F{% endequation %}, שמקיימת

{% equation %}F\left(\alpha\right)=G\left(F|_{\alpha}\right){% endequation %}

לכל הסודרים, כאשר {% equation %}F|_{\alpha}{% endequation %} הוא הצמצום של {% equation %}F{% endequation %} לאיברי הסודר {% equation %}\alpha{% endequation %}, דהיינו הסדרה {% equation %}\left\{ F_{\beta}\right\} _{\beta<\alpha}{% endequation %} (הסדרה הזו היא <strong>כן</strong> קבוצה בזכות אקסיומת ההחלפה, שמחליפה את אברי הסודר {% equation %}\alpha{% endequation %} בזוגות {% equation %}\left(\beta,F_{\beta}\right){% endequation %}, ולכן קלט לגיטימי של {% equation %}G{% endequation %}).

את הטענה שבאמת קיימת סדרה אחת ויחידה {% equation %}F{% endequation %} כזו צריך להוכיח; אז בונים את {% equation %}F{% endequation %} בתור נוסחה לוגית {% equation %}\varphi{% endequation %} עם שני משתנים, {% equation %}\alpha,x{% endequation %}, כך ש-{% equation %}\varphi\left(\alpha,x\right){% endequation %} בודקת שקיימת סדרה {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}{% endequation %} כך שהדברים הללו מתקיימים

<ol> <li>לכל {% equation %}\beta<\alpha{% endequation %} מתקיים {% equation %}a_{\beta}=G\left(\left\{ a_{\gamma}\right\} _{\gamma<\beta}\right){% endequation %}</li>


<li>{% equation %}x=G\left(\left\{ a_{\beta}\right\} _{\beta<\alpha}\right){% endequation %}</li>

</ol>

כדי להראות שזה עובד, משתמשים באינדוקציה על-סופית. ראשית, אנחנו רוצים להראות ש-{% equation %}F{% endequation %} היא באמת פונקציה, כלומר שלכל {% equation %}\alpha{% endequation %}, אם קיימים {% equation %}x_{1},x_{2}{% endequation %} כך ש-{% equation %}\varphi\left(\alpha,x_{1}\right){% endequation %} וגם {% equation %}\varphi\left(\alpha,x_{2}\right){% endequation %} שניהם T אז {% equation %}x_{1}=x_{2}{% endequation %}. מה אנחנו יודעים על {% equation %}x_{1},x_{2}{% endequation %}? אנחנו יודעים שעבור {% equation %}x_{1}{% endequation %} קיימת סדרה {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}{% endequation %} שמקיימת את תנאי 1, ובנוסף {% equation %}x_{1}=G\left(\left\{ a_{\beta}\right\} _{\beta<\alpha}\right){% endequation %}; ואנחנו יודעים שעבור {% equation %}x_{2}{% endequation %} קיימת סדרה {% equation %}\left\{ b_{\beta}\right\} _{\beta<\alpha}{% endequation %} שמקיימת את תנאי 1 ובנוסף {% equation %}x_{2}=G\left(\left\{ a_{\beta}\right\} _{\beta<\alpha}\right){% endequation %}. אז מכיוון שאנחנו יודעים ש-{% equation %}G{% endequation %} פונקציה, אם נראה ש-{% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}=\left\{ b_{\beta}\right\} _{\beta<\alpha}{% endequation %}, ינבע מכך {% equation %}x_{1}=x_{2}{% endequation %}. ואיך נראה ששתי הסדרות הללו שוות? בעזרת תנאי 1, ובעזרת אינדוקציה.

אנחנו משתמשים באינדוקציה על {% equation %}\beta{% endequation %} ומראים ש-{% equation %}a_{\beta}=b_{\beta}{% endequation %} לכל {% equation %}\beta<\alpha{% endequation %}: הבסיס הוא {% equation %}\beta=0{% endequation %} ועבורו {% equation %}a_{0}=G\left(\emptyset\right)=b_{0}{% endequation %} (כי במקרה זה לא קיים {% equation %}\gamma<\beta{% endequation %} ולכן הסדרה של תנאי 1 ריקה). לכל סודר אחר, גבולי או עוקב, אנחנו מניחים שלכל {% equation %}\gamma<\beta{% endequation %} כבר מתקיים {% equation %}a_{\gamma}=b_{\gamma}{% endequation %}, ומכאן שהסדרות {% equation %}\left\{ a_{\gamma}\right\} _{\gamma<\beta},\left\{ b_{\gamma}\right\} _{\gamma<\beta}{% endequation %} שוות, ולכן 

{% equation %}a_{\beta}=G\left(\left\{ a_{\gamma}\right\} _{\gamma<\beta}\right)=G\left(\left\{ b_{\gamma}\right\} _{\gamma<\beta}\right)=b_{\beta}{% endequation %}

וזה מסיים את ההוכחה באינדוקציה. די פשוט!

יפה, אז מה שהשגנו עד כה הוא להראות ש-{% equation %}F{% endequation %} היא באמת פונקציה. אבל עדיין צריך להראות ש-{% equation %}F{% endequation %} מוגדרת <strong>לכל</strong> סודר {% equation %}\alpha{% endequation %}, כלומר שתמיד קיים {% equation %}x{% endequation %} כך ש-{% equation %}\varphi\left(\alpha,x\right){% endequation %} היא בעלת ערך T; זה לא מתחייב ממה שראינו עד כה. גם את זה נוכיח, כמה מפתיע, באינדוקציה על {% equation %}\alpha{% endequation %}.

עבור {% equation %}\alpha=0{% endequation %}, בוודאי ש-{% equation %}x=G\left(\emptyset\right){% endequation %} ישיג את המטרה ש-{% equation %}\varphi\left(0,x\right){% endequation %} תקבל T; הסדרה של ה"קיימת סדרה" במקרה הזה היא בהכרח ריקה (כי האינדקסים שלה הם {% equation %}\beta<0{% endequation %} ואין כאלו) ולכן תנאי 1 מתקיים באופן ריק ותנאי 2 הוא בדיוק {% equation %}x=G\left(\emptyset\right){% endequation %}. אז זה הבסיס.

עבור {% equation %}\alpha+1{% endequation %}, אנו מניחים שהטענה נכונה עבור {% equation %}\alpha{% endequation %}, כלומר קיים איבר שאסמן {% equation %}a_{\alpha}{% endequation %} וקיימת סדרה {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}{% endequation %} שמקיימת את תנאי 1 ובנוסף {% equation %}a_{\alpha}=G\left(\left\{ a_{\beta}\right\} _{\beta<\alpha}\right){% endequation %}. נרחיב את הסדרה הזו לסדרה {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha+1}{% endequation %} על ידי הוספת {% equation %}a_{\alpha}{% endequation %} בתור האיבר האחרון שלה. נסמן {% equation %}x=G\left(\left\{ a_{\beta}\right\} _{\beta<\alpha+1}\right){% endequation %} (קיים {% equation %}x{% endequation %} כזה כי {% equation %}G{% endequation %} היא פונקציה) ועכשיו ברור ש-{% equation %}\varphi\left(\alpha+1,x\right){% endequation %} הוא T.

אם {% equation %}\alpha{% endequation %} הוא סודר גבולי, אנחנו מניחים שהטענה נכונה לכל {% equation %}\beta<\alpha{% endequation %}. עכשיו מגיע החלק הטריקי והטכני ביותר בהוכחה: אני רוצה לבנות את הסדרה {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}{% endequation %}. אם אני אבנה אותה, אני אוכל להגדיר {% equation %}x=G\left(\left\{ a_{\beta}\right\} _{\beta<\alpha}\right){% endequation %} ואז {% equation %}\varphi\left(\alpha,x\right){% endequation %} יתקיים וכולנו נשמח. אבל בשביל זה צריך להראות שהסדרה {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}{% endequation %} <strong>קיימת</strong>. לא קיימת במובן הנפנוף-ידיימי של מחלקות; קיימת בתור אובייקט מתמטי קונקרטי - קבוצה - ביקום שלנו.

אז ראשית כל, אינטואיציה. אם יש לנו {% equation %}\beta_{1}<\beta_{2}<\alpha{% endequation %}, אנחנו יודעים שהסדרה עד {% equation %}\beta_{1}{% endequation %} היא תת-סדרה של הסדרה עד {% equation %}\beta_{2}{% endequation %}. פורמלית, מכיוון ש-{% equation %}\beta_{1}{% endequation %} מקיימת את הנחת האינדוקציה קיימת עבורה סדרה, {% equation %}\left\{ a_{\gamma}\right\} _{\gamma\le\beta_{1}}{% endequation %} שמקיימת את תכונות 1-2. בדומה עבור {% equation %}\beta_{2}{% endequation %} קיימת סדרה {% equation %}\left\{ b_{\gamma}\right\} _{\gamma\le\beta_{2}}{% endequation %} שכזו. אפשר להוכיח באינדוקציה, כמו שעשינו קודם, שעבור {% equation %}\gamma\le\beta_{1}{% endequation %} מתקיים {% equation %}a_{\gamma}=b_{\gamma}{% endequation %} - שתי הסדרות זהות עד שהסדרה הקצרה ביותר נגמרת. זה נכון לכל זוג {% equation %}\beta_{1}<\beta_{2}<\alpha{% endequation %}, ולכן אם נחשוב לרגע על שתי הסדרות הללו בתור קבוצות של זוגות סדורים:

{% equation %}\left\{ \left(0,a_{0}\right),\left(1,a_{1}\right),\ldots,\left(\beta_{1},a_{\beta_{1}}\right)\right\} {% endequation %}

{% equation %}\left\{ \left(0,a_{0}\right),\left(1,a_{1}\right),\ldots,\left(\beta_{1},a_{\beta_{1}}\right),\ldots,\left(\beta_{2},a_{\beta_{2}}\right)\right\} {% endequation %}

אז אחרי שנאחד את שתי הקבוצות הללו נקבל את הגדולה יותר, בלי "איברים מיותרים" נוספים.

על פי אותו הגיון, אם תהיה לנו קבוצה שהאיברים שלה הן <strong>כל הסדרות</strong> שמתאימות לכל אחד מה-{% equation %}\beta<\alpha{% endequation %} האפשריים, איחוד של כל אברי הקבוצה הזו יתן לנו בדיוק את הסדרה {% equation %}\left\{ a_{\beta}\right\} _{\beta<\alpha}{% endequation %} המבוקשת: לכל {% equation %}\beta<\alpha{% endequation %} אכן יהיה בדיוק איבר אחד בסדרה, והסדרה תקיים את החוקיות של דרישה (1). רק צריך להראות שקיימת קבוצה שהאיברים שלה הן <strong>כל הסדרות</strong>. הקבוצה הזו מתקבלת <strong>מאקסיומת ההחלפה</strong> כשמפעילים אותה על {% equation %}\alpha{% endequation %} ומחליפים כל {% equation %}\beta{% endequation %} בסדרה {% equation %}\left\{ a_{\gamma}\right\} _{\gamma\le\beta_{1}}{% endequation %} . השימוש הזה באקסיומת ההחלפה דורש בעצמו עבודה טכנית - להראות שיש פסוק שמקבל זוג של {% equation %}\beta{% endequation %} וסדרה {% equation %}\left\{ a_{\gamma}\right\} _{\gamma\le\beta}{% endequation %} ומוודא שהסדרה {% equation %}\left\{ a_{\gamma}\right\} _{\gamma\le\beta}{% endequation %} מקיימת את תנאים 1-2 ושהיא כוללת את כל הסודרים עד וכולל {% equation %}\beta{% endequation %}, וש-{% equation %}\beta{% endequation %} הוא בכלל סודר... הבנו את הרעיון, זה הזמן להתחיל לחפף.

לסיום, בואו נוכיח יחידות: נניח ש-{% equation %}F,F^{\prime}{% endequation %} הן שתי פונקציות שמקיימות שתיהן {% equation %}F\left(\alpha\right)=G\left(F|_{\alpha}\right){% endequation %} ו-{% equation %}F^{\prime}\left(\alpha\right)=G\left(F^{\prime}|_{\alpha}\right){% endequation %} ונוכיח ש-{% equation %}F\left(\alpha\right)=F^{\prime}\left(\alpha\right){% endequation %} לכל סודר {% equation %}\alpha{% endequation %} (כאן אנחנו נעזרים בכך שאנחנו כבר יודעים ש-{% equation %}F,F^{\prime}{% endequation %} מוגדרות לכל סודר). איך? באינדוקציה, כמובן! ההוכחה טריוויאלית, כי {% equation %}F|_{\alpha}=F^{\prime}|_{\alpha}{% endequation %} אם אנחנו מניחים את נכונות הטענה לכל {% equation %}\beta<\alpha{% endequation %} (כי צמצמנו את שתי הפונקציות הללו אל תחום שבו הן שוות) ולכן {% equation %}F\left(\alpha\right)=G\left(F|_{\alpha}\right)=G\left(F^{\prime}|_{\alpha}\right)=F^{\prime}\left(\alpha\right){% endequation %}, מה שמסיים את ההוכחה.

<h2>דוגמא מועילה במיוחד: ההיררכייה המצטברת</h2>

אינדוקציה ורקורסיה על-סופיות הן דבר מועיל, ואנחנו מתעסקים בקבוצות, אז מה יותר מועיל מלהוכיח דברים באינדוקציה על-סופית על קבוצות, ולהגדיר קבוצות בעזרת רקורסיה על-סופית? הבעיה היא ששתיהן דורשת <strong>סדרה</strong>, וקבוצות לא מסודרות בסדרה, הן... בלאגן אחד גדול. אבל יש טריק פשוט שמאפשר לנו לעבור מרמת הקבוצה לרמת הסדרה - מה שנקרא <strong>ההיררכייה המצטברת</strong>, שהוא דרך להתאים לכל קבוצה "דרגה" שהיא מספר סודר כלשהו, כך שלכל קבוצה - הדרגות של כל האיברים שלה קטנות יותר. זה מאפשר לנו להוכיח באינדוקציה דברים על קבוצות: מוכיחים באינדוקציה על-סופית על הדרגות, ואז בכל פעם שיש לנו קבוצה שצריך להוכיח עליה משהו, אפשר להניח שאותו משהו כבר מתקיים לכל איבריה.

אם כן, הרעיון הוא שקיימת סדרה על-סופית {% equation %}V_{0},V_{1},V_{2},\ldots{% endequation %} של קבוצות כך שלכל קבוצה קיימת {% equation %}V_{\alpha}{% endequation %} בהיררכייה שהיא שייכת אליה. דרך אפשרית אחת להגדיר את ההיררכייה היא בתור {% equation %}V_{\alpha}=\mathcal{P}\left(\bigcup_{\beta<\alpha}V_{\beta}\right){% endequation %}, מה שנותן

{% equation %}V_{0}=\mathcal{P}\left(\emptyset\right)=\left\{ \emptyset\right\} {% endequation %}

{% equation %}V_{1}=\mathcal{P}\left(\left\{ \emptyset\right\} \right)=\left\{ \emptyset,\left\{ \emptyset\right\} \right\} {% endequation %}

{% equation %}V_{2}=\mathcal{P}\left(\left\{ \emptyset,\left\{ \emptyset\right\} \right\} \right)=\left\{ \emptyset,\left\{ \emptyset\right\} ,\left\{ \left\{ \emptyset\right\} \right\} \left\{ \emptyset,\left\{ \emptyset\right\} \right\} \right\} {% endequation %}

וכן הלאה וכן הלאה. אז הדרגה של {% equation %}\emptyset{% endequation %} היא 0 ושל {% equation %}\left\{ \emptyset,\left\{ \emptyset\right\} \right\} {% endequation %} היא 2 וכן הלאה.

למה כל קבוצה שייכת לדרגה כלשהי בהיררכייה? ובכן, זה לא לגמרי מובן מאליו - כדי להוכיח את זה אני אשתמש באחת מהאקסיומות של ZFC שאני לא בטוח אם הצגתי עד כה - <strong>אקסיומת היסוד</strong>. אדבר עליה בפירוט בהמשך; לעת עתה מה שצריך לדעת הוא שהיא באה למנוע סיטואציות הזויות כמו קבוצות {% equation %}A{% endequation %} שמקיימות {% equation %}A\in A{% endequation %}, ופורמלית אני מגדיר אותה באופן הבא: לכל קבוצה לא ריקה {% equation %}A{% endequation %}, קיים ב-{% equation %}A{% endequation %} איבר מינימלי ביחס ל-{% equation %}\in{% endequation %} (כלומר קיים {% equation %}x\in A{% endequation %} כך שלכל {% equation %}y\in A{% endequation %} מתקיים {% equation %}y\notin x{% endequation %}).

בואו ניקח קבוצה {% equation %}A{% endequation %} כלשהי ונניח שלכל {% equation %}x\in A{% endequation %}, קיים סודר {% equation %}\alpha_{x}{% endequation %} כך ש-{% equation %}x\in V_{\alpha_{x}}{% endequation %}. אז נגדיר סודר חדש, {% equation %}\overline{\alpha}=\bigcup\left\{ \alpha_{x}+1\ |\ x\in A\right\} {% endequation %}. קיבלנו סודר כך ש-{% equation %}\alpha_{x}<\overline{\alpha}{% endequation %} לכל {% equation %}x\in A{% endequation %}, אז {% equation %}\bigcup_{\beta<\overline{\alpha}}V_{\beta}{% endequation %} כוללת את כל ה-{% equation %}x\in A{% endequation %}-ים, ולכן {% equation %}A\in V_{\overline{\alpha}}=\mathcal{P}\left(\bigcup_{\beta<\overline{\alpha}}V_{\beta}\right){% endequation %}. אז זה מסביר למה, באופן לא מפתיע, אם כל האיברים של קבוצה שייכים להיררכייה אז היא עצמה שייכת להיררכייה; אבל למה אפשר תמיד להניח שכל האיברים של קבוצה יהיו שייכים להיררכייה?

בבירור מסתתר כאן טיעון כלשהו שמדבר לא רק על קבוצה והאיברים שלה אלא גם על האיברים של האיברים שלה והאיברים-של-האיברים-של-האיברים שלה וכן הלאה. צריך לפרמל את זה איכשהו, אז אפשר לדבר על <strong>הסגור הטרנזיטיבי</strong> של קבוצה שהוא מה שמכיל את כל הדברים הללו. בשביל הגדרה פורמלית, נגדיר {% equation %}A^{\prime}=\bigcup_{x\in A}x{% endequation %}: זו הקבוצה שאבריה הם כל האיברים-של-איברים של {% equation %}A{% endequation %}. עכשיו אפשר להגדיר סגור טרנזיטיבי על ידי {% equation %}A^{*}=A\cup A^{\prime}\cup A^{\prime\prime}\cup\ldots{% endequation %}. נשאר להוכיח את הטענה שבהינתן {% equation %}A{% endequation %}, לכל {% equation %}x\in A^{*}{% endequation %} מתקיים ש-{% equation %}x{% endequation %} שייך להיררכייה המצטברת. זו טענה חזקה יותר מהטענה הקודמת, כי {% equation %}A\subseteq A^{*}{% endequation %} ולכן אם הטענה נכונה עבור {% equation %}A^{*}{% endequation %} היא בוודאי נכונה עבור {% equation %}A{% endequation %}; אבל היתרון בכך שהיא חזקה יותר הוא שעכשיו יש לנו גם יותר לעבוד איתו ב"צעד האינדוקציה" (במרכאות, כי אנחנו לא באמת מבצעים פה אינדוקציה).

בואו נניח עכשיו בשלילה שב-{% equation %}A^{*}{% endequation %} יש איברים ש<strong>אינם</strong> שייכים להיררכייה המצטברת. אז בזכות אקסיומת היסוד, אני יכול להניח שיש ביניהם איבר מינימלי {% equation %}x{% endequation %}. אם כל האיברים של {% equation %}x{% endequation %} כן שייכים להיררכייה המצטברת, כבר ראינו שמכך ינבע שגם {% equation %}x{% endequation %} שייך. אם כן, יהי {% equation %}y\in x{% endequation %} כלשהו. אם {% equation %}x\in A^{\left(n\right)}{% endequation %} אז {% equation %}y\in A^{\left(n+1\right)}{% endequation %}, ולכן {% equation %}y\in A^{*}{% endequation %} בעצמו. המינימליות של {% equation %}x{% endequation %} והעובדה ש-{% equation %}y\in x{% endequation %} אומרת לנו שלא ייתכן שגם {% equation %}y{% endequation %} לא שייך להיררכייה המצטברת, ולכן כל האיברים של {% equation %}x{% endequation %} שייכים להיררכייה המצטברת, ולכן גם {% equation %}x{% endequation %} עצמו, וסיימנו.

מכאן ואילך נוכל להשתמש בחופשיות בהיררכייה המצטברת בהוכחות. פורמלית, לכל קבוצה {% equation %}A{% endequation %} נתאים סודר {% equation %}\text{rank}\left(A\right){% endequation %} כך ש-{% equation %}\text{rank}\left(A\right)=\min\left\{ \alpha\ |\ A\in V_{\alpha}\right\} {% endequation %} ונקרא לזה <strong>הדרגה</strong> של {% equation %}A{% endequation %}, ואז האינדוקציה/רקורסיה שלנו תהיה על הדרגה. אנחנו רוצים להיות מסוגלים להניח שלכל {% equation %}A{% endequation %}, הדרגה של כל האיברים של {% equation %}A{% endequation %} קטנה מהדרגה של {% equation %}A{% endequation %} עצמה (ולכן אפשר להניח באינדוקציה שהטענה נכונה עבורם/להניח שערכם כבר הוגדר ברקורסיה). למה זה נכון? כי אם {% equation %}A\in V_{\alpha}{% endequation %}, כש-{% equation %}\alpha{% endequation %} הוא המינימלי בעל תכונה זו, אז {% equation %}A\in\mathcal{P}\left(\bigcup_{\beta<\alpha}V_{\beta}\right){% endequation %}, מה שאומר שכל אברי {% equation %}A{% endequation %} שייכים ל-{% equation %}V_{\beta}{% endequation %} עם {% equation %}\beta<\alpha{% endequation %}.

זהו, סיימנו עם ההירכייה המצטברת, ולכן עם הפוסט הזה. מה עכשיו? סיימנו את הדברים הבסיסיים שאפשר לומר על סודרים, ואפשר לעבור אל המושג הכי מלהיב שאנחנו יכולים להגדיר בעזרתם בשלב הזה: <strong>עוצמות</strong>. זה מה שיקרה בפוסט הבא. 
