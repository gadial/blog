---
id: 2167
title: "משוואת פל"
date: 2012-08-31 01:08:21
layout: post
categories: 
  - אלגברה מופשטת
  - תורת המספרים
tags: 
  - גם טכני זה כיף!
  - הרחבות ריבועיות
  - משוואת פל
  - שברים משולבים
  - תורת המספרים האלגברית
social_media_share: true
---
אני רוצה לדבר הפעם על משוואת פל ואיך פותרים אותה. ממבט ראשון, משוואת פל היא בסך הכל איזו משוואה מוזרה שלא ברור מה טוב בה ומה מעניין בה ומה יפה בה, אבל אחרי שמתעמקים בה קצת ורואים דוגמאות, היופי שבעניין מתחיל לצוץ. זה לפחות היה התהליך שעבר עלי, ואני חושב שזה תהליך שמתרחש בתחומים רבים של המתמטיקה, שבהם עיסוק במשהו שנראה "קטנוני" למתבונן מהצד בעצם מכיל חשיבות ויופי רבים. בפרט, הפוסט הזה יקח כלים מכמה תחומים מתמטיים שונים ויזרוק אותם על בעיה קונקרטית מאוד ויפתור אותה לחלוטין באמצעותם.

נתחיל מכך ש"משוואת פל" זה שם מטעה פעמיים. ראשית, כי לא מדובר על משוואה אחת אלא על משפחה אינסופית של משוואות; ושנית, כי למתמטיקאי שנקרא פל לא היה קשר למשוואה - לאונרד אוילר, מגדולי המתמטיקאי של כל הזמנים, ייחס בטעות לפל עיסוק במשוואה הזו והשם השתרש.

אז על מה מדובר? על משוואה שנראית כך:

{% equation %}x^{2}-Ny^{2}=1{% endequation %}

כאשר {% equation %}x,y{% endequation %} הם משתנים ואילו {% equation %}N{% endequation %} הוא <strong>פרמטר</strong>, כלומר מספר קבוע כלשהו, שהוא מספר שלם חיובי. עבור פרמטרים שונים נקבל משוואות שונות, למשל:

{% equation %}x^{2}-2y^{2}=1{% endequation %}

זו דוגמה קונקרטית אחת למשוואת פל, עם {% equation %}N=2{% endequation %}, ואילו

{% equation %}x^{2}-7y^{2}=1{% endequation %}

היא דוגמה אחרת, עבור {% equation %}N=7{% endequation %}.

משוואת פל היא דוגמה למשוואה <strong>דיופנטית</strong> - זו משוואה פולינומית, המקדמים שמופיעים בה הם שלמים, והשאלה שמעניינת אותנו היא "מה הפתרונות השלמים למשוואה?". דיברתי על משוואות דיופנטיות בפוסט הקודם (ואני מדבר על משוואת פל עכשיו בין היתר כי היא תהיה רלוונטית להמשך הטיפול בנושאים שדיברתי עליהם <a href="http://www.gadial.net/2012/08/27/hilbert_tenth_intro/">בפוסט הקודם</a>) וזו דוגמה נאה למשוואה דיופנטית שכזו.

השאלה הראשונה שמשוואה כמו זו מעוררת היא "למה לעזאזל שמישהו יתעניין במשוואה הזו?". התשובה היא שהמשוואה צצה בהקשרים רבים ושונים, ולא אציג אף אחד מהם כרגע כי זה יקח יותר מדי מקום בפוסט (חוץ מאחד מההקשרים שיהיה מאוד רלוונטי בהמשך). ב<a href="http://projecteuler.net/">פרוייקט אוילר</a> נתקלתי בכמה וכמה שאלות שבסופו של דבר, אחרי כל הפישוטים וההתאמות, התגלה שהקושי הטכני האמיתי בפתרונן הוא פתרון של משוואת פל מסויימת. סמכו עלי - כמו משוואות רבות אחרות בתורת המספרים, יש למשוואה הזו את הכשרון לצוץ בדיוק כשלא מצפים לה.

השאלה הבאה, שהיא קצת יותר מעשית, היא "איך פותרים את המשוואה?". אבל מה זה בעצם אומר, לפתור את המשוואה? למצוא זוג ערכים של {% equation %}x,y{% endequation %} שמקיימים את המשוואה? להכריע אם קיים או לא קיים זוג כזה? למצוא <strong>כמה</strong> זוגות כאלו יש? למצוא אלגוריתם שמייצר סדרתית את כל הפתרונות? להבין את המבנה האלגברי שלהם, אם קיים כזה? כל אלו הן תשובות אפשריות; מה שיפה במשוואת פל הוא שיש תשובה משביעת רצון לכולן.

נתחיל בדברים הברורים מאליהם. למשוואה תמיד יש פתרון שבו {% equation %}x=1{% endequation %} ו-{% equation %}y=0{% endequation %}. הפתרון הזה מכונה "הפתרון הטריוויאלי" והוא לא מעניין במיוחד, אז לא נדבר עליו יותר. האתגר הוא למצוא פתרונות שבהם גם {% equation %}x{% endequation %} וגם {% equation %}y{% endequation %} הם חיוביים. עכשיו, אם {% equation %}N{% endequation %} הוא בעצמו ריבוע של מספר כלשהו, אז {% equation %}x^{2}-Ny^{2}{% endequation %} הוא הפרש של שני ריבועים; ההפרש הקטן ביותר של שני ריבועים שונים הוא 3 ({% equation %}2^{2}-1^{2}{% endequation %}) ובאופן כללי הוא יהיה גדול יותר, כי {% equation %}a^{2}-b^{2}=\left(a-b\right)\left(a+b\right){% endequation %} ועבור שני מספרים חיוביים שונים, {% equation %}a+b{% endequation %} יהיה לפחות 3. לכן למשוואה <strong>אין פתרון לא טריוויאלי</strong> אם {% equation %}n{% endequation %} הוא ריבוע, ולכן מראש מדברים על המשוואה רק במקרה שבו {% equation %}n{% endequation %} אינו ריבוע. במקרה זה למשוואה <strong>יש אינסוף פתרונות</strong>, תמיד. מהם הפתרונות הללו ואיך מוצאים אותם - זה מה שאני רוצה לדבר עליו בפוסט הזה.

