---
id: 2292
title: "הבעיה העשירית של הילברט - נקמתן של הפונקציות הרקורסיביות והדיופנטיות"
date: 2013-01-01 23:10:26
layout: post
categories: 
  - תורת המספרים
tags: 
  - הבעיה העשירית של הילברט
---
בפוסטים הקודמים בסדרה <a href="http://www.gadial.net/2012/11/12/hilbert_tenth_exponential_function/">עבדנו קשה</a> כדי להוכיח שהפונקציה האקספוננציאלית היא דיופנטית. הצלחנו בזה סוף סוף ועכשיו אפשר לשכוח מהעניין לבינתיים ולנסות להיזכר מה בעצם אנחנו מנסים להוכיח, ומה האסטרטגיה הכללית שלנו.

כזכור, פונקציה דיופנטית היא פונקציה {% equation %}f\left(x_{1},\dots,x_{n}\right){% endequation %} כך שקיימת מערכת משוואות דיופנטיות עם המשתנים {% equation %}x_{1},\dots,x_{n},y,z_{1},\dots,z_{n}{% endequation %} בעלת התכונה הבאה: אם אנו מציבים ערכים {% equation %}a_{1},\dots,a_{n}{% endequation %} ב-{% equation %}x{% endequation %}-ים ו-{% equation %}b{% endequation %} ב-{% equation %}y{% endequation %}, אז למה שנשאר ממערכת המשוואות (שכעת היא רק עם המשתנים {% equation %}z_{1},\dots,z_{n}{% endequation %}) קיים פתרון אם ורק אם {% equation %}b=f\left(a_{1},\dots,a_{n}\right){% endequation %}. כאן "משוואה דיופנטית" היא משוואה פולינומית עם מקדמים חיוביים שהפתרונות שלה גם הם חייבים להיות חיוביים.

הבעיה העשירית של הילברט היא זו: בהינתן משוואה דיופנטית, לקבוע האם קיים לה פתרון או לא. איך זה קשור לפונקציות דיופנטיות? בצורה הבאה: נניח שהצלחנו לפתור את הבעיה העשירית של הילברט; אז אם {% equation %}f{% endequation %} היא פונקציה דיופנטית ואנחנו רוצים לדעת אם {% equation %}f\left(a_{1},\dots,a_{n}\right)=b{% endequation %}, כל מה שאנחנו צריכים לעשות הוא לקחת את מערכת המשוואות שמראה ש-{% equation %}f{% endequation %} היא דיופנטית, להציב במשתנים המתאימים בה את {% equation %}a_{1},\dots,a_{n},b{% endequation %}, ואז לקחת את האלגוריתם שפותר את הבעיה העשירית של הילברט ולהפעיל אותו על המשוואה שקיבלנו. אם יש פתרון, אז {% equation %}f\left(a_{1},\dots,a_{n}\right)=b{% endequation %}; ואם אין פתרון, אז {% equation %}f\left(a_{1},\dots,a_{n}\right)\ne b{% endequation %}.

בואו ניקח את זה צעד אחד קדימה: נניח שכל מה שנתון לנו הם רק {% equation %}a_{1},\dots,a_{n}{% endequation %} ומבקשים מאיתנו <strong>לחשב</strong> את {% equation %}f\left(a_{1},\dots,a_{n}\right){% endequation %} או אפילו סתם לדעת אם {% equation %}f{% endequation %} מוגדרת על הקלט הזה. באופן כללי זו יכולה להיות בעיה קשה למדי, אבל לא אם יש לנו פתרון לבעיה העשירית של הילברט: במקרה זה פשוט נציב את {% equation %}a_{1},\dots,a_{n}{% endequation %} במשוואות ונראה אם יש לנו פתרון. אם אין פתרון, אז {% equation %}f\left(a_{1},\dots,a_{n}\right){% endequation %} אינו מוגדר, ואילו אם יש פתרון אז ניקח את הערך שהוצב במשתנה {% equation %}y{% endequation %} במשוואות: הערך הזה יהיה {% equation %}b{% endequation %} שמקיים {% equation %}b=f\left(a_{1},\dots,a_{n}\right){% endequation %}.

