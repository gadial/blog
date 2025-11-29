---
id: 3780
title: "משפט הערך הממוצע של לגראנז'"
date: 2019-06-17 14:59:37
layout: post
categories: 
  - אנליזה מתמטית
tags: 
  - כלל לופיטל
  - משפט הערך הממוצע של לגראנז'
  - משפט הערך הממוצע של קושי
  - משפט רול
social_media_share: true
---
ביקשו ממני לסגור את אחד החורים המציקים שיש בבלוג - לתאר את <strong>משפט הערך הממוצע </strong>של לגראנז', שהוא אחד מהתוצאות הבסיסיות והמעניינות ביותר שמלמדים על <strong>נגזרות</strong>. כתבתי בשעתו <a href="https://gadial.net/2010/11/21/derivative/">פוסט שמתאר מהן נגזרות</a> והוא הרקע שדרוש כדי להבין את משפט לגראנז'; אבל אל לגראנז' עצמו לא הגעתי. אז נתחיל עם תזכורת קטנה על מה מדובר.

אנחנו מדברים על <strong>פונקציות ממשיות</strong>: פונקציות {% equation %}f:\mathbb{R}\to\mathbb{R}{% endequation %}. אם יש לנו מספיק מזל, הפונקציות הללו הן "נחמדות", והקצב שבו הן משתנות ניתן גם הוא לתיאור על ידי פונקציה, שנקראת <strong>הנגזרת</strong> של {% equation %}f{% endequation %}. פורמלית, אנחנו מגדירים את הנגזרת של {% equation %}f{% endequation %} בנקודה {% equation %}a{% endequation %} בתור הערך של הגבול {% equation %}\lim_{h\to0}\frac{f\left(a+h\right)-f\left(a\right)}{h}{% endequation %}, במקרה שבו הוא קיים. בואו נסתכל שניה על הביטוי הזה יותר בפירוט כדי להבין מה הוא אומר: אפשר לכתוב אותו גם בתור

{% equation %}\lim_{h\to0}\frac{f\left(a+h\right)-f\left(a\right)}{\left(a+h\right)-a}{% endequation %}

כלומר, אפשר לחשוב עליו בתור הערך {% equation %}\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %} עבור נקודות {% equation %}b{% endequation %} שהן "הולכות וקרבות" ל-{% equation %}a{% endequation %}. אבל מה זה הערך הזה? זה פשוט <strong>השינוי הממוצע</strong> בין הערך של {% equation %}f{% endequation %} בנקודה {% equation %}a{% endequation %} והערך שלה בנקודה {% equation %}b{% endequation %}. קל לראות את זה עם דוגמא יומיומית: נניח שאנחנו נוסעים מתל אביב לאילת ומודדים כמה התרחקנו מתל אביב עד כה בעזרת הפונקציה {% equation %}f{% endequation %}. אם בזמן {% equation %}t_{1}=1{% endequation %} (בשעות) היינו במרחק 50 ק"מ מתל אביב ובזמן {% equation %}t_{2}=4{% endequation %} היינו במרחק 290 ק"מ מתל אביב, אז <strong>המהירות הממוצעת</strong> שלנו בנסיעה הזו בין שני פרקי הזמן הללו נתונה, בקילומטר לשעה, על ידי

{% equation %}\frac{f\left(t_{2}\right)-f\left(t_{1}\right)}{t_{2}-t_{1}}=\frac{290-50}{4-1}=\frac{240}{3}=80{% endequation %}

מה המשמעות של מהירות ממוצעת שכזו? האם זה אומר שזו המהירות שבה נסענו במשך רוב הדרך? לא. ייתכן שנסענו במהירות 100 קמ"ש בשעתיים הראשונות שאחרי {% equation %}t_{1}=1{% endequation %}, ואז את 40 הקילומטרים הנוספים עשינו בזחילה במהירות 40 קמ"ש בשעה האחרונה. המשמעות של המהירות הממוצעת היא זו - אם היינו נוסעים כל הדרך באותה מהירות בדיוק, בלי לשנות אותה כלל, אז היינו עוברים את אותה הדרך.

על נגזרת אפשר לחשוב בתור "ערך ממוצע רגעי". כלומר, אנחנו מחשבים את המהירות הממוצעת שלנו לא על פני פרק זמן של שלוש שעות אלא על פני פרק זמן של דקה... לא בעצם, פרק זמן של שנייה... לא, בעצם מילישנייה... וכן הלאה. אם יש איזו מהירות מסויימת שהמהירות הממוצעת מספיק קרובה אליה, בהינתן שפרק הזמן שלנו קצר דיו (זה היה ניסוח מילולי מסורבל של מושג ה<strong>גבול</strong>, {% equation %}\lim{% endequation %}), אז המהירות המסויימת הזו היא <strong>הנגזרת</strong> של פונקציית המיקום שלנו באותה נקודת זמן שאנחנו לוקחים ממנה פער כל כך קצרצר. בהקשר של מהירות קוראים לזה <strong>מהירות רגעית</strong>.

כפי שאפשר להבין, מהירות רגעית שכזו היא עניין, אה, רגעי. מקומי. נקודתי. משהו שמתאר שבריר שניה אחד בהיסטוריה של הנסיעה. מה שמשפט הערך הממוצע של לגראנז' עושה הוא להעביר אותנו מהמקומי הזה אל <strong>הגלובלי</strong> - להראות שקיימת נקודה רגעית בזמן שמה שקורה בה הוא האפיון הממוצע של מה שקורה בכל פרק הזמן הרלוונטי. זה מתאים לחוויה היומיומית שלנו: אם בהתחלה נסענו במהירות ממוצעת של 100 קמ"ש ואז ירדנו למהירות ממוצעת של 40 קמ"ש, אז היה שבריר שניה כלשהו שבו מד המהירות שלנו הראה את המהירות 80 קמ"ש, שהיא המהירות הממוצעת עבור כל הנסיעה.