נתחיל מהסוף - לכל {% equation %}n{% endequation %} שאינו ריבוע, יש למשוואה פתרון לא טריוויאלי מסויים, שנקרא לו "הפתרון היסודי", ויש שיטה פשוטה יחסית למצוא אותו. מרגע שמצאנו אותו, כל פתרון אחר (ויש אינסוף כאלו) מתקבל <strong>מתוך</strong> הפתרון היסודי באמצעות שיטה פשוטה אחרת. כל העסק מוסבר בצורה יפהפיה בעזרת <strong>המבנה האלגברי</strong> של הפתרונות.

המתמטיקאים ההודי בראהמגופטה גילה, אי שם במאה ה-7 לספירה, שאם יש לנו שני פתרונות למשוואה {% equation %}x^{2}-Ny^{2}=1{% endequation %} אז אפשר "לבנות" מהם פתרון חדש, באופן הזה: נסמן את הפתרונות בתור {% equation %}\left(x_{1},y_{1}\right),\left(x_{2},y_{2}\right){% endequation %}, אז מתקיימת המשוואה הבאה:

{% equation %}\left(x_{1}^{2}-Ny_{1}^{2}\right)\left(x_{2}^{2}-Ny_{2}^{2}\right)=\left(x_{1}x_{2}+Ny_{1}y_{2}\right)^{2}-N\left(x_{1}y_{2}+x_{2}y_{1}\right)^{2}{% endequation %}

מה קורה כאן? מכיוון ש-{% equation %}\left(x_{1},y_{1}\right){% endequation %} ו-{% equation %}\left(x_{2},y_{2}\right){% endequation %} הם פתרונות למשוואת פל עם הפרמטר {% equation %}N{% endequation %}, אגף שמאל הוא פשוט 1 כפול 1; אגף ימין, לעומת זאת, נראה כמו משוואת פל - משהו בריבוע פחות {% equation %}N{% endequation %} כפול משהו אחר בריבוע. מכאן שקיבלנו פתרון חדש של משוואת פל: {% equation %}\left(x_{1}x_{2}+Ny_{1}y_{2},x_{1}y_{2}+x_{2}y_{1}\right){% endequation %}.

כדי לראות שהנוסחה נכונה אפשר פשוט לפתוח סוגריים ולבדוק, אבל זה מזוויע. תחת זאת, אפשר לתת לה פירוש אלגברי מודרני יותר. אלו מכם שמכירים מספרים מרוכבים אולי מרגישים שהפתרון החדש הוא בעל צורה שמזכירה מאוד כפל של מרוכבים; זה לא מקרי. הרעיון הוא שאת הביטוי {% equation %}x^{2}-Ny^{2}{% endequation %} אפשר לפרק לשני חלקים: {% equation %}x^{2}-Ny^{2}=\left(x+\sqrt{N}y\right)\left(x-\sqrt{N}y\right){% endequation %}. אם {% equation %}N{% endequation %} איננו ריבוע אז {% equation %}\sqrt{N}{% endequation %} כלל לא יהיה מספר שלם (ואפילו <a href="http://www.gadial.net/2008/10/31/irrationality_of_square_roots/">לא מספר רציונלי</a>). מנקודת מבט אלגברית, זה הופך ביטוי כמו {% equation %}x+\sqrt{N}y{% endequation %} למעניין <strong>יותר</strong>. המתמטיקאים מתחילים לדבר בשלב הזה על קבוצת <strong>כל</strong> המספרים מהצורה {% equation %}x+y\sqrt{N}{% endequation %} כאשר {% equation %}x,y{% endequation %} הם שלמים, ולנסות להבין עד כמה הקבוצה הזו דומה למספרים השלמים ועד כמה היא שונה. זה אחד מהדברים הבסיסיים שבהם עוסקת <strong>תורת המספרים האלגברית</strong>; לקבוצה {% equation %}\mathbb{Z}\left[\sqrt{N}\right]=\left\{ x+y\sqrt{N}\ |\ x,y\in\mathbb{Z}\right\} {% endequation %} קוראים <strong>חוג השלמים</strong> של שדה המספרים {% equation %}\mathbb{Q}\left(\sqrt{N}\right){% endequation %} (אני משקר כאן קצת - אם {% equation %}N{% endequation %} שקול ל-1 מודולו 4 חוג השלמים של {% equation %}\mathbb{Q}\left(\sqrt{N}\right){% endequation %} הוא מסובך יותר, אבל זה לא יהיה מהותי עבורנו). <a href="http://www.gadial.net/2011/08/19/algebraic_number_theory_intro_1/">דיברתי קצת</a> על תורת המספרים האלגברית בעבר בבלוג, אבל לא הגעתי אז אל המשפט ה"כבד" (יחסית; זה אחד מהמשפטים הרציניים הראשונים שמציגים בכל מבוא לתחום) שבו אני רוצה להשתמש עכשיו.