עכשיו, בואו נכניס לתמונה שחקן חדש שתמיד כדאי להכיר: <a href="http://www.gadial.net/2007/09/26/halting_problem/">בעיית העצירה</a>. בניסוח לא פורמלי שיספיק לנו כאן, בעיית העצירה היא זו - נותנים לכם קוד של תוכנית מחשב בשפת C, ושואלים אם תוכנית המחשב הזו מסיימת אי פעם את ריצה (אנו מניחים שאין עליה מגבלות זמן וזכרון כמו שיש על תוכניות שרצות על מחשבים אמיתיים). על פניו לא בעיה נוראית, אבל אלן טיורינג הוכיח ש<strong>אין אלגוריתם</strong> שפותר את הבעיה הזו. עם זאת, הבעיה היא כן "חצי פתירה" במובן הבא: אם התוכנית עוצרת מתישהו תמיד נוכל לגלות את זה אם נריץ אותה מספיק זמן; ולכן יש לנו בעיה לענות נכון רק אם התוכנית לא עוצרת אף פעם (כי מתי אנחנו יכולים להפסיק את הבדיקה ולהחליט בודאות גמורה שהתוכנית לא תעצור אף פעם?). בהתאם לתכונה הזו אפשר להגדיר פונקציה {% equation %}f{% endequation %} שמקבלת כקלט תוכנית מחשב בשפת C, ופולטת את מספר הצעדים שהתוכנית מבצעת עד שהיא עוצרת, ואילו אם התוכנית לא עוצרת אז {% equation %}f{% endequation %} לא מוגדרת עליה.

נניח שבאורח קסום כלשהו {% equation %}f{% endequation %} הייתה דיופנטית והבעיה העשירית של הילברט הייתה פתירה, אז היינו פותרים את בעיית העצירה כך: בהינתן תוכנית מחשב שמקודדת על ידי ערכים {% equation %}a_{1},\dots,a_{a}{% endequation %} ש-{% equation %}f{% endequation %} מקבלת נציב את {% equation %}a_{1},\dots,a_{n}{% endequation %} במשוואה הדיופנטית שמתאימה ל-{% equation %}f{% endequation %}, נפעיל את האלגוריתם שפותר את הבעיה העשירית של הילברט על המשוואה שהתקבלה, ואם אין לה פתרון נכריז שהתוכנית לא עוצרת, ואחרת נכריז שהתוכנית כן עוצרת. פשוט ביותר.

אם כן, כדי להוכיח שהבעיה העשירית של הילברט אינה פתירה, די לי להוכיח שהפונקציה {% equation %}f{% endequation %} שהגדרתי היא דיופנטית. מה שעשו בפועל היה הרבה יותר מכך - הוכיחו שכל פונקציה <strong>ניתנת לחישוב</strong> היא דיופנטית. מהי פונקציה ניתנת לחישוב? פונקציה {% equation %}f{% endequation %} שקיים אלגוריתם שעל כל קלט {% equation %}x{% endequation %} <strong>עבורו היא מוגדרת</strong> מחשבת את {% equation %}f\left(x\right){% endequation %}, ואילו על קלטים שעבורם {% equation %}f{% endequation %} לא מוגדרת האלגוריתם פשוט לא עוצר. אם כן, זה היעד שלנו וזה מה שמחסל את הבעיה העשירית של הילברט: הטענה "אם פונקציה היא ניתנת לחישוב, אז היא דיופנטית".

הבעיה היא ש"ניתנת לחישוב" הוא מושג די מופשט. צריך להיסגר על פורמליזם קונקרטי של חישוב ולעבוד איתו. אפשר היה ללכת לפורמליזם הסטנדרטי בתורת החישוביות: "מכונת טיורינג". רק שאנחנו לא עושים זאת, כי יש פורמליזם אחר, שקול, שהרבה יותר דומה למה שאנחנו מנסים לעשות עם פונקציות דיופנטית ואיתו העבודה שלנו תהיה קלה בהרבה: המודל של <strong>פונקציות רקורסיביות</strong>. כבר הזכרתי אותן <a href="http://www.gadial.net/2012/09/04/hilbert_tenth_diophantic_functions/">בפוסט השני</a> בסדרת הפוסטים הנוכחית ותיארתי את תחילת ההוכחה לשקילות שלהן ושל הפונקציות הדיופנטיות. מה שנשאר היה רק ליצור "שפה" דמוית לוגיקה שבעזרתה אפשר לבנות פונקציות דיופנטיות מורכבות וזאת כדי להוכיח שכללי הבניה של הפונקציות הרקורסיביות, כשמפעילים אותם על פונקציות דיופנטיות, מחזירים פונקציות דיופנטיות. בואו נתחיל, בזהירות, ליצור את ה"שפה" הזו. פורמלית, אני מגדיר קבוצה של איברים שאני קורא להם ברישול מה "ביטויים דיופנטיים".