אז הנה מה שלגראנז' אומר, פורמלית: אם {% equation %}a&lt;b{% endequation %} ויש לנו פונקציה {% equation %}f:\left[a,b\right]\to\mathbb{R}{% endequation %} פונקציה שרציפה בקטע הסגור {% equation %}\left[a,b\right]{% endequation %} וגזירה בקטע הפתוח {% equation %}\left(a,b\right){% endequation %}, אז קיימת נקודה {% equation %}c\in\left(a,b\right){% endequation %} כך ש-{% equation %}f^{\prime}\left(c\right)=\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %}. בפוסט הזה נוכיח את המשפט (בהסתמך על דברים קודמים, כמובן) וניתן דוגמא או שתיים לשימושיות שלו.

ראשית, אי אפשר בלי להזכיר את האופן הגאומטרי שבו אנחנו רואים את המשפט. כשאנחנו מציירים פונקציה, אנחנו מציירים נקודות שהקואורדינטות שלהן הן מהצורה {% equation %}\left(x,f\left(x\right)\right){% endequation %} (כלומר, {% equation %}f\left(x\right){% endequation %} היא קואורדינטת ה-{% equation %}y{% endequation %} של הציור). נקודות הקצה של הפונקציה הן {% equation %}\left(a,f\left(a\right)\right){% endequation %} ו-{% equation %}\left(b,f\left(b\right)\right){% endequation %}. אם ניזכר איך הולכים דברים בגאומטריה אנליטית נראה שהביטוי {% equation %}\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %} הוא <strong>שיפוע הישר</strong> שמחבר את שתי הנקודות הללו. עכשיו, מה זו נגזרת? המשמעות של נגזרת בנקודה כלשהי היא <strong>שיפוע המשיק</strong> לפונקציה בנקודה הזו. לכן לגראנז' אומר שיש נקודה כלשהי על גרף הפונקציה ששיפוע המשיק לאותה נקודה זהה לשיפוע הישר שמחבר את שני קצוות הפונקציה. הנה איור באדיבות ויקיפדיה העברית:

<img class="alignnone size-full wp-image-3781" src="{{site.baseurl}}{{site.post_images}}/2019/06/Mv4_he.svg_.png" alt="" width="1024" height="931" />

איך מוכיחים את המשפט? כאן צריך להיזהר עם האינטואיציה שלנו, שעשויה להטעות אותנו. נחזור אל דוגמת הרכב שנסע במהירות של 100 קמ"ש ואז ירד למהירות של 40 קמ"ש. האינטואיציה שלנו אומרת שבירידה מ-100 קמ"ש אל 40 קמ"ש הייתה חייבת להיות שניה שבה המהירות הייתה 80 קמ"ש, כי אנחנו חושבים על מהירות בתור משהו ש<strong>משתנה באופן רציף</strong>. יש לדבר הזה פורמליזם בחדו"א: פונקציה {% equation %}f{% endequation %} היא <strong>רציפה</strong> בנקודה {% equation %}a{% endequation %} אם {% equation %}\lim_{x\to a}f\left(x\right)=f\left(a\right){% endequation %} (כלומר, הערך שנראה ש-{% equation %}f{% endequation %} "אמורה לקבל" ב-{% equation %}a{% endequation %} הוא מה שמתקבל בפועל). אם יש לנו פונקציה רציפה, אז יש לנו עבורה משהו שנקרא <strong>משפט ערך הביניים</strong> שאומר שאם {% equation %}y{% endequation %} הוא ערך כלשהו שנמצא בין {% equation %}f\left(a\right){% endequation %} ו-{% equation %}f\left(b\right){% endequation %}, אז קיים {% equation %}x\in\left[a,b\right]{% endequation %} כך ש-{% equation %}f\left(x\right)=y{% endequation %}. בפרט, מהירות של 80 קמ"ש נמצאת בין 100 קמ"ש ו-40 קמ"ש ולכן היא חייבת להתקבל מתישהו.

אז מה הבעיה? הבעיה היא שנגזרת, באופן כללי, לא חייבת להיות פונקציה רציפה. אמנם, הדוגמאות הנגדיות (של פונקציות גזירות שהנגזרת שלהן אינה רציפה) הן לא יפות במיוחד ואפשר גם להוכיח שאי רציפות של "קפיצה" ישירות מ-100 קמ"ש אל 40 קמ"ש פשוט לא יכולה להתקיים, אבל השורה התחתונה היא שאנחנו רוצים להוכיח את המשפט בלי הסתמכות על משפט ערך הביניים.

עוד נקודה שצריך לתת אליה תשומת לב היא שהתנאים של המשפט די קשיחים. ראשית, הדרישה ש-{% equation %}f{% endequation %} תהיה גזירה בכל הקטע הפתוח {% equation %}\left(a,b\right){% endequation %}. אחרת אפשר לקחת את דוגמת הנסיעה שלנו לאקסטרים: נדמיין שאנחנו נוסעים 100 קמ"ש ואז <strong>קופצים מיידית</strong> אל 40 קמ"ש, בלי לעבור בערכים באמצע; אז באמת לא היינו בשום מקום במהירות 80 קמ"ש כפי שמשפט לגראנז' טוען. העניין הוא שהנקודה שבה ביצענו את הקפיצה הזו לא תהיה גזירה; הנגזרת ממש לפניה היא 100 והנגזרת ממש אחריה היא 40, ובנקודה עצמה? הנגזרת לא מוגדרת.

שנית, הדרישה הנוספת ש-{% equation %}f{% endequation %} תהיה רציפה בכל {% equation %}\left[a,b\right]{% endequation %} היא כמעט מובנת מאליה. היא חייבת להיות רציפה ב-{% equation %}\left(a,b\right){% endequation %} כי קל לראות שגזירות בקטע הזה גוררת רציפות בו. היא חייבת להיות רציפה בקצוות, אחרת אפשר יהיה לשנות את הערכים שלה שם באופן שרירותי לגמרי, למשל להגדיר {% equation %}f\left(a\right)=f\left(b\right)=232352{% endequation %}, ואז אין סיבה שמשפט ערך הביניים יעבוד כי הוא מתבסס בצורה חזקה על הערכים בקצוות ועל כך שהם מייצגים תקינים של מה שקורה בתוך הקטע.