כשאומרים ש-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} הוא "חוג", למה הכוונה? לכך שיש פעולות חיבור וכפל על איברי החוג שמתנהגות כפי שאנו מצפים מחיבור וכפל להתנהג - חוקי הקיבוץ, החילוף והפילוג מתקיימים. בואו נניח שיש לנו שני מספרים, {% equation %}x_{1}+y_{1}\sqrt{N}{% endequation %} ו-{% equation %}x_{2}+y_{2}\sqrt{N}{% endequation %}. הסכום שלהם הוא

{% equation %}\left(x_{1}+y_{1}\sqrt{N}\right)+\left(x_{2}+y_{2}\sqrt{N}\right)=\left(x_{1}+x_{2}\right)+\left(y_{1}+y_{2}\right)\sqrt{N}{% endequation %}

כאן השתמשנו בחוקי החילוף, הקיבוץ והפילוג של מספרים שלמים "רגילים" וראינו שחיבור פועל "רכיב רכיב" (אפשר לכתוב מספר מהצורה {% equation %}x+y\sqrt{N}{% endequation %} באופן מקוצר כ-{% equation %}\left(x,y\right){% endequation %}; האיבר השמאלי הוא "הרכיב השמאלי" והימני הוא "הרכיב הימני" ואז פעולת החיבור מקיימת {% equation %}\left(x_{1},y_{1}\right)+\left(x_{2},y_{2}\right)=\left(x_{1}+x_{2},y_{1}+y_{2}\right){% endequation %}). כפל, לעומת זאת, יתנהג באופן קצת יותר מורכב - בואו פשוט נבצע את החישוב:

{% equation %}\left(x_{1}+y_{1}\sqrt{N}\right)\left(x_{2}+y_{2}\sqrt{N}\right)=x_{1}x_{2}+\left(y_{1}\sqrt{N}\right)x_{2}+x_{1}\left(y_{2}\sqrt{N}\right)+\left(y_{1}\sqrt{N}\right)\left(y_{2}\sqrt{N}\right){% endequation %}

{% equation %}=x_{1}x_{2}+x_{2}y_{1}\sqrt{N}+x_{1}y_{2}\sqrt{N}+y_{1}y_{2}N=\left(x_{1}x_{2}+Ny_{1}y_{2}\right)+\left(x_{1}y_{2}+x_{2}y_{1}\right)\sqrt{N}{% endequation %}

נראה מוכר? זה בדיוק מה שהופיע באגף ימין משוואה של בראהמגופטה. במילים אחרות, עכשיו אפשר לנסח את התגלית של בראהמגופטה כך: אם אנחנו חושבים על פתרון {% equation %}\left(x,y\right){% endequation %} למשוואת פל בתור האיבר {% equation %}x+y\sqrt{N}{% endequation %} בחוג השלמים {% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %}, אז גם מכפלה של פתרונות (עם פעולת הכפל של {% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %}) היא פתרון.

טוב ויפה, אבל שימו לב שעדיין אין לנו הוכחה אלטרנטיבית לתוצאה הזו - <strong>למה</strong> מכפלה של פתרונות היא גם פתרון? האם יש איזה עקרון עמוק שעומד מאחורי זה? התשובה חיובית, ומצריכה הכנסת מושג נוסף לתמונה - <strong>נורמה</strong>.

למילה "נורמה" מספר שימושים שונים במתמטיקה שהמשמעות שלהם שונה. <a href="http://www.gadial.net/2012/03/01/inner_product_spaces_geometry/">הצגתי כבר</a> שימוש אחד כזה, באלגברה לינארית, וחשוב לי להבהיר שמה שאני מדבר עליו עכשיו הוא לא אותו דבר (למרות שבמקרים מאוד מסויימים שני המושגים מתלכדים). המקרה שלנו הוא נורמה של שדה מספרים. להגדיר נורמה כזו באופן כללי - זה קצת קשה ולא אעשה את זה. הגדרה קצת פחות כללית, שעדיין תהיה בלתי מובנת לרבים מהקוראים, היא זו: הנורמה של איבר {% equation %}\alpha{% endequation %} היא מכפלת כל הצמודים של {% equation %}\alpha{% endequation %}, כלומר מכפלת ההפעלות של כל איברי חבורת הגלואה של ההרחבה של שדה המספרים על {% equation %}\alpha{% endequation %}. למרות שזו הגדרה שנשמעת ג'יברישית לחלקכם חשוב לי שתראו איך הכל הוא חלק מתורה כללית ורבת שימושים לכשעצמה, ואיך שום דבר שאנחנו עושים כאן הוא לא אד-הוקי.

בפועל, עבור {% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %}, להגדרה הזו יש משמעות מאוד פשוטה: הנורמה של {% equation %}x+y\sqrt{N}{% endequation %} היא המכפלה שלו באיבר {% equation %}x-y\sqrt{N}{% endequation %} (ה"צמוד" שלו), וחישוב מהיר מראה שזה יוצא {% equation %}x^{2}-Ny^{2}{% endequation %}. במילים אחרות, איבר של {% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} הוא פתרון של משוואת פל אם ורק אם הוא מנורמה 1. עכשיו, מההגדרה הכללית של נורמה נובע די בקלות שהיא <strong>כפלית</strong>, כלומר הנורמה של מכפלה של איברים היא מכפלת הנורמות שלהם ({% equation %}\text{Norm}\left(\alpha\cdot\beta\right)=\text{Norm}\left(\alpha\right)\cdot\text{Norm}\left(\beta\right){% endequation %}). אם כופלים שני איברים מנורמה 1, אז הנורמה של המכפלה גם כן תהיה 1, ולכן גם היא תהיה פתרון למשוואת פל - הופס! הוכחנו את בראהמגופטה בלי להיכנס לחישובים טכניים (כמובן, נפנפתי את העניין הזה שנורמה היא תמיד כפלית, וגם את זה שאנחנו יודעים מה הנורמה של איבר ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %}, אבל סמכו עלי שאין שם סיבוך טכני). לא רק שהוכחנו, עכשיו אנחנו גם מבינים יותר טוב מה הולך כאן, והצלחנו להמיר את הבעיה של הכרת המבנה של אוסף הפתרונות של משוואת פל לבעיה אחרת - הבנת המבנה של קבוצת האיברים ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} שהם מנורמה 1.