ראשית, כל משוואה דיופנטית היא כמובן ביטוי דיופנטי לגיטימי בשפה שלנו. משוואה דיופנטית היא משהו מהצורה {% equation %}p\left(x_{1},\dots,x_{n}\right)=0{% endequation %} כאשר {% equation %}x_{1},\dots,x_{n}{% endequation %} הם משתנים כלשהם ו-{% equation %}p{% endequation %} הוא פולינום. אפשר להכליל את זה קצת ולדבר על משוואות מהצורה {% equation %}p\left(x_{1},\dots,x_{n}\right)=q\left(x_{1},\dots,x_{n}\right){% endequation %} כאשר {% equation %}q{% endequation %} גם הוא פולינום (גם 0 הוא פולינום חוקי מבחינתנו). המשוואה הדיופנטית שמייצגת את הביטוי {% equation %}p\left(x_{1},\dots,x_{n}\right)=q\left(x_{1},\dots,x_{n}\right){% endequation %} היא פשוט {% equation %}p\left(x_{1},\dots,x_{n}\right)-q\left(x_{1},\dots,x_{n}\right)=0{% endequation %} (כלומר, הפולינום {% equation %}p-q{% endequation %} מייצג את הביטוי הזה).

כעת, אם {% equation %}P,Q{% endequation %} הם שני ביטויים דיופנטיים שמיוצגים על ידי הפולינומים {% equation %}p,q{% endequation %} בהתאמה, גם {% equation %}P\wedge Q{% endequation %} הוא ביטוי דיופנטי שמיוצג על ידי הפולינום {% equation %}p^{2}+q^{2}{% endequation %} (שמתאפס אם ורק אם {% equation %}p,q{% endequation %} מתאפסים בו זמנית). עד כאן - הכל קל.