עכשיו אפשר לעבור להוכחה של המשפט. נתחיל עם מקרה פרטי שלו שנקרא <strong>משפט רול</strong> שבעזרתו קל להוכיח את התוצאה הכללית. משפט רול אומר שאם {% equation %}f\left(a\right)=f\left(b\right){% endequation %} אז קיימת {% equation %}c\in\left[a,b\right]{% endequation %} כך ש-{% equation %}f^{\prime}\left(c\right)=0{% endequation %}. אינטואיטיבית, אם נקודות ההתחלה והסיום של הטיול שלנו הן זהות, אז היה רגע שבו עמדנו במקום ולא זזנו.

זה לא משפט טריוויאלי, אבל עם ידע רלוונטי בחדו"א אפשר לתת לו הוכחה של שורה אחת, שהאינטואיציה שלה די ברורה: אם נקודות ההתחלה והסיום שלנו זהות, אז או שלא זזנו בכלל כל הזמן, או שזזנו קדימה ואז אחורה ולכן הייתה שניה שבה עברנו מלזוז קדימה אל לזוז אחורה ובה לא זזנו; או שזזנו אחורה ואז קדימה ולכן הייתה שניה שבה לא זזנו. העניין הוא שהאינטואיציה הזו שוב מניחה רציפות של הנגזרת ובפעול משפט רול מצליח לעקוף את זה (ולכן אינו טריוויאלי) בעזרת משפטים קודמים, שרק בזכותם ההוכחה היא בת שורה אחת.

בואו ניתן את השורה הזו למקרה שיש לכם את הידע הזה ואז נרחיב: מכיוון ש-{% equation %}f{% endequation %} רציפה ב-{% equation %}\left[a,b\right]{% endequation %} היא מקבלת בקטע הזה מקסימום ומינימום. אם הם בתוך הקטע, אז בכל אחד מהם ערך הנגזרת הוא 0 על פי משפט פרמה לנקודות קיצון; אם שניהם בקצוות הקטע אז הם שווים זה לזה ולכן הפונקציה קבועה ולכן הנגזרת שלה היא 0 בכל הקטע.

הבעיה עם להסביר את כל המלל שכתבתי למעלה היא שלא ברור כמה רחוק אני אמור ללכת. את הטענה על משפט פרמה לנקודות קיצון <a href="https://gadial.net/2011/01/16/derivative_and_extremal_problems_1-2/">הוכחתי בפוסט קודם</a>, אז אני פטור מלדבר עליה, אבל מה עם הטענה שפונקציה רציפה בקטע סגור מקבלת בו ערכי מקסימום ומינימום? הטענה הזו נקראת בחדו"א "משפט ויירשטראס" (השני; הראשון אומר שפונקציה רציפה בקטע סגור חסומה בו). אני יכול להוכיח אותה, אבל ההוכחה מתבססת על משהו יותר בסיסי שנקרא <strong>משפט בולצאנו-ויירשטראס</strong>, שבתורו נובע מהתכונות הבסיסיות של הממשיים... בקיצור, אני לא הולך ללכת בכיוון הזה ואולי אדבר על משפטי ויירשטראס בפירוט בפוסט אחר מתישהו.

דבר אחד כן קל מאוד להסביר: אם {% equation %}f{% endequation %} היא פונקציה קבועה בקטע, אז הנגזרת שלה בכל נקודה בקטע היא {% equation %}0{% endequation %} פשוט כי בביטוי {% equation %}\lim_{h\to0}\frac{f\left(a+h\right)-f\left(a\right)}{h}{% endequation %} מתקיים {% equation %}f\left(a+h\right)=f\left(a\right){% endequation %} ולכן המונה הוא אפס.

עכשיו, איך עוברים מהמשפט הזה אל משפט לגראנז'? די בקלות: אם יש לנו פונקציה {% equation %}f\left(x\right){% endequation %}, אפשר לדבר על הפונקציה {% equation %}g\left(x\right){% endequation %} שמודדת את <strong>המרחק</strong> של {% equation %}f\left(x\right){% endequation %} מהמיתר שמחבר את הנקודות {% equation %}\left(a,f\left(a\right)\right){% endequation %} ו-{% equation %}\left(b,f\left(b\right)\right){% endequation %}. כלומר, היא מודדת כמה {% equation %}f\left(x\right){% endequation %} <strong>אינה</strong> מתאימה לממוצע בנקודה מסויימת. בנקודות הקצה המרחק הזה יהיה 0, כך שאנחנו רואים את משפט רול בפעולה.

כדי לכתוב את {% equation %}g\left(x\right){% endequation %} במפורש צריך להיזכר קודם כל בקצת גאומטריה אנליטית - איך כותבים את משוואות הקו הישר שמחבר שתי נקודות {% equation %}\left(x_{1},y_{1}\right),\left(x_{2},y_{2}\right){% endequation %}? התשובה היא שזו תהיה משוואה מהצורה {% equation %}y=mx+n{% endequation %} כאשר {% equation %}m{% endequation %} נקרא <strong>השיפוע</strong> של הישר ואילו {% equation %}n{% endequation %} היא נקודת החיתוך של הישר עם ציר {% equation %}y{% endequation %} (כמה "גבוה" הישר יהיה כשנציב {% equation %}x=0{% endequation %}). אם נציב את שתי הנקודות שידועות לנו במשוואה הזו נקבל שתי משוואות:

{% equation %}y_{1}=mx_{1}+n{% endequation %}

{% equation %}y_{2}=mx_{2}+n{% endequation %}

אם נחסר אחת מהשניה ונחלק, נקבל

{% equation %}m=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}{% endequation %}