עכשיו, אם איבר הוא מנורמה 1, אז הוא <strong>הפיך</strong> (אפשר לכפול אותו במשהו ולקבל 1 - זה נובע מכך שהנורמה היא מכפלת איבר בכל הצמודים שלו, אז מכפלת כל הצמודים הזו היא בדיוק ההופכי). לרוע המזל, ההפך לא נכון - איבר הפיך יכול להיות גם מנורמה {% equation %}-1{% endequation %}. עם זאת, היתרון שבלעבור לדבר על הבעיה של הבנת המבנה של קבוצת כל ההפיכים ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} הוא שעכשיו אפשר להכניס לתמונה את המשפט ה"כבד" שדיברתי עליו - משפט ההפיכים של דיריכלה (באנגלית זה Dirichlet Unit Theorem כאשר Unit הוא השם המקובל לאיבר הפיך בחוג; אני מעדיף לתרגם בתור "משפט ההפיכים" מאשר בתור "משפט היחידות" שנשמע יותר מדי כמו "Uniqueness Theorem'').

מהמשפט הזה נובע שאת<strong> כל</strong> ההפיכים ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} ניתן לקבל על ידי כך שמתחילים מאיבר הפיך ספציפי (שכבר קראתי לו "הפתרון היסודי" קודם) וכופלים אותו בעצמו, שוב ושוב ושוב. במילים אחרות, כל פתרון הוא חזקה של הפתרון היסודי. פורמלית זה הולך כך: אם {% equation %}\left(x_{0},y_{0}\right){% endequation %} הוא הפתרון היסודי, אז נגדיר רקורסיבית את הסדרה הבאה:

{% equation %}x_{n+1}=x_{n}x_{0}+Ny_{n}y_{0}{% endequation %}

{% equation %}y_{n+1}=x_{n}y_{0}+y_{n}x_{0}{% endequation %}

וכך נקבל סדרה {% equation %}\left(x_{0},y_{0}\right),\left(x_{1},y_{1}\right),\left(x_{2},y_{2}\right),\dots{% endequation %} שבה נמצאים <strong>כל</strong> האיברים ההפיכים ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %}, ולכן בפרט גם את <strong>כל </strong>הפתרונות למשוואת פל {% equation %}x^{2}-Ny^{2}=1{% endequation %} (אבל, אם הפתרון היסודי מקיים {% equation %}x_{0}^{2}-Ny_{0}^{2}=-1{% endequation %}, אז גם איברים שאינם פתרון למשוואת פל אם כי הם פותרים משוואה קרובה שגם היא מעניינת לעתים - {% equation %}x^{2}-Ny^{2}=-1{% endequation %}, או אם תרצו {% equation %}Ny^{2}-x^{2}=1{% endequation %}).

איך זה נובע מהמשפט של דיריכלה? כאן כבר אין מנוס - אני הולך להיות טכני, ומי שיאבד אותי כאן יכול לקפוץ לפסקה הבאה. קל לראות שקבוצת כל ההפיכים בחוג שלמים היא תמיד חבורה, וחבורה אבלית, כי הכפל בחוג הוא קומוטטיבי. עכשיו, כל חבורה אבלית איזומורפית לחבורה מהצורה {% equation %}\mathbb{Z}^{r}\times\mathbb{Z}_{k_{1}}\times\dots\times\mathbb{Z}_{k_{t}}{% endequation %}, כאשר {% equation %}\mathbb{Z}^{r}{% endequation %} נקרא <strong>הרכיב החופשי</strong> של החבורה ו-{% equation %}r{% endequation %} נקרא <strong>המימד</strong> שלו, ואילו {% equation %}\mathbb{Z}_{k_{1}}\times\dots\times\mathbb{Z}_{k_{t}}{% endequation %} נקרא <strong>הפיתול</strong> של החבורה - החלק בה שמכיל את האיברים מסדר סופי (אפשר אפילו להגיד עוד משהו על הקשר בין ה-{% equation %}k_{i}{% endequation %}-ים השונים, אבל זה לפוסט אחר). בחבורה האבלית של ההפיכים של חוג שלמים כלשהו, הפיתול כולל בדיוק את <strong>שורשי היחידה</strong> בחוג הזה; ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} מדובר רק על {% equation %}\left\{ 1,-1\right\} {% endequation %} כך שהפיתול לא מעניין במיוחד. מה שמעניין הוא {% equation %}r{% endequation %}. משפט היחידה של דיריכלה מצביע על ערכו של {% equation %}r{% endequation %}: הוא שווה ל-{% equation %}r_{1}+r_{2}-1{% endequation %}, כאשר {% equation %}r_{1}{% endequation %} הוא מספר השיכונים של {% equation %}\mathbb{Q}\left(\sqrt{N}\right){% endequation %} ב-{% equation %}\mathbb{R}{% endequation %} ו-{% equation %}r_{2}{% endequation %} הוא מספר השיכונים של {% equation %}\mathbb{Q}\left(\sqrt{N}\right){% endequation %} ב-{% equation %}\mathbb{C}{% endequation %}, חלקי 2 (שיכונים כאלו תמיד באים בזוגות צמודים, אז סופרים את הזוגות). בפועל, {% equation %}r_{1}{% endequation %} הוא פשוט מספר הצמודים של {% equation %}\sqrt{N}{% endequation %} שהם ממשיים (יש שניים - {% equation %}\sqrt{N}{% endequation %} ו-{% equation %}-\sqrt{N}{% endequation %}) ו-{% equation %}2r_{2}{% endequation %} הוא מספר הצמודים של {% equation %}\sqrt{N}{% endequation %} שאינם ממשיים (לפעמים קוראים להם "מרוכבים" למרות שזה קצת שקר כי גם ממשי הוא מרוכב). כאן אין ל-{% equation %}\sqrt{N}{% endequation %} צמודים שאינם ממשיים, כך ש-{% equation %}r_{1}=2{% endequation %} ו-{% equation %}r_{2}=0{% endequation %} וקיבלנו ממשפט דיריכלה שמבנה חבורת ההפיכים ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} הוא איזומורפי ל-{% equation %}\mathbb{Z}\times\left\{ 1,-1\right\} {% endequation %}, וזה מה שרצינו.