עכשיו, נניח ש-{% equation %}f\left(x_{1},\dots,x_{n}\right){% endequation %} היא פונקציה שכבר הוכחנו שהיא דיופנטית ואנחנו רוצים להשתמש בה בביטוי שלנו. מה זה אומר ש-{% equation %}f{% endequation %} דיופנטית? כפי שאמרנו בתחילת הפוסט, שיש פולינום {% equation %}p_{f}\left(x_{1},\dots,x_{n},y,z_{1},\dots,z_{m}\right){% endequation %} כך שלערכים נתונים של {% equation %}x_{1},\dots,x_{n}{% endequation %} ו-{% equation %}y{% endequation %}, המשוואה {% equation %}p_{f}=0{% endequation %} (במשתנים שנותרו, {% equation %}z_{1},\dots,z_{m}{% endequation %} פתירה אם ורק אם {% equation %}f\left(x_{1},\dots,x_{n}\right)=y{% endequation %}. אם כן, אפשר להשתמש בביטוי הדיופנטי {% equation %}y=f\left(x_{n},\dots,x_{n}\right){% endequation %} בתור קיצור ל-{% equation %}p_{f}=0{% endequation %}. אפשר גם לכתוב משהו כמו {% equation %}f\left(x_{1},\dots,x_{n}\right)=g\left(x_{1},\dots,x_{n}\right){% endequation %} בתור קיצור ל-{% equation %}\left(y=f\left(x_{1},\dots,x_{n}\right)\right)\wedge\left(z=g\left(x_{1},\dots,x_{n}\right)\right)\wedge\left(y=z\right){% endequation %}.

הדבר האחרון שנזדקק לו הוא <strong>כמתים</strong>. נתחיל בקל מביניהם: אם {% equation %}P{% endequation %} היא ביטוי דיופנטי אז גם {% equation %}\exists x\left(P\right){% endequation %} הוא ביטוי דיופנטי, כש-{% equation %}x{% endequation %} הוא משתנה כלשהו (כנראה כזה שמופיע ב-{% equation %}P{% endequation %}, אחרת מה הטעם). מבחינה פורמלית, כשאנחנו מתרגמים את הכל לפולינום, אין הבדל בין הפולינום של {% equation %}P{% endequation %} ובין הפולינום של {% equation %}\exists x\left(P\right){% endequation %}. ההבדל הוא רעיוני: אם משתנה ב-{% equation %}P{% endequation %} נופל תחת כמת {% equation %}\exists{% endequation %} עבורו, אומרים שהוא <strong>משתנה קשור</strong>, ואם הוא לא נופל תחת כמת אומרים שהוא <strong>חופשי</strong>. הרעיון בביטוי דיופנטי הוא לקבל בסופו של דבר פולינום בעל התכונה הבאה: לכל הצבה של ערכים <strong>במשתנים החופשיים</strong>, למשוואה שמיוצגת על ידי הפולינום קיים פתרון אם ורק אם הביטוי הדיופנטי מקבל את ערך האמת "אמת". במילים אחרות, המשתנים הקשורים הם המשתנים שבהם משחקים את משחק ה"האם המשוואה פתירה, עכשיו משהצבתי בה ערכים מסויימים?"

נשאר לנו עוד לתאר כמת אחד אבל קודם כל בואו נראה דוגמאות למכביר כי אחרת קשה להבין מה הלך פה. באופן כללי כשאני רוצה לייצג פונקציה דיופנטית {% equation %}f{% endequation %} כלשהי אני כותב משהו מהצורה {% equation %}y=f\left(x_{1},\dots,x_{n}\right)\iff P\left(y,x_{1},\dots,x_{n}\right){% endequation %} כאשר {% equation %}P{% endequation %} הוא ביטוי דיופנטי שמקבל "אמת" רק כאשר מתקיים הקשר {% equation %}y=f\left(x_{1},\dots,x_{n}\right){% endequation %} (או במילים אחרות, הוא מייצג פולינום שאחרי שמציבים בו את {% equation %}y,x_{1},\dots,x_{n}{% endequation %} המשוואה שמתקבלת היא פתירה אם ורק אם {% equation %}y=f\left(x_{1},\dots,x_{n}\right){% endequation %}).

הפונקציות הרקורסיביות הבסיסיות היו הפונקציה הקבועה {% equation %}c\left(x\right)=1{% endequation %}, פונקציית העוקב {% equation %}s\left(x\right)=x+1{% endequation %} ופונקציות ההטלה {% equation %}U_{i}^{n}\left(x_{1},\dots,x_{n}\right)=x_{i}{% endequation %}. הביטויים הדיופנטיים המתאימים הם:

{% equation %}y=c\left(x\right)\iff\left(y=1\right){% endequation %}

{% equation %}y=s\left(x\right)\iff\left(y=x+1\right){% endequation %}

{% equation %}y=U_{i}^{n}\left(x_{1},\dots,x_{n}\right)\iff\left(y=x_{i}\right){% endequation %}

בכל המקרים הללו הביטוי הדיופנטי הוא מה שקראתי לו "ביטוי בסיסי" מהצורה {% equation %}p=q{% endequation %} כאשר {% equation %}p,q{% endequation %} הם שני פולינומים (ופולינומים פשוטים למדי במקרה שלנו). בניה קצת יותר מעניינת אפשר לתת אם זוכרים שהצלחנו להוכיח שהפונקציה {% equation %}h\left(n,k\right)=n^{k}{% endequation %} היא דיופנטית. נניח שאנחנו רוצים להוכיח עכשיו שהפונקציה {% equation %}f\left(n,k,t\right)=n^{\left(k^{t}\right)}{% endequation %} היא דיופנטית, את זה אפשר לעשות בקלי קלות:

{% equation %}y=n^{k^{t}}\iff\exists z\left(y=n^{z}\wedge z=k^{t}\right){% endequation %}

שימו לב: כאן {% equation %}n,k,t,y{% endequation %} כולם <strong>פרמטרים</strong> שאנחנו הולכים להציב בפולינום שמתאר את הביטוי באגף ימין, ואחרי שנעשה את זה נישאר עם פולינום שהמשתנה החופשי היחיד שלו הוא {% equation %}z{% endequation %}, ו... רגע, האמנם?

בפולינום הזה יהיה כמובן את {% equation %}z{% endequation %} בתור משתנה חופשי, אבל יהיו בו המון משתנים חופשיים אחרים ש"מוסתרים" כרגע מאיתנו. הביטוי {% equation %}y=n^{z}{% endequation %} והביטוי {% equation %}z=k^{t}{% endequation %} אומרים שניהם את אותו הדבר: עבדנו קשה בפוסטים הקודמים כדי לקבל פולינום מסובך מאוד שמתאר את הפונקציה הזו (אם תזכרו, בסופו של דבר קיבלנו מערכת של 11 משוואות). קחו את הפולינום שמתאים ל-{% equation %}z=k^{t}{% endequation %} ואת הפולינום שמתאים ל-{% equation %}y=n^{z}{% endequation %} (זה אותו פולינום אבל עם שמות שונים למשתנים שבתוכו) ועכשיו "תערבבו" אותם על פי הכלל של {% equation %}\wedge{% endequation %} (דהיינו תעלו בריבוע ותחברו). התוצאה תיראה איום ונורא, אבל כל עוד אנחנו מסוגלים לתאר אותה בצורה הקומפטית {% equation %}\exists z\left(y=n^{z}\wedge z=k^{t}\right){% endequation %} ולדעת זה עובד, אנחנו מרוצים. וזה כמובן עובד, כי {% equation %}\exists z\left(y=n^{z}\wedge z=k^{t}\right){% endequation %} מקבל ערך אמת רק אם באמת {% equation %}y=n^{k^{t}}{% endequation %}.

בואו נמשיך לחסל את הפונקציות הרקורסיביות, ונעבור כעת לטפל בכללי הבניה שלהן - די לנו להראות שאם מפעילים את כללי הבניה על פונקציות דיופנטיות מקבלים פונקציה דיופנטית. הכלל הראשון היה הרכבה, ובו בנינו מתוך הפונקציות {% equation %}f,g_{1},\dots,g_{m}{% endequation %} את {% equation %}h\left(x_{1},\dots,x_{n}\right)=f\left(g_{1}\left(x_{1},\dots,x_{n}\right),\dots,g_{m}\left(x_{1},\dots,x_{n}\right)\right){% endequation %}. הביטוי הדיופנטי המתאים (שכבר הצגתי בעבר) הוא

{% equation %}y=h\left(x_{1},\dots,x_{n}\right)\iff\exists t_{1},\dots,t_{m}{% endequation %}

{% equation %}\left(y=f\left(t_{1},\dots,t_{m}\right)\wedge t_{1}=g_{1}\left(x_{1},\dots,x_{n}\right)\wedge\dots\wedge t_{m}=g_{m}\left(x_{1},\dots,x_{n}\right)\right){% endequation %}

שבנוי בדיוק על פי אותם עקרונות כמו {% equation %}\exists z\left(y=n^{z}\wedge z=k^{t}\right){% endequation %}, רק באופן כללי. למעשה, אם תחשבו על כך לרגע, {% equation %}f\left(n,k,t\right)=n^{k^{t}}{% endequation %} מתקבל מהפונקציה {% equation %}h\left(n,k\right)=n^{k}{% endequation %} בעזרת הרכבה: {% equation %}f\left(n,k,t\right)=h\left(n,h\left(k,t\right)\right){% endequation %} (כלומר, מה שקראתי לו {% equation %}f{% endequation %} בהגדרה הכללית של הרכבה הוא כאן {% equation %}h{% endequation %}, ואילו {% equation %}g_{1}\left(n,k,t\right)=n{% endequation %} ו-{% equation %}g_{2}\left(n,k,t\right)=h\left(k,t\right){% endequation %}) כך שזה לא ממש מפתיע.

בואו נוסיף עוד כלל בניה של ביטויים דיופנטיים: הקשר "או", {% equation %}\vee{% endequation %}. נניח שיש לנו את הביטויים {% equation %}P,Q{% endequation %} עם פולינומים מתאימים {% equation %}p,q{% endequation %} ואנחנו רוצים למצוא פולינום עבור {% equation %}P\vee Q{% endequation %}, כלומר כזה שמתאפס אם לפחות אחד משני הפולינומים מתאפס, מה נעשה? פשוט נכפול אותם: {% equation %}pq{% endequation %}.

ואו נשלים את הבניה של אוסף הביטויים הדיופנטיים על ידי הוספה של המרכיב האחרון: כמת "לכל". בלוגיקה מסדר ראשון, הכמת {% equation %}\forall x{% endequation %} אומר "לכל {% equation %}x{% endequation %}". אפשר להכניס דבר כזה לביטויים הדיופנטיים שלנו, אבל אז עולה השאלה - איך לתרגם את זה לפולינום? יש כאן איזו שהיא סתירה מובנית - הרי הרעיון הוא שאם הביטוי מקבל ערך אמת אז כל מה שצריך הוא שיהיה <strong>קיים</strong> ערך שאפשר להציב למשתנה {% equation %}x{% endequation %} כחלק מהצבה שמאפסת את הפולינום; ומצד שני, אנחנו רוצים לטפל איכשהו ב<strong>כל</strong> הערכים האפשריים של {% equation %}x{% endequation %}. זו אינטואיציה; אם אתם רוצים לקבל אינטואיציה חזקה יותר נסו לחשוב איך לממש פולינום עבור {% equation %}\forall{% endequation %} ותראו איפה אתם נתקעים. בקיצור, תשכחו מזה אין לנו דרך לעשות משהו כזה.

מה שכן אפשר לעשות, עם זאת, הוא טוב כמעט באותה מידה: כמת {% equation %}\forall{% endequation %} <strong>חסום</strong>. אם {% equation %}z{% endequation %} הוא משתנה שקיבל ערך כלשהו, אנחנו <strong>יכולים</strong> להשתמש בכמת מהצורה {% equation %}\forall x&lt;z{% endequation %}, שפירושו "לכל ערך של {% equation %}x{% endequation %} שקטן מ-{% equation %}z{% endequation %}". איך לממש את הכמת הזה - זה עניין מסובך שידרוש מאיתנו להשתמש בפונקציה האקספוננציאלית, ואני דוחה אותו לפוסט הבא (שיהיה האחרון!). לעת עתה אני רוצה להראות איך בעזרת הכמת הזה אנחנו מסוגלים להתגבר על שני כללי הבניה שעוד נותרו לנו.

כלל הבניה הבא בתור הוא מה שקראתי לו <strong>רקורסיה פרימיטיבית</strong>. בואו נזכיר אותו, כי הוא די קשה לעיכול. בניסוח לא פורמלי, אנחנו חושבים על קלט כלשהו למשתנים {% equation %}x_{1},\dots,x_{n}{% endequation %} כאילו הוא מגדיר סדרה אינסופית {% equation %}a_{1},a_{2},a_{3},a_{4},\dots{% endequation %} שמוגדרת באופן רקורסיבי. האיבר הראשון בסדרה מחושב בדרך כלשהי מתוך {% equation %}x_{1},\dots,x_{n}{% endequation %}; בואו נקרא לדרך הזו {% equation %}f{% endequation %}, כלומר {% equation %}a_{1}=f\left(x_{1},\dots,x_{n}\right){% endequation %}. כעת, האיבר ה-{% equation %}k+1{% endequation %} בסדרה מחושב מתוך שלושה סוגי קלטים שונים: ראשית, הפרמטרים {% equation %}x_{1},\dots,x_{n}{% endequation %} שאנו לא שוכחים מהם אף פעם; שנית, האיבר הקודם בסדרה, {% equation %}a_{k}{% endequation %}; שלישית, האינדקס של האיבר הקודם בסדרה, כלומר המספר הטבעי {% equation %}k{% endequation %}. נסמן ב-{% equation %}g{% endequation %} את הפונקציה שמקבלת את שלושת הקלטים הללו: {% equation %}a_{k+1}=g\left(k,a_{k},x_{1},\dots,x_{n}\right){% endequation %}. כעת אפשר להגדיר פונקציה {% equation %}h\left(x_{1},\dots,x_{n},k\right)=a_{k}{% endequation %}.

פורמלית זה הולך כך. אנו מגדירים {% equation %}h\left(x_{1},\dots,x_{n},1\right)=f\left(x_{1},\dots,x_{n}\right){% endequation %} ולכל {% equation %}k{% endequation %} אנו מגדירים {% equation %}h\left(x_{1},\dots,x_{n},k+1\right)=g\left(k,h\left(x_{1},\dots,x_{n},k\right),x_{1},\dots,x_{n}\right){% endequation %}. זה בדיוק מה שכתבתי למעלה, רק כתוב יותר פורמלי ויותר מבלבל.

התיאור שנתתי כאן מרמז על האופן שבו אפשר למדל את הבניה הזו עם ביטוי דיופנטי. הנה הנסיון הראשון לעשות את זה:

{% equation %}y=h\left(x_{1},\dots,x_{n},k\right)\iff\exists a_{1},a_{2},\dots,a_{k}{% endequation %}

{% equation %}a_{1}=f\left(x_{1},\dots,x_{k}\right)\wedge{% endequation %}

{% equation %}a_{2}=g\left(1,a_{1},x_{1},\dots,x_{n}\right)\wedge{% endequation %}

{% equation %}a_{3}=g\left(2,a_{2},x_{1},\dots,x_{n}\right)\wedge{% endequation %}

{% equation %}\dots{% endequation %}

{% equation %}a_{k}=g\left(k-1,a_{k-1},x_{1},\dots,x_{n}\right)\wedge{% endequation %}

{% equation %}y=a_{k}{% endequation %}

התיאור הזה טוב ויפה מבחינה רעיונית, אבל <strong>הוא לא ביטוי דיופנטי</strong> חוקי. נסו רגע להבין למה - זה חמקמק למדי. הבעיה כאן היא ש<strong>אורך</strong> הביטוי הזה - כמות האיברים שמופיעים בו - תלויה בפרמטר המספרי {% equation %}k{% endequation %}, אבל זה לא מתאים למה שאנחנו צריכים לעשות - אנחנו צריכים לתת ביטוי <strong>אחד</strong>, שמטפל בכל ה-{% equation %}k{% endequation %} באותו האופן. אם לא נעשה את זה, אנחנו כבר לא תוקפים את הבעיה העשירית של הילברט אלא בעיה עוד יותר כללית (ולכן עוד יותר קשה) - להגיד אם יש פתרון למערכת משוואות דיופמנטיות שבו המשוואות עצמן תלויות בערכים של חלק מהמשתנים (ערכים שונים - משוואות שונות). אם כן, הבניה שלעיל היא לא מוצלחת כל עוד לא מצאנו דרך לכתוב אותה במסגרת הכללים הנוקשים יחסית של בניית ביטויים דיופנטיים שיש לנו.

לב הבעיה הוא בכך שכדי לתאר את הרקורסיה בשלב {% equation %}k{% endequation %} אנחנו צריכים {% equation %}k{% endequation %} משתנים, {% equation %}a_{1},\dots,a_{k}{% endequation %}, כלומר מספר משתנים שאינו קבוע אלא תלוי בפרמטר {% equation %}k{% endequation %}. אם הייתה איכשהו דרך לדחוף את כל המשתנים הללו לתוך משתנה יחיד...

וכאן הגיע הזמן להחזיר למשחק את הפונקציה שתיארתי ב<a href="http://www.gadial.net/2012/09/15/hilbert_tenth_sequence_function/">פוסט השלישי בסדרה</a>: פונקציה דיופנטית {% equation %}S\left(i,u\right){% endequation %} שהיא בעלת התכונה הבאה: לכל סדרה סופית {% equation %}a_{1},\dots,a_{k}{% endequation %} של מספרים טבעיים חיוביים, קיים {% equation %}u{% endequation %} כך ש-{% equation %}S\left(i,u\right)=a_{i}{% endequation %} לכל {% equation %}1\le i\le k{% endequation %}. במילים אחרות, {% equation %}u{% endequation %} מקודד את הסדרה {% equation %}a_{1},\dots,a_{k}{% endequation %} במלואה. בעזרת הפונקציה הזו אפשר לכתוב מחדש את הביטוי שלעיל באופן הבא:

{% equation %}y=h\left(x_{1},\dots,x_{n},k\right)\iff\exists u{% endequation %}

{% equation %}S\left(1,u\right)=f\left(x_{1},\dots,x_{k}\right)\wedge{% endequation %}

{% equation %}S\left(2,u\right)=g\left(1,S\left(1,u\right),x_{1},\dots,x_{n}\right)\wedge{% endequation %}

{% equation %}S\left(3,u\right)=g\left(2,S\left(2,u\right),x_{1},\dots,x_{n}\right)\wedge{% endequation %}

{% equation %}\dots{% endequation %}

{% equation %}S\left(k,u\right)=g\left(k-1,S\left(k-1,u\right),x_{1},\dots,x_{n}\right)\wedge{% endequation %}

{% equation %}y=S\left(k,u\right){% endequation %}

אבל, למרות שעכשיו אנחנו צריכים להניח את קיומו של משתנה יחיד {% equation %}u{% endequation %} ולא של {% equation %}k{% endequation %} משתנים, זה עדיין לא פותר לנו את הבעיה, כי הפסוק עצמו עדיין תלוי באורכו ב-{% equation %}k{% endequation %}. לכן הטוויסט האחרון הוא להשתמש בכמת "לכל":

{% equation %}y=h\left(x_{1},\dots,x_{n},k\right)\iff\exists u{% endequation %}

{% equation %}S\left(1,u\right)=f\left(x_{1},\dots,x_{k}\right)\wedge{% endequation %}

{% equation %}\forall i&lt;k\left(S\left(i+1,u\right)=g\left(i,S\left(i,u\right),x_{1},\dots,x_{n}\right)\right)\wedge{% endequation %}

{% equation %}y=S\left(k,u\right){% endequation %}

וזהו זה! זה כבר ביטוי תקין לגמרי, בהינתן שאנחנו מאמינים שאפשר להשתמש בכמת "לכל" חסום. כדאי להעיר שהתעלול הזה, של שימוש ב-{% equation %}S{% endequation %} כדי לתפוס רקורסיה בפסוק קצר אחד, הוא המצאתו של קורט גדל (עד לרמה הטכנית של בניית {% equation %}S{% endequation %} עם משפט השאריות הסיני) והוא אחד מהכלים שבהם הוא השתמש בהוכחה המבריקה שלו של משפט אי השלמות הראשון.

אם כן, סיימנו עם הרקורסיה הפרימיטיבית ומותיר לנו רק את כלל היצירה האחרון: מינימיזציה.

כזכור, מינימיזציה הולכת כך:

{% equation %}h\left(x_{1},\dots,x_{n}\right)=\min_{y}\left(f\left(x_{1},\dots,x_{n},y\right)=g\left(x_{1},\dots,x_{n},y\right)\right){% endequation %}

כלומר, {% equation %}h{% endequation %} מחזירה את הערך המינימלי של {% equation %}y{% endequation %} שכאשר מזינים אותו (יחד עם שאר הפרמטרים {% equation %}x_{1},\dots,x_{N}{% endequation %}) הן ל-{% equation %}f{% endequation %} והן ל-{% equation %}g{% endequation %} מקבלים את אותה התוצאה. אם אין {% equation %}y{% endequation %} שעבורו זה קורה, {% equation %}h{% endequation %} פשוט לא מוגדרת על {% equation %}x_{1},\dots,x_{n}{% endequation %}.

לתרגם את הפונקציה הזו לביטוי יהיה קל יותר מאשר רקורסיה. נתחיל מכך ש-{% equation %}f\left(x_{1},\dots,x_{n},y\right)=g\left(x_{1},\dots,x_{n},y\right){% endequation %} הוא ביטוי לגיטימי למהדרין. כל מה שנשאר לעשות הוא לקודד איכשהו את תכונת המינימליות. כלומר, אנחנו רוצים להגיד שאין איזה {% equation %}t&lt;y{% endequation %} כך ש-{% equation %}f\left(x_{1},\dots,x_{n},t\right)=g\left(x_{1},\dots,x_{n},t\right){% endequation %}. הכמת החסום בנוי בדיוק עבור זה:

{% equation %}y=h\left(x_{1},\dots,x_{n}\right)\iff f\left(x_{1},\dots,x_{n},y\right)=g\left(x_{1},\dots,x_{n},y\right)\wedge{% endequation %}

{% equation %}\wedge\forall t&lt;y\left(f\left(x_{1},\dots,x_{n},t\right)\ne g\left(x_{1},\dots,x_{n},t\right)\right){% endequation %}

דבר אחד שעדיין צריך להסביר הוא איך לתאר את {% equation %}f\ne g{% endequation %}. זה פשוט קיצור של {% equation %}\left(f&gt;g\right)\vee\left(f&lt;g\right){% endequation %}, ולכן כל מה שנותר לעשות הוא להשתכנע שאפשר להשתמש ב-{% equation %}&lt;{% endequation %}, אבל זה אחד מהדברים הראשונים שהראיתי: כדי לתאר את {% equation %}x&lt;y{% endequation %} משתמשים במשוואה הדיופנטית {% equation %}x+z=y{% endequation %}. וזהו! סיימנו את ההוכחה של אי-כריעות הבעיה העשירית של הילברט!

...פרט לכך שעדיין לא הוכחנו שאפשר לקודד את הכמת "לכל" החסום. זה יהיה תוכן הפוסט הבא, האחרון בסדרה.