כאן אנחנו מניחים ש-{% equation %}x_{2}\ne x_{1}{% endequation %} כדי שנוכל לחלק, וזה מתאים להנחה שלנו ש-{% equation %}a&lt;b{% endequation %} במשפט לגראנז' (אם לא היינו מניחים את זה אז משפט לגרנז' היה חסר משמעות; הוא היה אומר שקיים {% equation %}x\in\left(a,b\right){% endequation %} שמקיים כך-וכך, אבל {% equation %}\left(a,b\right){% endequation %} היה קטע ריק).

את הערך של {% equation %}n{% endequation %} קל למצוא עכשיו על ידי כך שניקח את המשוואה הראשונה ונעביר אגף: {% equation %}y_{1}-mx_{1}=n{% endequation %}. אם נציב את זה בחזרה במשוואה הכללית {% equation %}y=mx+n{% endequation %} נקבל

{% equation %}y=mx+\left(y_{1}-mx_{1}\right){% endequation %}

כלומר

{% equation %}y=m\left(x-x_{1}\right)+y_{1}{% endequation %}

במקרה שלנו, שבו {% equation %}\left(x_{1},y_{1}\right)=\left(a,f\left(a\right)\right){% endequation %} ו-{% equation %}\left(x_{2},y_{2}\right)=\left(b,f\left(b\right)\right){% endequation %}, משוואת המיתר תהיה

{% equation %}y=\frac{f\left(b\right)-f\left(a\right)}{b-a}\left(x-a\right)+f\left(a\right){% endequation %}

ולכן אם אנחנו רוצים ש-{% equation %}g\left(x\right){% endequation %} תתאר את <strong>ההפרש</strong> בין הערך של המיתר והפונקציה, כלומר {% equation %}f\left(x\right)-y{% endequation %}, נקבל:

{% equation %}g\left(x\right)=f\left(x\right)-\frac{f\left(b\right)-f\left(a\right)}{b-a}\left(x-a\right)-f\left(a\right){% endequation %}

אם נציב {% equation %}x=a{% endequation %} במשוואה הזו נקבל

{% equation %}g\left(a\right)=f\left(a\right)-f\left(a\right)=0{% endequation %}

ואם נציב בה {% equation %}b{% endequation %} נקבל

{% equation %}g\left(b\right)=f\left(b\right)-\left(f\left(b\right)-f\left(a\right)\right)-f\left(a\right)=0{% endequation %}

בנוסף לכך, {% equation %}g{% endequation %} רציפה ב-{% equation %}\left[a,b\right]{% endequation %} וגזירה ב-{% equation %}\left(a,b\right){% endequation %} בשל האופן הפשוט שבו היא מתקבלת מ-{% equation %}f\left(x\right){% endequation %} שגם כן מקיימת את התכונות הנחמדות הללו; זאת מכיוון שחיבור של פונקציות גזירות או כפל שלהן בקבוע מותיר אותן גזירות, וכמו כן פולינומים הם פונקציות גזירות.

לכן ניתן להשתמש במשפט רול על {% equation %}g{% endequation %} ולקבל שיש {% equation %}c\in\left(a,b\right){% endequation %} כך ש-{% equation %}g^{\prime}\left(c\right)=0{% endequation %}. כעת, מהי הנגזרת של {% equation %}g{% endequation %}? קל לחשוב אותה במפורש:

{% equation %}g^{\prime}\left(x\right)=f^{\prime}\left(x\right)-\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %}

ולכן אם {% equation %}g^{\prime}\left(c\right)=0{% endequation %} נקבל ש-

{% equation %}f^{\prime}\left(c\right)-\frac{f\left(b\right)-f\left(a\right)}{b-a}=0{% endequation %}

כלומר {% equation %}f^{\prime}\left(c\right)=\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %} שזה בדיוק מה שרצינו. האינטואיציה פה שוב פשוטה ונובעת ממה שנקרא <strong>לינאריות הנגזרת</strong>, {% equation %}\left(f+g\right)^{\prime}=f^{\prime}+g^{\prime}{% endequation %}: מכיוון ש-{% equation %}g{% endequation %} היא ההפרש בין {% equation %}f{% endequation %} ובין המיתר, אז הנגזרת של {% equation %}g{% endequation %} היא ההפרש בין הנגזרת של {% equation %}f{% endequation %} ובין נגזרת המיתר, שהיא פשוט השיפוע הקבוע של המיתר. לכן יש נקודה שבה ההפרש הזה מתאפס, והנגזרת של {% equation %}f{% endequation %} שווה בדיוק לשיפוע המיתר.

סיימנו להוכיח את המשפט, אבל מן הסתם פוסט בנושא לא יהיה שלם בלי לראות כמה מהשימושים הפשוטים שלו. כאמור, הרעיון במשפט הזה הוא היכולת לעבור מה"מקומי" (הנגזרת) אל ה"גלובלי" (ההתנהגות של הפונקציה בכל הקטע), ובמקרי קצה פשוטים יש כמה הסקות מיידיות שניתן לבצע:
<ol>
 	<li>אם הנגזרת של {% equation %}f{% endequation %} היא 0 בקטע כלשהו אז {% equation %}f{% endequation %} קבועה בכל הקטע הזה (קודם ראינו את ההפך - שהנגזרת של פונקציה קבועה היא 0; עכשיו אנחנו רואים שזה קורה רק לפונקציות קבועות)</li>
 	<li>אם הנגזרת של {% equation %}f{% endequation %} היא <strong>חיובית</strong> בקטע כלשהו אז {% equation %}f{% endequation %} היא <strong>עולה ממש</strong> בכל הקטע הזה.</li>
 	<li>אם הנגזרת של {% equation %}f{% endequation %} היא <strong>שלילית </strong>בקטע כלשהו אז {% equation %}f{% endequation %} היא <strong>יורדת ממש</strong> בכל הקטע הזה.</li>