נותרנו רק עם שאלה אחת - איך מוצאים את הפתרון היסודי? התשובה לוקחת אותנו לתחום אחר לגמרי - שברים משולבים. כבר תיארתי שברים משולבים <a href="http://www.gadial.net/2010/05/29/continued_fractions_1/">בפוסט קודם</a> ולכן לא אציג את הכל מחדש, אבל בכל זאת אציג משהו מחדש. אתחיל, כמקודם, מהשורה התחתונה: מפתחים את {% equation %}\sqrt{N}{% endequation %} לשבר משולב; בגלל ש-{% equation %}\sqrt{N}{% endequation %} הוא שורש של פולינום ממעלה שניה, השבר המשולב יהיה מחזורי; הפתרון היסודי מסתתר בדיוק לפני שלב בפיתוח שבו הפיתוח מתחיל לחזור על עצמו. עכשיו בואו נראה את הפרטים.

שבר משולב הוא ביטוי שנראה כך: {% equation %}a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}+\frac{1}{a_{3}+\dots}}}{% endequation %}. במילים אחרות, אפשר לאפיין שבר משולב על ידי סדרה של מספרים {% equation %}a_{0},a_{1},a_{2},\dots{% endequation %} ולא לכתוב את השבר המפחיד בכל פעם מחדש. שבר משולב יכול להיות סופי, כלומר שסדרת המספרים המתאימה לו היא סופית, ואז אפשר לחשב אותו "עד הסוף" ולקבל מספר רציונלי; הוא גם יכול להיות סדרה אינסופית, ואז הוא מגדיר סדרה אינסופית של מספרים רציונליים, שמתכנסת למספר ממשי כלשהו. אפשר להראות שלכל מספר ממשי יש פיתוח כזה כשבר משולב, ואפשר להראות משהו מעניין עוד יותר - שכל מספר ממשי אי רציונלי שהוא פתרון של משוואה ממעלה שניה מתואר על ידי שבר משולב אינסופי שהוא <strong>מחזורי</strong>החל ממקום מסוים. למעשה, אפשר להוכיח אפילו יותר מזה! שהשבר המשולב תמיד יהיה מהצורה הבאה - {% equation %}a_{0},a_{1},a_{2},\dots,a_{n}\dots,a_{2}a_{1},2a_{0},a_{1},a_{2},\dots{% endequation %}, כלומר הוא יהיה מורכב באופן הבא:
<ol>
	<li>איבר התחלתי {% equation %}a_{0}{% endequation %}.</li>
	<li>קטע סימטרי {% equation %}a_{1},a_{2},\dots,a_{n},\dots,a_{2},a_{1}{% endequation %}.</li>
	<li>האיבר ההתחלתי כפול 2: {% equation %}2a_{0}{% endequation %}.</li>
</ol>
כאשר 2 ו-3 חוזרים על עצמם לאין קץ.

איך מוצאים את הייצוג הזה בפועל? ובכן, פשוט מחשבים. תכף אתן את האלגוריתם, אבל בואו ננסה להבין באמצעות דוגמה קודם. למשל, {% equation %}\sqrt{19}{% endequation %}.

מתחילים מהערך השלם התחתון של {% equation %}\sqrt{19}{% endequation %}, כלומר {% equation %}\left\lfloor \sqrt{19}\right\rfloor =4{% endequation %}. כן, צריך לחשב אותו - אף אחד לא אמר שאפשר למצוא את השבר המשולב של {% equation %}\sqrt{19}{% endequation %} בלי לעשות חישובים! (איך מוציאים שורש? גם על זה <a href="http://www.gadial.net/2007/10/31/finding_square_roots/">כבר יש לי פוסט</a>). נגדיר {% equation %}a_{0}=4{% endequation %}. עכשיו כותבים:

{% equation %}\sqrt{19}=4+\frac{1}{x}{% endequation %}

איך נמצא את {% equation %}x{% endequation %}? ובכן, נעביר את {% equation %}4{% endequation %} אגף, ניקח את ההופכיים של שני האגפים, ונקבל:

{% equation %}x=\frac{1}{\sqrt{19}-4}{% endequation %}

עכשיו נשתמש בתעלול מימי בית הספר - נכפיל מונה ומכנה ב<strong>צמוד</strong> של הביטוי שלמטה (האם עכשיו המילה "צמוד" מצלצלת לכם?), כלומר ב-{% equation %}\sqrt{19}+4{% endequation %}. נקבל:

{% equation %}x=\frac{\sqrt{19}+4}{3}{% endequation %}