</ol>
שלושת אלו הם מה שנדרש לנו לצורך "חקירת פונקציות" כמו שלומדים בתיכון - זיהוי תחומי עליה וירידה של פונקציה. כדי לראות שזה נכון, אנחנו לוקחים שתי נקודות כלשהן בתוך הקטע, נקרא להן {% equation %}a,b{% endequation %}, כך ש-{% equation %}a&lt;b{% endequation %}. עכשיו:
<ol>
 	<li>אם {% equation %}f{% endequation %} קבועה בכל הקטע אנחנו מצפים שיתקיים {% equation %}f\left(a\right)=f\left(b\right){% endequation %}</li>
 	<li>אם {% equation %}f{% endequation %} עולה ממש בכל הקטע אנחנו מצפים שיתקיים {% equation %}f\left(a\right)&lt;f\left(b\right){% endequation %}</li>
 	<li>אם {% equation %}f{% endequation %} יורדת ממש בכל הקטע אנחנו מצפים שיתקיים {% equation %}f\left(a\right)&gt;f\left(b\right){% endequation %}</li>
</ol>
שלושת אלו אכן מתקיימים, בזכות משפט הערך הממוצע. כזכור, הוא אומר שקיימת {% equation %}c\in\left(a,b\right){% endequation %} כך ש-{% equation %}f^{\prime}\left(c\right)=\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %}. אולי קצת יותר קל להרגיש מה קורה אם כופלים ב-{% equation %}b-a{% endequation %} ומקבלים

{% equation %}f\left(b\right)-f\left(a\right)=f^{\prime}\left(c\right)\left(b-a\right){% endequation %}

כלומר, אנחנו יכולים לתאר את ההפרש בין {% equation %}f{% endequation %} בשתי נקודות הקצה של הקטע בעזרת אורך הקטע כפול קבוע מספרי כלשהו שקשור לנגזרת של {% equation %}f{% endequation %}. נחזור אל שלושת המקרים שלנו:
<ol>
 	<li>אם הנגזרת של {% equation %}f{% endequation %} היא 0 בכל הקטע אז {% equation %}f^{\prime}\left(c\right)=0{% endequation %} ולכן {% equation %}f\left(b\right)-f\left(a\right)=0{% endequation %}, כלומר {% equation %}f\left(b\right)=f\left(a\right){% endequation %}</li>
 	<li>אם הנגזרת של {% equation %}f{% endequation %} היא חיובית בכל הקטע אז {% equation %}f^{\prime}\left(c\right)\left(b-a\right)&gt;0{% endequation %} ולכן {% equation %}f\left(b\right)-f\left(a\right)&gt;0{% endequation %}, כלומר {% equation %}f\left(a\right)&lt;f\left(b\right){% endequation %}</li>
 	<li>אם הנגזרת של {% equation %}f{% endequation %} היא שלילית בכל הקטע אז {% equation %}f^{\prime}\left(c\right)\left(b-a\right)&lt;0{% endequation %} ולכן {% equation %}f\left(b\right)-f\left(a\right)&lt;0{% endequation %}, כלומר {% equation %}f\left(a\right)&gt;f\left(b\right){% endequation %}</li>
</ol>
העובדה שאם הנגזרת של {% equation %}f{% endequation %} היא אפס בקטע אז {% equation %}f{% endequation %} היא קבועה היא הבסיס לעוד טענה מעניינת: אם הנגזרת של שתי פונקציות היא זהה, אז הן <strong>נבדלות בקבוע</strong> ותו לא. בואו נראה את זה: נניח ש-{% equation %}f^{\prime}\left(x\right)=g^{\prime}\left(x\right){% endequation %} לכל {% equation %}x{% endequation %} בקטע מסויים, אז {% equation %}\left(f-g\right)^{\prime}\left(x\right)=0{% endequation %} לכל הנקודות בקטע הזה, ומכאן ש-{% equation %}f-g{% endequation %} היא פונקציה קבועה: {% equation %}\left(f-g\right)\left(x\right)=c{% endequation %} עבור {% equation %}c\in\mathbb{R}{% endequation %} כלשהו בקטע, כלומר {% equation %}f\left(x\right)=g\left(x\right)+c{% endequation %}. זו אולי התוצאה הבסיסית ביותר שמכירים כשמדברים על <strong>אינטגרלים</strong>: שאם מצאנו פונקציה קדומה של משהו, אז הפונקציות הקדומות הנוספות מתקבלות ממנה על ידי חיבור קבוע כלשהו.

לסיום הפוסט אני רוצה להוכיח משפט מועיל מאין כמותו - <strong>כלל לופיטל</strong>. יש פה קוריוז היסטורי קטן: לופיטל לא גילה או הוכיח את המשפט אלא יוהאן ברנולי עשה את זה (ולופיטל, תלמידו, פרסם אותו בספר שכתב וקיבל את הקרדיט; סוג של קניה בכסף של משפט שייקרא על שמך), ואני הולך להוכיח אותו עם משהו שנקרא "משפט הערך הממוצע של קושי" שחי הרבה אחרי לופיטל וברנולי (אין לי מושג איך ברנולי הוכיח את המשפט).

כלל לופיטל הוא שיטה מועילה לחישוב <strong>גבולות</strong> שהם מנה שבה המונה והמכנה שואפים שניהם לאפס (ועם קצת עבודה אפשר להשתמש בו עבור עוד סוגי גבולות בעייתיים אבל לא אכנס לכך בפוסט הזה). פורמלית, אם {% equation %}f,g{% endequation %} הן פונקציות ממשיות ו-{% equation %}a{% endequation %} מספר ממשי כלשהו כך ש-{% equation %}\lim_{x\to a}f\left(x\right)=\lim_{x\to a}g\left(x\right)=0{% endequation %}, ואם בנוסף לכך הגבול הבא קיים:

{% equation %}\lim_{x\to a}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %}

אז גם הגבול הבא קיים:

{% equation %}\lim_{x\to a}\frac{f\left(x\right)}{g\left(x\right)}{% endequation %}

והם שווים, כלומר {% equation %}\lim_{x\to a}\frac{f\left(x\right)}{g\left(x\right)}=\lim_{x\to a}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %}