לכאורה רק סיבכנו את עצמנו - רצינו למצוא את השורש של 19, ועכשיו קיבלנו מספר שנראה עוד יותר מסובך. עם זאת, אל דאגה! פשוט ממשיכים באותה השיטה לטפל גם בו. ראשית, מחשבים את הערך התחתון שלו: {% equation %}\left\lfloor \frac{\sqrt{19}+4}{3}\right\rfloor =2{% endequation %}. מגדירים {% equation %}a_{1}=2{% endequation %} וכותבים:

{% equation %}\frac{\sqrt{19}+4}{3}=2+\frac{1}{x}{% endequation %}

איך נמצא את {% equation %}x{% endequation %}? ובכן, באותה שיטת חילוץ! נעביר את 2 אגף ונקבל

{% equation %}\frac{1}{x}=\frac{\sqrt{19}+4-6}{3}{% endequation %}

ניקח הופכי לשני האגפים ונקבל

{% equation %}x=\frac{3}{\sqrt{19}-2}{% endequation %}

נכפול בצמוד {% equation %}\sqrt{19}+2{% endequation %} ונקבל

{% equation %}x=\frac{3\left(\sqrt{19}+2\right)}{15}=\frac{\sqrt{19}+2}{5}{% endequation %}

ואתם כבר מבינים איך זה נמשך מכאן.

פורמלית, האלגוריתם פועל כך:

מאתחלים משתנים

{% equation %}a_{0}=\left\lfloor \sqrt{N}\right\rfloor {% endequation %}

{% equation %}m_{0}=0{% endequation %}

{% equation %}d_{0}=1{% endequation %}

ועכשיו בכל שלב מבצעים את החישובים הבאים:

{% equation %}m_{n+1}=a_{n}d_{n}-m_{n}{% endequation %}

{% equation %}d_{n+1}=\frac{N-m_{n+1}^{2}}{d_{n}}{% endequation %}

{% equation %}a_{n+1}=\left\lfloor \frac{\sqrt{N}+m_{n+1}}{d_{n+1}}\right\rfloor {% endequation %}

מה קורה כאן? ובכן, בשלב {% equation %}n{% endequation %} המספר שאנחנו מנסים לחשב את השבר המשולב שלו הוא {% equation %}\frac{\sqrt{N}+m_{n}}{d_{n}}{% endequation %}. אנחנו יודעים שהשבר המשולב הזה הוא מהצורה {% equation %}a_{n}+\frac{1}{x}{% endequation %} ורוצים למצוא את {% equation %}x{% endequation %}. כפי שכבר ראינו, יתברר בסוף ש-{% equation %}x{% endequation %} הוא מהצורה {% equation %}x=\frac{\sqrt{N}+y}{z}{% endequation %} כך ש-{% equation %}y,z{% endequation %} הם שלמים, וצריך רק לחשב אותם.

אז {% equation %}a_{n}{% endequation %} יהיה {% equation %}\left\lfloor \frac{\sqrt{N}+m_{n}}{d_{n}}\right\rfloor {% endequation %}. עכשיו, אם {% equation %}\frac{\sqrt{N}+m_{n}}{d_{n}}=a_{n}+\frac{1}{x}{% endequation %} אז {% equation %}\frac{1}{x}=\frac{\sqrt{N}+m_{n}-a_{n}d_{n}}{d_{n}}{% endequation %}, ולכן {% equation %}x=\frac{d_{n}}{\sqrt{N}-\left(a_{n}d_{n}-m_{n}\right)}{% endequation %}. שימו לב שהפכתי את האיבר {% equation %}m_{n}-a_{n}d_{n}{% endequation %} שבמכנה על ידי הוצאת סימן מינוס החוצה, וקיבלתי בדיוק את האיבר שהגדרתי כ-{% equation %}m_{n+1}{% endequation %}. כלומר, קיבלנו {% equation %}x=\frac{d_{n}}{\sqrt{N}-m_{n+1}}{% endequation %}. עכשיו מגיע שלב הכפל בצמוד, שהוא במקרה שלנו {% equation %}\sqrt{N}+m_{n+1}{% endequation %}, ומקבלים {% equation %}x=\frac{d_{n}\left(\sqrt{N}+m_{n+1}\right)}{N-m_{n+1}^{2}}=\frac{d_{n}}{N-m_{n+1}^{2}}\left(\sqrt{N}+m_{n+1}\right){% endequation %}.

עכשיו, מה הוא הגורם {% equation %}\frac{d_{n}}{N-m_{n+1}^{2}}{% endequation %}? שוב, שימו לב להגדרות שלי - זה בדיוק {% equation %}\frac{1}{d_{n+1}}{% endequation %}. לכן קיבלנו {% equation %}x=\frac{\sqrt{N}+m_{n+1}}{d_{n+1}}{% endequation %}. כלומר, {% equation %}y=m_{n+1}{% endequation %} ו-{% equation %}z=d_{n+1}{% endequation %}, כפי שהיה ניתן לצפות, ולכן המשך החישוב הוא בדיוק ביצוע החישוב {% equation %}\left\lfloor \frac{\sqrt{N}+m_{n+1}}{d_{n+1}}\right\rfloor {% endequation %} וכן הלאה.

כזכור, הובטח לנו שהחישוב הופך למחזורי מתישהו. לא ניכנס לפרטי ההוכחה הזו עכשיו; רק נציין שאפשר לזהות מתי זה מתרחש בתוך האלגוריתם עצמו. כפי שראינו, בשלב {% equation %}n{% endequation %} המצב של האלגוריתם מאופיין על ידי שלושה ערכים: {% equation %}a_{n},m_{n},d_{n}{% endequation %}. שלושת אלו קובעים את השלב הבא של האלגוריתם ({% equation %}a_{n+1},m_{n+1},d_{n+1}{% endequation %}). האלגוריתם מתחיל לחזור על עצמו בדיוק כשאנחנו חוזרים לשלשה שכבר היינו בה.