המשמעות של הכלל היא שאם יש לנו גבול קשה לחישוב, למשל {% equation %}\lim_{x\to0}\frac{\sin x}{x}{% endequation %}, אז אפשר לנסות לפשט אותו על ידי גזירת המונה והמכנה; אם נצליח למצוא את הגבול המתאים עבור הנגזרות, ינבע מכך הגבול המקורי. בדוגמה שלנו גזירת המונה והמכנה מניבה את

{% equation %}\lim_{x\to0}\frac{\cos x}{1}=1{% endequation %}

(יש בדוגמא שלי מעגליות מכוונת: כדי לדעת מהי הנגזרת של {% equation %}\sin{% endequation %} כבר צריך להכיר את הערך של הגבול הזה; יש לי על כך <a href="https://gadial.net/2008/01/20/lim_sin_x_over_x/">פוסט כאן</a>)

איך מוכיחים את הכלל? בשביל זה אני צריך, כאמור, הכללה של משפט הערך הממוצע של לגראנז' שנקראת משפט הערך הממוצע של קושי. אם בלגראנז' הרעיון הוא שקיים {% equation %}c{% endequation %} עבורו מתקיים

{% equation %}f^{\prime}\left(c\right)=\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %}

אז במשפט קושי הרעיון הוא שקיים {% equation %}c{% endequation %} עבורו מתקיים

{% equation %}\frac{f^{\prime}\left(c\right)}{g^{\prime}\left(c\right)}=\frac{f\left(b\right)-f\left(a\right)}{g\left(b\right)-g\left(a\right)}{% endequation %}

עבור פונקציה {% equation %}g{% endequation %} שמקיימת את אותם תנאים כמו של {% equation %}f{% endequation %} (רציפה ב-{% equation %}\left[a,b\right]{% endequation %} וגזירה ב-{% equation %}\left(a,b\right){% endequation %}) ובנוסף לכך החלוקה בה ובנגזרתה לא עושה צרות - כלומר, {% equation %}g\left(a\right)\ne g\left(b\right){% endequation %} ו-{% equation %}g^{\prime}\left(x\right)\ne0{% endequation %} לכל {% equation %}x\in\left(a,b\right){% endequation %}. לגראנז' הוא מקרה פרטי של זה עבור פונקציית הזהות {% equation %}g\left(x\right)=x{% endequation %}.

למען האמת, הניסוח לעיל של משפט קושי הוא קצת מעצבן; במקום שיהיה לנו משפט סימטרי ונחמד יש לנו את כל הדרישות הנוספות המעיקות על {% equation %}g{% endequation %}. אפשר להיפטר מהקושי הזה אם נפטרים מהחלוקה. כלומר, ניסוח "טוב יותר" של משפט קושי הוא שאם {% equation %}f,g{% endequation %} רציפות על {% equation %}\left[a,b\right]{% endequation %} וגזירות על {% equation %}\left(a,b\right){% endequation %} אז קיים {% equation %}c\in\left(a,b\right){% endequation %} כך ש-

{% equation %}f^{\prime}\left(c\right)\left(g\left(b\right)-g\left(a\right)\right)=g^{\prime}\left(c\right)\left(f\left(b\right)-f\left(a\right)\right){% endequation %}

איך מוכיחים את המשפט? על פניו אפשר לומר משהו כזה: נשתמש פעמיים במשפט לגראנז' ונקבל ש-

{% equation %}f^{\prime}\left(c\right)=\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %}

{% equation %}g^{\prime}\left(c\right)=\frac{g\left(b\right)-g\left(a\right)}{b-a}{% endequation %}

ועכשיו פשוט נכפול את אגף ימין של המשוואה האחת באגף שמאל של השניה, ואת אגף שמאל של השניה באגף ימין של הראשונה, ונצמצמם {% equation %}\frac{1}{b-a}{% endequation %} משני האגפים. זה נשמע מאוד פשוט ואלגנטי ונחמד וזה גם <strong>שגוי מאוד</strong> בצורה שכדאי לתת עליה את הדעת כי זו טעות מאוד נפוצה במתמטיקה. רואים אותה? קחו רגע לחשוב על זה.

השגיאה היא בכך שכתבתי

{% equation %}f^{\prime}\left(c\right)=\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %}

{% equation %}g^{\prime}\left(c\right)=\frac{g\left(b\right)-g\left(a\right)}{b-a}{% endequation %}

כך שבשתי המשוואות הללו מופיע <strong>אותו</strong> ערך {% equation %}c{% endequation %}. זה <strong>לא</strong> מה שמשפט הערך הממוצע של לגראנז' מבטיח! הוא מבטיח שעבור {% equation %}f{% endequation %} קיים קבוע {% equation %}c_{f}{% endequation %} כך ש-{% equation %}f^{\prime}\left(c_{f}\right)=\frac{f\left(b\right)-f\left(a\right)}{b-a}{% endequation %}, ועבור {% equation %}g{% endequation %} קיים קבוע {% equation %}c_{g}{% endequation %} כך ש-{% equation %}g^{\prime}\left(c_{g}\right)=\frac{g\left(b\right)-g\left(a\right)}{b-a}{% endequation %}, אבל שום דבר לא מבטיח לנו {% equation %}c_{f}=c_{g}{% endequation %}; אנחנו צריכים איכשהו להפעיל את משפט לגראנז' <strong>סימולטנית</strong> לשתי הפונקציות הללו ביחד, ואין לנו את זה.