חזרה לשורש 19. הפעלת האלגוריתם עליו "עד הסוף" מניבה את השבר המשולב המחזורי הבא: {% equation %}\left[4,2,1,3,1,2,8,2,1,3,1,2,8,\dots\right]{% endequation %}, כאשר המספרים הללו הם סדרת ה-{% equation %}a_{n}{% endequation %}-ים. אתם רואים שבאופן לא מפתיע זה מציית לתבנית שתיארתי - {% equation %}q_{0}=4{% endequation %} הוא החלק ההתחלתי, החלק המחזורי הסימטרי הוא {% equation %}2,1,3,1,2{% endequation %}, וה-{% equation %}8{% endequation %} הוא {% equation %}2q_{0}{% endequation %}.

מה עושים עכשיו?

לוקחים את החלק מהשבר המשולב עד <strong>ולא כולל</strong> {% equation %}2q_{0}{% endequation %}, כלומר את {% equation %}\left[4,2,1,3,1,2\right]{% endequation %}. זה שבר משולב סופי, ולכן הוא מייצג מספר רציונלי שאפשר לחשב עד הסוף. אם נעשה זאת, נקבל {% equation %}\frac{170}{39}{% endequation %}. כעת מגדירים {% equation %}x=170,y=39{% endequation %}, מחשבים את {% equation %}x^{2}-19y^{2}{% endequation %} ומגלים, למרבה התדהמה, שקיבלנו 1! מצאנו פתרון למשוואת פל עם הפרמטר {% equation %}N=19{% endequation %}, ולא סתם פתרון - את הפתרון היסודי!