העניין הוא שלא צריך להסתבך עם לגראנז, בכלל, הנה הוכחה ישירה בעזרת משפט רול שוב (רואים? משפט רול <strong>יעיל</strong>! הוא בעצם מקפל בתוכו את כל החדו"א המורכב שנלמד עד לשלב הזה, ומרגע שיש לנו אותו צריך רק תעלולים פשוטים). נגדיר פונקציה

{% equation %}h\left(x\right)=f\left(x\right)\left(g\left(b\right)-g\left(a\right)\right)-g\left(x\right)\left(f\left(b\right)-f\left(a\right)\right){% endequation %}

כלומר, מאוד דומה לייצוג של המשוואה שאנחנו רוצים שתתקיים בסוף. כעת קל לראות ש-{% equation %}h{% endequation %} היא רציפה ב-{% equation %}\left[a,b\right]{% endequation %} וגזירה ב-{% equation %}\left(a,b\right){% endequation %} והנגזרת שלה היא

{% equation %}h^{\prime}\left(x\right)=f^{\prime}\left(x\right)\left(g\left(b\right)-g\left(a\right)\right)-g^{\prime}\left(x\right)\left(f\left(b\right)-f\left(a\right)\right){% endequation %}

וכמו כן מתקיים:

{% equation %}h\left(a\right)=f\left(a\right)\left(g\left(b\right)-g\left(a\right)\right)-g\left(a\right)\left(f\left(b\right)-f\left(a\right)\right)=f\left(a\right)g\left(b\right)-g\left(a\right)f\left(b\right){% endequation %}

{% equation %}h\left(b\right)=f\left(b\right)\left(g\left(b\right)-g\left(a\right)\right)-g\left(b\right)\left(f\left(b\right)-f\left(a\right)\right)=f\left(a\right)g\left(b\right)-g\left(a\right)f\left(b\right){% endequation %}

כלומר {% equation %}h\left(a\right)=h\left(b\right){% endequation %} ולכן ממשפט רול קיים {% equation %}c{% endequation %} כך ש-{% equation %}h^{\prime}\left(c\right)=0{% endequation %}, כלומר

{% equation %}f^{\prime}\left(c\right)\left(g\left(b\right)-g\left(a\right)\right)-g^{\prime}\left(c\right)\left(f\left(b\right)-f\left(a\right)\right)=0{% endequation %}

וזה מה שרצינו.

נשאר רק להוכיח את כלל לופיטל בעזרת משפט הערך הממוצע של קושי. זו הוכחה קצת פחות "נקייה" ממה שראינו עד כה, אז טוב ששמרתי אותה לסוף, אבל אין בה שום דבר נוראי; פשוט, הדרך הטובה ביותר להבין מה הולך בה היא לכתוב אותה בעצמכם. כמו מה שאני עושה כרגע. כי בחיי שאין לי שמץ של מושג מה הולך בהוכחה הזו למרות שקראתי אותה לפני רגע, אבל אני יודע שהיא פשוטה ואחרי שאכתוב אותה גם אבין אותה.

ובכן, מה יש לנו? הפונקציות {% equation %}f,g{% endequation %} שמקיימות שני דברים:
<ol>
 	<li>{% equation %}\lim_{x\to a}f\left(x\right)=\lim_{x\to a}g\left(x\right)=0{% endequation %}</li>
 	<li>{% equation %}\lim_{x\to a}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %} קיים</li>
</ol>
הטענה השניה נותנת לנו מידע כלשהו על הנגזרות בסביבת הנקודה {% equation %}a{% endequation %}. באופן כללי, הטענה {% equation %}\lim_{x\to a}h\left(x\right)=L{% endequation %} אומרת שלכל {% equation %}\varepsilon&gt;0{% endequation %} קיים {% equation %}\delta&gt;0{% endequation %} כך שלכל {% equation %}x{% endequation %} עבורו {% equation %}0&lt;\left|x-a\right|&lt;\delta{% endequation %} מתקיים {% equation %}\left|h\left(x\right)-L\right|&lt;\varepsilon{% endequation %}; בפרט, כדי שזה יתקיים, הכרחי ש-{% equation %}h\left(x\right){% endequation %} תהיה מוגדרת לכל {% equation %}x{% endequation %} עבורו {% equation %}0&lt;\left|x-a\right|&lt;\delta{% endequation %}. החריג היחיד הוא הנקודה {% equation %}a{% endequation %} עצמה, שאין לנו דרישה לגבי הערך של {% equation %}h{% endequation %} בה. עכשיו, אצלנו {% equation %}h\left(x\right)=\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %}, כך שאנחנו יודעים שקיים {% equation %}\delta{% endequation %} עבורו אם {% equation %}0&lt;\left|x-a\right|&lt;\delta{% endequation %} אז {% equation %}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %} קיים; כלומר גם {% equation %}f^{\prime}\left(x\right){% endequation %} קיימת, וגם {% equation %}g^{\prime}\left(x\right){% endequation %} קיימת <strong>ושונה מאפס</strong>.

הרעיון עכשיו הוא לקחת {% equation %}x{% endequation %} כלשהו עבורו {% equation %}0&lt;\left|x-a\right|&lt;\delta{% endequation %} ולהפעיל את משפט הערך הממוצע של קושי על הקטע שקצוותיו הם {% equation %}a{% endequation %} ו-{% equation %}x{% endequation %}. יש כאן שני מקרים: כאשר {% equation %}a&lt;x{% endequation %} וכאשר {% equation %}a&gt;x{% endequation %}, אבל מן הסתם מה שיקרה בהם יהיה סימטרי אז נניח ש-{% equation %}a&lt;x{% endequation %}. עכשיו צריך שני דברים: ש-{% equation %}f,g{% endequation %} יהיו <strong>רציפות</strong> ב-{% equation %}\left[a,x\right]{% endequation %}, ושיהיו <strong>גזירות</strong> ב-{% equation %}\left(a,x\right){% endequation %}. את הדבר השני כבר יש לנו, ואנחנו גם יודעים שהפונקציות גזירות ב-{% equation %}x{% endequation %} ולכן הן רציפות שם; הקושי היחיד הוא ב-{% equation %}a{% endequation %}. אנחנו יודעים ש-{% equation %}\lim_{x\to a}f\left(x\right)=\lim_{x\to a}g\left(x\right)=0{% endequation %} ולכן כדי שהפונקציות הללו יהיו רציפות ב-{% equation %}a{% endequation %} צריך להתקיים {% equation %}f\left(a\right)=g\left(a\right)=0{% endequation %}; אבל אם זה לא מתקיים, הן לא יהיו רציפות שם. לכן נכריח את זה לקרות - <strong>נגדיר מחדש</strong> את הפונקציות הללו ב-{% equation %}a{% endequation %} על ידי {% equation %}f\left(a\right)=g\left(a\right)=0{% endequation %}. האם ההגדרה מחדש הזו תיצור לנו בעיות? עוד מעט נחזור לשאלה הזו כדי לראות למה אין בעיות.

עכשיו אפשר להשתמש במשפט הערך הממוצע של קושי ולקבל את הקיום של {% equation %}c\in\left(a,x\right){% endequation %} שעבורו מתקיים

{% equation %}f^{\prime}\left(c\right)\left(g\left(x\right)-g\left(a\right)\right)=g^{\prime}\left(c\right)\left(f\left(x\right)-f\left(a\right)\right){% endequation %}

ומכיוון ש-{% equation %}f\left(a\right)=g\left(a\right)=0{% endequation %} אפשר לפשט קצת ולכתוב

{% equation %}f^{\prime}\left(c\right)g\left(x\right)=g^{\prime}\left(c\right)f\left(x\right){% endequation %}

ואם נחלק, נקבל

{% equation %}\frac{f\left(x\right)}{g\left(x\right)}=\frac{f^{\prime}\left(c\right)}{g^{\prime}\left(c\right)}{% endequation %}

שכבר קצת מזכיר את המבנה של כלל לופיטל. אבל רגע אחד! אם אני מחלק בדברים, צריך לוודא שהם שונים מאפס! לגבי {% equation %}g^{\prime}\left(c\right){% endequation %} כבר ראינו את זה בהתחלה. מה לגבי {% equation %}g\left(x\right){% endequation %}? ובכן, אם היה מתקיים {% equation %}g\left(x\right)=0=g\left(a\right){% endequation %} אז אפשר היה להשתמש במשפט רול כדי למצוא נקודה בין {% equation %}a{% endequation %} ל-{% equation %}x{% endequation %} שבה {% equation %}g^{\prime}{% endequation %} שווה לאפס, וכבר ראינו שזה לא יכול לקרות.

עכשיו אפשר לסכם, עם טיעון קצת עדין שאפשר לנסח בחופזה בתור "מכיוון ש-{% equation %}c{% endequation %} נמצא ב-{% equation %}\left(a,x\right){% endequation %} אז כאשר {% equation %}x{% endequation %} שואף ל-{% equation %}a{% endequation %} כך גם {% equation %}c{% endequation %}, ולכן {% equation %}\lim_{x\to a}\frac{f\left(x\right)}{g\left(x\right)}{% endequation %} שווה ל-{% equation %}\lim_{c\to a}\frac{f^{\prime}\left(c\right)}{g^{\prime}\left(c\right)}{% endequation %} כמבוקש". אני ממליץ לכם לנסות להשלים את הפרטים בעצמכם כדי לקבל את תחושת ה"למה זה נכון" אבל הנה הפירוט הטכני בכל מקרה:

פתחנו עם הנתון לפיו {% equation %}\lim_{x\to a}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %} קיים; בואו ואסמן אותו {% equation %}L=\lim_{x\to a}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %}. אני רוצה להוכיח שגם {% equation %}\lim_{x\to a}\frac{f\left(x\right)}{g\left(x\right)}=L{% endequation %}, ואני אעשה את זה לפי הספר עם הגדרת האפסילון-דלתא הסטנדרטית. יהא אם כן {% equation %}\varepsilon&gt;0{% endequation %} כלשהו. מכיוון ש-{% equation %}L=\lim_{x\to a}\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}{% endequation %} אז קיים {% equation %}\delta&gt;0{% endequation %} כך שאם {% equation %}0&lt;\left|x-a\right|&lt;\delta{% endequation %} אז מתקיים {% equation %}\left|\frac{f^{\prime}\left(x\right)}{g^{\prime}\left(x\right)}-L\right|&lt;\varepsilon{% endequation %}. אני טוען שאותו {% equation %}\delta{% endequation %} יוכיח ש-{% equation %}\lim_{x\to a}\frac{f\left(x\right)}{g\left(x\right)}=L{% endequation %}; כלומר, אני צריך להראות שאם {% equation %}0&lt;\left|x-a\right|&lt;\delta{% endequation %} אז {% equation %}\left|\frac{f\left(x\right)}{g\left(x\right)}-L\right|&lt;\varepsilon{% endequation %}.

עכשיו, הוכחנו קודם כי על פי משפט הערך הממוצע, קיים {% equation %}c{% endequation %} כך ש-{% equation %}c\in\left(a,x\right){% endequation %} (או {% equation %}c\in\left(x,a\right){% endequation %} אם {% equation %}x&lt;a{% endequation %}) כך ש-{% equation %}\frac{f\left(x\right)}{g\left(x\right)}=\frac{f^{\prime}\left(c\right)}{g^{\prime}\left(c\right)}{% endequation %}. מכיוון ש-{% equation %}a&lt;c&lt;x{% endequation %} ו-{% equation %}\left|x-a\right|&lt;\delta{% endequation %} אז גם {% equation %}\left|c-a\right|&lt;\delta{% endequation %} ולכן {% equation %}\left|\frac{f^{\prime}\left(c\right)}{g^{\prime}\left(c\right)}-L\right|&lt;\varepsilon{% endequation %} ולכן {% equation %}\left|\frac{f\left(x\right)}{g\left(x\right)}-L\right|&lt;\varepsilon{% endequation %} כמבוקש, מה שמסיים את ההוכחה.

זה זמן טוב לסיים בו את הפוסט, אבל כרגיל - זה רק קצה הקרחון של השימושים במשפט הערך הממוצע, וזה פשוט ששולי הבלוג הזה צרים מלהכילם.