אם המתמטיקה לא נראית לכם כמו קסם אפילו עכשיו, אין לי מושג איך עוד אפשר לשכנע אתכם. כמובן שיש הסבר הגיוני מאחורי כל זה ונראה אותו, אבל בינתיים בואו נעצור לשניה ונעריך את הקסם שיש כאן. אין לי מושג איך הגיעו לתגלית הזו לראשונה (דומני שהיה זה לגראנז' שהוכיח את הזהות בין שברים משולבים מחזוריים אינסופיים ופתרונות של משוואות ריבועיות, ואילו ברוקנר היה זה שמצא את הקשר בינם לבין משוואת פל, אבל אולי אני טועה), אבל אני מנחש שזה היה בראש ובראשונה על ידי התקלות ב<strong>תגלית</strong> לפיה התופעה המתרחשת הזו מתקיימת - שיש קשר הדוק בין המספרים הרציונליים שמתקבלים בפיתוח לשבר משולב של {% equation %}\sqrt{N}{% endequation %} והפתרונות של משוואת פל עבור הפרמטר {% equation %}N{% endequation %} (המספרים הרציונליים שמתקבלים בפיתוח של {% equation %}\sqrt{N}{% endequation %} הם לא מקריים; בפוסטים על שברים משולבים ניסיתי להסביר למה אלו במובן מסויים "הקירובים הטובים ביותר" של {% equation %}\sqrt{N}{% endequation %} על ידי מספרים רציונליים).

מה שעשיתי עבור {% equation %}N=19{% endequation %} תקף תמיד, כמובן. בהינתן {% equation %}N{% endequation %}, מפתחים את {% equation %}\sqrt{N}{% endequation %} לשבר משולב מחזורי אינסופי, לוקחים את המספר הרציונלי שמתאים לשבר המשולב שמתקבל מעצירת הסדרה המחזורית בדיוק בתום המחזור הראשון שלה, לפני {% equation %}q_{0}{% endequation %}; המונה יהיה {% equation %}x{% endequation %} והמכנה יהיה {% equation %}y{% endequation %}. הבעיה היחידה היא שלא תמיד יתקיים {% equation %}x^{2}-Ny^{2}=1{% endequation %}, כי עלול להתקיים גם {% equation %}x^{2}-Ny^{2}=-1{% endequation %}, אבל בכל מקרה נקבל את היוצר של כל ההפיכים ב-{% equation %}\mathbb{Z}\left[\sqrt{N}\right]{% endequation %} ולכן נוכל לקבל ממנו את כל הפתרונות.

זהו, עכשיו אתם יודעים לפתור, אלגוריתמית, את משוואת פל. כמובן, הייתי יכול לתת את האלגוריתם חיש קל בתחילת הפוסט (הוא בסך הכל פשוט למדי, עניין של כמה שורות) אבל עכשיו אני מקווה שאנחנו גם מבינים בערך <strong>מה</strong> הולך פה, גם אם אנחנו עדיין לא מבינים למה הקסם עם השבר המשולב עובד.

בואו נעבור להסבר של הקסם הזה - הסבר שיהיה כרוך, כמובן, בפרטים טכניים.

טוב, אז בואו נסמן את השבר שמתקבל מהשבר המשולב עד ולא כולל {% equation %}2q_{0}{% endequation %} בתור {% equation %}\frac{A_{n}}{B_{n}}{% endequation %}, ונסמן את השבר שבא לפניו (כלומר, לא כולל האיבר שממש לפני {% equation %}2q_{0}{% endequation %}) בתור {% equation %}\frac{A_{n-1}}{B_{n-1}}{% endequation %}. אנחנו רוצים להוכיח ש-{% equation %}A_{n}^{2}-NB_{n}^{2}=\pm1{% endequation %}. זה מוכיח שאנחנו מקבלים פתרון; זה עדיין לא מוכיח שהוא הפתרון היסודי, אבל זה כבר באמת יהיה קצת יותר מדי עבורנו.

בואו ניזכר בתוצאה שהוכחנו בדי עמל בפוסט הראשון שלי על שברים משולבים: באופן כללי, אפשר לפתח את המספר {% equation %}\alpha{% endequation %} לשבר משולב תוך שאנו מרשים למספר האחרון להיות לא שלם, ומסמנים אותו בסימון {% equation %}\alpha_{n+1}{% endequation %}, כלומר {% equation %}\alpha=a_{0}+\frac{1}{a_{1}+}\frac{1}{a_{2}+}\cdots\frac{1}{a_{n}+}\frac{1}{\alpha_{n+1}}{% endequation %}. עבור {% equation %}\alpha_{n+1}{% endequation %} הזה הוכחנו שמתקיימת המשוואה

{% equation %}\alpha=\frac{\alpha_{n+1}A_{n}+A_{n-1}}{\alpha_{n+1}B_{n}+B_{n-1}}{% endequation %}

אז בואו נחיל את זה על המקרה שלנו. אצלנו {% equation %}\alpha{% endequation %} הוא {% equation %}\sqrt{N}{% endequation %} שמיוצג על ידי השבר המשולב {% equation %}\left[q_{0},q_{1},\dots,q_{n},2q_{0},q_{1},\dots,q_{n},2q_{0},q_{1},\dots\right]{% endequation %}, ואילו {% equation %}\frac{A_{n}}{B_{n}}=\left[q_{0},q_{1},\dots,q_{n}\right]{% endequation %} ו-{% equation %}\frac{A_{n-1}}{B_{n-1}}=\left[q_{0},q_{1},\dots,q_{n-1}\right]{% endequation %}, והכי חשוב - {% equation %}\alpha_{n+1}=\left[2q_{0},q_{1},\dots,q_{n},2q_{0},q_{1},\dots\right]{% endequation %}. שימו לב כמה הוא דומה ל-{% equation %}\sqrt{N}{% endequation %} - ההבדל היחיד הוא האיבר הראשון, שהוא {% equation %}2q_{0}{% endequation %} במקום {% equation %}q_{0}{% endequation %}. כלומר מתקיים ש-{% equation %}\alpha_{n+1}=q_{0}+\sqrt{N}{% endequation %}.

הבה ונציב את כל זה במשוואה שלעיל, ונקבל:

{% equation %}\sqrt{N}=\frac{\left(q_{0}+\sqrt{N}\right)A_{n}+A_{n-1}}{\left(q_{0}+\sqrt{N}\right)B_{n}+B_{n-1}}{% endequation %}

נכפול את שני האגפים במכנה של אגף ימין ונקבל:

{% equation %}\sqrt{N}\left(q_{0}+\sqrt{N}\right)B_{n}+\sqrt{N}B_{n-1}=\left(q_{0}+\sqrt{N}\right)A_{n}+A_{n-1}{% endequation %}

למשוואה הזו תכונה מעניינת - היא למעשה כוללת שתי משוואות שונות. זאת מכיוון שפרט ל-{% equation %}\sqrt{N}{% endequation %}, כל שאר המספרים במשוואה הם שלמים, ולכן כפל שלהם ב-{% equation %}\sqrt{N}{% endequation %} מותיר אותו אי רציונלי. אז אפשר לחשוב על המשוואה הזו כאילו היא מהצורה {% equation %}a_{1}+b_{1}\sqrt{N}=a_{2}+b_{2}\sqrt{N}{% endequation %} ולהסיק את זוג המשוואות

{% equation %}a_{1}=a_{2}{% endequation %}

{% equation %}b_{1}=b_{2}{% endequation %}

(נסו להוכיח פורמלית שאכן אפשר להסיק את שתי המשוואות הללו).

במקרה שלנו, אחרי פישוט, נקבל שהמשוואה לעיל יכולה להיכתב כך:

{% equation %}NB_{n}+\left(q_{0}B_{n}+B_{n-1}\right)\sqrt{N}=q_{0}A_{n}+A_{n-1}+A_{n}\sqrt{N}{% endequation %}

ומכאן שתי המשוואות:

{% equation %}NB_{n}=q_{0}A_{n}+A_{n-1}{% endequation %}

{% equation %}q_{0}B_{n}+B_{n-1}=A_{n}{% endequation %}

אפשר מהמשוואות הללו לחלץ את {% equation %}A_{n-1}{% endequation %} ואת {% equation %}B_{n-1}{% endequation %}:

{% equation %}A_{n-1}=NB_{n}-q_{0}A_{n}{% endequation %}

{% equation %}B_{n-1}=A_{n}-q_{0}B_{n}{% endequation %}

וכעת אפשר לשלוף עוד נוסחה מהפוסט הראשון שלי על שברים משולבים, נוסחה יפהפיה במיוחד:

{% equation %}A_{n}B_{n-1}-A_{n-1}B_{n}=\left(-1\right)^{n-1}{% endequation %}

נציב את {% equation %}A_{n-1},B_{n-1}{% endequation %} בנוסחה הזו ונקבל:

{% equation %}A_{n}\left(A_{n}-q_{0}B_{n}\right)-B_{n}\left(NB_{n}-q_{0}A_{n}\right)=\left(-1\right)^{n-1}{% endequation %}

נפתח סוגריים ונקבל:

{% equation %}A_{n}^{2}-q_{0}A_{n}B_{n}-NB_{n}^{2}+q_{0}A_{n}B_{n}=\left(-1\right)^{n-1}{% endequation %}

ולסיום, קיבלנו:

{% equation %}A_{n}^{2}-NB_{n}^{2}=\left(-1\right)^{n-1}{% endequation %}

שזה בדיוק מה שרצינו.

בשבילי כל העסק הזה הוא כל כך Mind Blowing שאני חושב שאעצור כאן לפני שהמקלדת תתפוצץ.

